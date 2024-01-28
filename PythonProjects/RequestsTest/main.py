"""
POST запрос на создание покемона
"""
import requests
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token':'1ea328b98c63b267c0108a296dcbc606'}

body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER)
print('status' , response.status_code, 'CREATED')
print(response.json()) 


"""
PUT смена имени покемона
""" 

import requests
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token':'1ea328b98c63b267c0108a296dcbc606'}

body = {
    "pokemon_id": "28802",
    "name": "Factor",
    "photo": "https://dolnikov.ru/pokemons/albums/070.png"
    }

response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER)
print('status' , response.status_code, 'OK')
print(response.json())


"""
POST поймать покемона в покебол
""" 

import requests
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token':'1ea328b98c63b267c0108a296dcbc606'}

body = {
         "pokemon_id": "28804"
       }

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER)
print('status' , response.status_code, 'OK')
print(response.json())
