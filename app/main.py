

from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://mongo:27017")
db = client['pets_db']
collection = db['pets_collection']


class Pet(BaseModel):
    name: str
    pet_type: str
    status: str


@app.post('/create_pet')
async def create_pet(pet: Pet):
    pet_doc = pet.dict()
    insert_result = collection.insert_one(pet_doc)
    return {"message": "Pet created successfully", "pet_id": str(insert_result.inserted_id)}
