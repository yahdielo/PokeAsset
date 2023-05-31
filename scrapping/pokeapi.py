import pokepy

client = pokepy.V2Client()
pokemon = client.get_pokemon(1)

print(pokemon)