import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    """
     Fetches the animals data for the animal 'animal_name'.
     Returns: a list of animals, each animal is a dictionary:
     {
       'name': ...,
       'taxonomy': {
         ...
       },
       'locations': [
         ...
       ],
       'characteristics': {
         ...
       }
     },
     """
    url = 'https://api.api-ninjas.com/v1/animals'
    headers = {'X-Api-Key': API_KEY }
    params = {'name': {animal_name}}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        animal_data = response.json()
        return animal_data
    else:
        print(f'Error: {response.status_code} - {response.text}')
