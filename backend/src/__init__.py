from flask import Flask, request
from flask_cors import CORS
from flask_restx import Resource, Api
from flask_pymongo import PyMongo
from pymongo.collection import Collection

# for the models
import os, re
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModel
import torch
from joblib import dump, load
from sklearn.preprocessing import OneHotEncoder
import tensorflow as tf
from tensorflow import keras
import pickle
import logging

from .model import Company # ?
import json

# Configure Flask & Flask-PyMongo:
app = Flask(__name__)
# allow access from everywhere
cors = CORS()
cors.init_app(app, resources={r"*": {"origins": "*"}})
app.config["MONGO_URI"] = "mongodb://localhost:27017/companiesdatabase"
pymongo = PyMongo(app)

# Get a reference to the companies collection.
companies: Collection = pymongo.db.companies

api = Api(app)

app.logger.info("==> BACKEND: imports done!")

# --------------------------------------------------------------------------------------------------------

# Get Docker global variables - OR MAYBE NO DOCKER NOW
STORAGE_DIR = os.path.join(os.getcwd(), "backend_storage/")

# Now all the setup for the ML model
with open(os.path.join(STORAGE_DIR, 'curr2eur.json'),'r') as json_file:
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
one_hot_neighborhood = load(os.path.join(STORAGE_DIR, 'one_hot_neighborhood.joblib'))

# load the nlp model
nlp_model = keras.models.load_model(os.path.join(STORAGE_DIR, "nlp_model.h5"))

# other one hot encoders
one_hot_city = load(os.path.join(STORAGE_DIR, "one_hot_city.joblib"))
one_hot_room_type = load(os.path.join(STORAGE_DIR, "one_hot_room_type.joblib"))

cities = list(one_hot_city.get_feature_names_out())
cities = [re.sub("\s", "_", city) for city in cities]

room_types = list(one_hot_room_type.get_feature_names_out())
room_types = [re.sub("\s", "_", room_type) for room_type in room_types]

# price encoding for neighborhoods
with open(os.path.join(STORAGE_DIR, 'neighbourhood_prices_dict.json','r')) as json_file:
   neighbourhood_prices_dict = json.load(json_file)

price_model = pickle.load(open(os.path.join(STORAGE_DIR, 'linear_model.pickle'), 'rb'))

feature_order = ['neighbourhood_names_embedded', 'neighbourhood', 'minimum_nights', 'reviews_per_month',
      'room_type_Entire_home/apt', 'room_type_Hotel_room', 'room_type_Private_room', 'room_type_Shared_room',
      'city_berlin', 'city_copenhagen', 'city_oslo', 'city_paris', 'city_rome', 'city_san-francisco', 'city_stockholm', 'city_zurich']

numeric_cols = ['minimum_nights']

# --------------------------------------------------------------------------------------------------------
app.logger.info("==> BACKEND: setup done! Ready for inference!")

class PredictPrice(Resource):
    # TODO return algorithm result(price prediction)
    def get(self, args=None):
        print("## PredictPrice ##")
        args = request.args.to_dict()
        app.logger.info("==> BACKEND: args: ", args)
        return json.dumps({"status": "Success"})

class CompaniesList(Resource):
    def get(self, args=None):
        args = request.args.to_dict()
        print(args)
        if args['category'] == 'All':
            cursor = companies.find()
        else:
            cursor = companies.find(args)
        # print([Company(**doc).to_json() for doc in cursor])
        return [Company(**doc).to_json() for doc in cursor]


class Companies(Resource):
    def get(self, id):
        import pandas as pd
        from statsmodels.tsa.ar_model import AutoReg
        # search for the company by ID
        cursor = companies.find_one_or_404({"id": id})
        company = Company(**cursor)
        # retrieve args
        args = request.args.to_dict()
        print(args)
        # retrieve the profit
        profit = company.profit
        # add to df
        profit_df = pd.DataFrame(profit).iloc[::-1]

        if args['algorithm'] == 'random':
            # retrieve the profit value from 2021
            prediction_value = int(profit_df["value"].iloc[-1])
            # add the value to profit list at position 0
            company.profit.insert(0, {'year': 2022, 'value': prediction_value})
        elif args['algorithm'] == 'regression':
            # create model
            model_ag = AutoReg(endog=profit_df['value'], lags=1, trend='c', seasonal=False, exog=None, hold_back=None,
                               period=None, missing='none')
            # train the model
            fit_ag = model_ag.fit()
            # predict for 2022 based on the profit data
            prediction_value = fit_ag.predict(start=len(profit_df), end=len(profit_df), dynamic=False).values[0]
            # add the value to profit list at position 0
            company.profit.insert(0, {'year': 2022, 'value': prediction_value})
        print(company.to_json())
        return company.to_json()





api.add_resource(CompaniesList, '/companies')
api.add_resource(Companies, '/companies/<int:id>')
api.add_resource(PredictPrice, '/PredictPrice')
