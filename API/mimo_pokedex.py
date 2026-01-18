import requests

url = "https://pokedex.mimo.dev/api/pokemon/pikachu"

response = requests.get(url)

if response.status_code == 200: 
  print("Data successfully retrieved")
  pokemon_data = response.json()
  print(f"Name:{pokemon_data['name']}")
  print(f"ID:{pokemon_data['id']}")
else
  print("Failed to retrieve data")