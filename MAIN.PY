from distutils.debug import DEBUG
from distutils.log import debug
from flask import Flask, request, Response
import json

app = Flask(__name__)

animals_db = {
    "ANIMAL_1": 
    { "GIRAFFE": "FEMALE", 
        "TRANSFER_DATE": "1999"}, 

    "ANIMAL_2": 
    { "TIGER": "FEMALE", 
    "TRANSFER_DATE": "2009"}, 

    "3":
    { "LION": "MALE", 
    "TRANSFER_DATE": "2005" }
}


@app.route("/")
def home(): 
    return "PLEASE FIND NEXT SOME INFO ON ZOO MANAGEMENT"

@app.route("/ZOOAPPMAN")
def list_animals(): 
    return animals_db 

@app.route("/animal/<animal_id>")
def get_animal(animal_id): 
    return animals_db[animals_db]

@app.route("/animal/add", methods=['POST'])
def add_animal():
    # Collect the new animal from the user/url
    request_data = request.get_json()

    # Extract the animal data from the request
    new_animal = request_data['animal']

    # Get the last position in the database
    new_id = len(animals_db) +1

    # Create a new entry for my animal
    new_animal_data = { str(new_id) : new_animal}

    # update the database with the new entry 
    animals_db.update(new_animal_data)
    return "animal was added"

@app.route("/animal/update", methods=['POST'])
def update_animal():
    # Collect the new animal from the user/url
    request_data = request.get_json()

    # update the database with the new entry 
    animals_db.update(request_data)
    return "animal was updated"

    

if __name__ == "__main__":
     app.run(host="127.0.0.1")


