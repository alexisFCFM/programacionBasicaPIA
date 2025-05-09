import os
import requests
import json

apiUrl = "https://pokeapi.co/api/v2/pokemon/"


pokemonDicc = {}


def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def Estadisticas(pokemon):
    for stat in pokemon['stats']:
        nombre_stat = stat['stat']['name']
        valor_stat = stat['base_stat']
        print(f"{nombre_stat.capitalize()}:{valor_stat}")
       

def Habilidades(pokemon):
    for ability in pokemon["abilities"]:
                print(ability["ability"]["name"])
    
    
def Movimientos (pokemon):
     print("")
     print("ADVERTENCIA")
     print("La mayoria de pokemon aprenden una gran cantidad de movmientos")
     try:

        numMov = int(input("Por favor elija la cantidad de movmientos que desee ver: "))
        movimientos = [movimiento['move']['name'] for movimiento in pokemon['moves'][:numMov]]
        print(f"{','.join(movimientos).capitalize()}")
        

     except:
          print("")
          input("Ingrese un valor valido")


     
def guardarPokemon(pokeName, pokemon):
    # Crear nuevas listas y diccionarios dentro de la función
    habilidades = [ability["ability"]["name"] for ability in pokemon["abilities"]]
    movimientos = [movimiento['move']['name'] for movimiento in pokemon['moves'][:4]]
    stats = {stat['stat']['name'].capitalize(): stat['base_stat'] for stat in pokemon['stats']}

    pokemonDicc[pokeName] = {
        "Habilidades": habilidades,
        "Movimientos": movimientos,
        "Estadisticas": stats
    }

