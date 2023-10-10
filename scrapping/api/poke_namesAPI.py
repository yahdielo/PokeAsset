import requests
'''This file contains the functions that interact with PokeAPI'''


def pokemon_names():
    '''Function that get the names of all pokemon, returns a list
        
        Note: currently only the OG 150 pokemon names are pull'''
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=150')
    result = response.json()
    pokemon_names = []
    poke_id = 1
    for j in result['results']:
        pokemon_names.append(j['name'])
    return(pokemon_names)

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   pokemon_names()