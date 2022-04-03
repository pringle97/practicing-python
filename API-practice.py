import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
pokemon = print(response.json())
print(pokemon['image'])