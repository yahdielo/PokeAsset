import requests

class Pokemon():

    def __init__(self, *args, **kwargs):

        self.id = 0
        self.name = "empty"
        self.type = "empty"
        self.attack = "empty"
        self.defense = "empty"
        self.speed = "empty"
        self.spattack = "empty"
        self.spdefence = "empty"

        if kwargs:
            for keys, value in kwargs.items():
                if keys in self.__dict__:
                    self.__dict__[keys] = value
                else:
                    pass

class Pikachu(Pokemon):

    def __init__(self, *args, **kwargs):

        self.id = 25
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.id}/")
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            self.name = data["name"]

            
        if kwargs:
            for keys, value in kwargs.items():
                if keys in self.__dict__:
                    self.__dict__[keys] = value
                else:
                    pass


## Testing classes
test = Pokemon()
print(test.name)

test2 = Pikachu()
print(test2.name)