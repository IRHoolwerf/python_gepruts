import requests
import pandas as pd

base_url = "https://pokedex.mimo.dev/api/pokemon/"

def get_pokemons():
  """"
  Haal alle Pokemons op uit de Mimo Pokedex API en print ze als DataFrame
  """
  response = requests.get(base_url)
  if response.status_code == 200: 
    print("Pokemons successfully retrieved")
    pokemon_data = response.json()
    df = pd.DataFrame(pokemon_data)
    print(df)
  else:
    print("Failed to retrieve Pokemons")


def get_pokemon(pokemon):
  """
  Haal een specifieke Pokemon op uit de Mimo Pokedex API en print de naam en ID

  Args:
      pokemon (str): Naam of ID van de Pokemon
  """
  response = requests.get(base_url+pokemon)
  if response.status_code == 200: 
    print("Pokemon successfully retrieved")
    pokemon_data = response.json()
    print(f"Name:{pokemon_data['name']}")
    print(f"ID:{pokemon_data['id']}")
  else:
    print("Failed to retrieve Pokemon")

#get_pokemons()
get_pokemon("5")