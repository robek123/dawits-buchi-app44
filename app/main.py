

@app.get('/get_all_pets')
async def get_all_pets():
    pets_list = []
    for pet in collection.find():
        pets_list.append(pet)
    return pets_list
