import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"

def get_pokemon_id(url):

   response = requests.get(url)
   print(response)

get_pokemon_id(url)