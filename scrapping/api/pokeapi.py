import requests
import sys
"""
    This module is a simple api request to pokeapi
    to get basic information of a certain character,
    this modules makes a request converts it to json and returns a dictionary,
    with name , id, and a url to a spite.png. it also downloads the sprite.png file
    and saves it in the ./imgss directory as <character_name>_sprite.png
 """

#pokemon = sys.argv


def get_character_info(character_name):


    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{character_name}/")

    if response.status_code == 200:
       data = response.json()
       atributes = {
           "id" : data["id"],
            "name" : data["name"],
            "sprites" : data["sprites"]["front_default"],
        }
    print(atributes['id'])
    sprite_img = data["sprites"]["front_default"]
    if sprite_img:
        with open(f"./imgs/{character_name}_sprite.png", "wb") as f:
            f.write(sprite_img.encode())
        print("Sprite downloaded successfully.")
    else:
        print("Failed to retrieve Charizard's sprite.")

    return atributes


character_data = get_character_info("pikachu")

