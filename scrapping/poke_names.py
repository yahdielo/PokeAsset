import requests
'''This file contains the functions that interact with PokeAPI'''


def pokemon_names():
    '''Function that get the names of all pokemon, returns a list'''
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=150')
    result = response.json()
    pokemon_names = []
    poke_id = 1
    for j in result['results']:
        pokemon_names.append(j['name'])
    return(pokemon_names)

pokemon_names()