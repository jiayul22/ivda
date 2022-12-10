from flask import Flask, request
from flask_cors import CORS
from flask_restx import Resource, Api
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from .model import House

# for the models
import os, re
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModel
import torch
from joblib import dump, load
import pickle
import logging
import json

# Configure Flask & Flask-PyMongo:
app = Flask(__name__)
# allow access from everywhere
cors = CORS()
cors.init_app(app, resources={r"*": {"origins": "*"}})

app.config["MONGO_URI"] = "mongodb://localhost:27017/Airbnb"
pymongo = PyMongo(app)
house: Collection = pymongo.db.house

api = Api(app)
app.logger.info("==> BACKEND: imports done!")

# --------------------------------------------------------------------------------------------------------
# --------------------------------------- SETUP EVERYTHING -----------------------------------------------
# --------------------------------------------------------------------------------------------------------
# Get Docker global variables - OR MAYBE NO DOCKER NOW
backend_storage = os.path.join(os.getcwd(), "backend_storage/")

# Now all the setup for the ML model
with open(os.path.join(backend_storage, 'curr2eur.json'),'r') as json_file:
    curr_to_eur = json.load(json_file)

#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return sum_embeddings / sum_mask

#Load AutoModel from huggingface model repository
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", device_map="auto", load_in_8bit=True, max_memory={0:"10GB"})
name_model = AutoModel.from_pretrained("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# one hot neighborhood
one_hot_neighborhood = load(os.path.join(backend_storage, 'one_hot_neighborhood.joblib'))

# load the nlp model - without tf this time
hidden1_weights = np.load(os.path.join(backend_storage, 'hidden1_weights.npy'))
hidden1_biases = np.load(os.path.join(backend_storage, 'hidden1_biases.npy'))
out_weights = np.load(os.path.join(backend_storage, 'out_weights.npy'))
out_biases = np.load(os.path.join(backend_storage, 'out_biases.npy'))

def nlp_model_predict(x):
    hidden_1 = np.dot(x, hidden1_weights) + hidden1_biases
    # relu
    hidden_1[hidden_1<0] =0
    return np.dot(hidden_1, out_weights) + out_biases

# other one hot encoders
one_hot_city = load(os.path.join(backend_storage, "one_hot_city.joblib"))
one_hot_room_type = load(os.path.join(backend_storage, "one_hot_room_type.joblib"))

cities = list(one_hot_city.get_feature_names_out())
cities = [re.sub("\s", "_", city) for city in cities]

room_types = list(one_hot_room_type.get_feature_names_out())
room_types = [re.sub("\s", "_", room_type) for room_type in room_types]

city_neighborhoods = load(os.path.join(backend_storage, 'city_neighborhoods.joblib'))
city_names = list(city_neighborhoods.keys())

def process_city_name(name):
    return name.lower().replace(' ', '-')

# price encoding for neighborhoods
with open(os.path.join(backend_storage, 'neighbourhood_prices_dict.json'),'r') as json_file:
    neighbourhood_prices_dict = json.load(json_file)

price_model_coef = np.load(os.path.join(backend_storage, 'price_model_coef.npy'))
price_model_intercept = np.load(os.path.join(backend_storage, 'price_model_intercept.npy'))

def price_model_predict(input):
    # inputs is df or np array.
    x = np.array(input)
    return np.exp(np.dot(x, price_model_coef) + price_model_intercept)
    # returns scalar value for single input and array of values for multiple rows in input

feature_order = ['neighbourhood_names_embedded', 'neighbourhood',
'room_type_Entire_home/apt', 'room_type_Hotel_room', 'room_type_Private_room', 'room_type_Shared_room',
'city_berlin', 'city_copenhagen', 'city_oslo', 'city_paris', 'city_rome', 'city_san-francisco', 'city_stockholm', 'city_zurich']

app.logger.info("==> BACKEND: setup done! Ready for inference!")

# --------------------------------------------------------------------------------------------------------
# --------------------------------------- INFERENCE -----------------------------------------------------
# --------------------------------------------------------------------------------------------------------
def inference(raw_data):
    res = dict()

    if raw_data['name'] == '':
        raw_data['name'] = ' '

    raw_data['city'] = process_city_name(name)
    if raw_data['city'] not in city_neighborhoods:
        raw_data['city'] = 'berlin'
    if raw_data["neighbourhood"] not in neighbourhood_prices_dict:
        raw_data["neighbourhood"] = city_neighborhoods[raw_data['city']][0]

    # get name embeddings
    encoded_input = tokenizer([raw_data["name"]], padding=True, truncation=True, max_length=128, return_tensors='pt')
    # Compute token embeddings
    with torch.no_grad():
        model_output = name_model(**encoded_input)
    # Perform pooling. In this case, mean pooling
    name_embedding = mean_pooling(model_output, encoded_input['attention_mask'])

    # one hot encode neighborhood
    neighborhood_encoded = one_hot_neighborhood.transform([[raw_data["neighbourhood"]]])

    name_neighborhood = np.concatenate([name_embedding, neighborhood_encoded.toarray()], axis=1)
    res["neighbourhood_names_embedded"] = float(nlp_model_predict(name_neighborhood))

    # one hot encode others
    encoded = np.array(one_hot_city.transform([[raw_data["city"]]]).todense())[0]
    for i in range(len(cities)):
        res['city_' + cities[i][3:]] = encoded[i]

    encoded = np.array(one_hot_room_type.transform([[raw_data["room_type"]]]).todense())[0]
    for i in range(len(room_types)):
        res['room_type_' + room_types[i][3:]] = encoded[i]

    res['neighbourhood'] = neighbourhood_prices_dict[raw_data["neighbourhood"]]

    input = pd.DataFrame([res])[feature_order]

    pred = price_model_predict(input)

    feature_contr = dict(zip(feature_order, input.to_numpy()[0] * price_model_coef))
    return pred[0], feature_contr, res['neighbourhood'], res['neighbourhood_names_embedded']


# --------------------------------------------------------------------------------------------------------
# --------------------------------------- APIs ----------------------------------------------------------
# --------------------------------------------------------------------------------------------------------


class PredictPrice(Resource):
    def get(self, args=None):
        app.logger.info("==> BACKEND: Predict pice method")
        args = request.args.to_dict()
        app.logger.info("==> BACKEND: args: ", args)
        pred, feature_contr, avg, name_score = inference(args)
        weights = []

        room_type = 0.0
        city = 0.0
        for key in feature_contr:
            if key[0:4] == 'room' and feature_contr[key] > room_type:
                room_type = feature_contr[key]
            if key[0:4] == 'city' and feature_contr[key] > city:
                city = feature_contr[key]

        weight_dict = {
            'Name':np.exp(feature_contr['neighbourhood_names_embedded']),
            'Neighborhood':np.exp(feature_contr['neighbourhood']),
            'Room Type':np.exp(room_type),
            'City':np.exp(city)
        }

        weight_sort = dict(sorted(weight_dict.items(), key=lambda item: -item[1]))
        for k, v in weight_sort.items():
            weights.append({'feature':k, 'weight':v})

        message = {
            "price": f'{pred:.2f}',
            "weights": weights,
            "neighborhood_avg": f'{avg:.2f}',
            "name_score": f'{name_score:.2f}'
        }
        return message

class Get_Houses(Resource):
    def get(self):
        # args: {'city':['Zurich', 'Berlin', 'Copenhagen', 'Oslo', 'Paris', 'Rome', 'San Francisco', 'Stockholm']
        # 'feature':['Price', 'room type', 'minimum nights']}
        args = request.args.to_dict()
        raw_data = args.copy()

        def process_city_name(name):
             return name.lower().replace(' ', '-')
        raw_data['city'] = process_city_name(raw_data['city'])

        feature = raw_data['feature'].lower().replace(' ', '_')
        del raw_data['feature']

        if raw_data['city'] not in city_neighborhoods:
            raw_data['city'] = 'select'
        if raw_data['city'] == 'select':
            cursor = house.find()
        else:
            cursor = house.find(raw_data)
        print(raw_data)
        houses = [House(**doc) for doc in cursor]
        print(houses[0])
        if feature == 'price':
            houses = [float(h.price) for h in houses]
        elif feature == 'minimum_nights':
            houses = [float(h.minimum_nights) for h in houses]
        elif feature == 'room_type':
            houses = [h.room_type for h in houses]
            values, counts = np.unique(houses, return_counts=True)
            return {'x': values.tolist(), 'y': counts.tolist(), 'type': 'bar'}
        else:
            print(feature)
            houses = [h.to_json() for h in houses]
        return {'out':houses, "max":np.max(houses).item()}

class Get_Houses_Map(Resource):
    def get(self):
        # args: {'city':['Zurich', 'Berlin', 'Copenhagen', 'Oslo', 'Paris', 'Rome', 'San Francisco', 'Stockholm']
        # 'feature':['Price', 'room type', 'minimum nights']}
        args = request.args.to_dict()
        raw_data = args.copy()
        def process_city_name(name):
            return name.lower().replace(' ', '-')
        raw_data['city'] = process_city_name(raw_data['city'])

        cursor = house.find(raw_data)
        m = []
        for doc in cursor:
            h = House(**doc)
            m.append({'price':h.price, 'lat':float(h.latitude), 'lng':float(h.longitude)})

        message = {'out':m}
        return message

api.add_resource(Get_Houses, '/house')
api.add_resource(Get_Houses_Map, '/map')

api.add_resource(PredictPrice, '/PredictPrice')
