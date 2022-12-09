# handles converting objects to json
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel
from typing import List

"""
class Company(BaseModel):
    id: int
    name: str
    category: str
    founding_year: int
    employees: int
    profit: List

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    """

class House(BaseModel):
    id: str
    name: str
    host_id:str
    host_name:str
    neighbourhood_group:str
    neighbourhood:str
    latitude:str
    longitude:str
    room_type:str
    price:str
    minimum_nights: str
    number_of_reviews:str
    last_review:str
    reviews_per_month:str
    calculated_host_listings_count:str
    availability_365:str
    number_of_reviews_ltm:str
    city:str

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)
