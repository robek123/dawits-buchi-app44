@app.post('/create_pet')
async def create_pet(pet_type: str, pet_name: str, status: str):
    new_pet = {
        'pet_type': pet_type,
        'pet_name': pet_name,
        'status': status
    }
    pet_id = collection.insert_one(new_pet).inserted_id
    return {'message': f'Pet created with id: {pet_id}'}


@app.get('/get_all_pets')
async def get_all_pets():
    pets_list = []
    for pet in collection.find():
        pets_list.append(pet)
    return pets_list
