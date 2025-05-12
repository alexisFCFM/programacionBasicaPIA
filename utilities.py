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
    returnStats = {stat['stat']['name'].capitalize(): stat['base_stat'] for stat in pokemon['stats']}
    return returnStats
          

def Habilidades(pokemon):
    returnMov = [ability["ability"]["name"] for ability in pokemon["abilities"]]
    return returnMov            

def Tipos(pokemon):
    returnType = [types["type"]["name"] for types in pokemon["types"]]
    return returnType

    
    
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
     
def descargarPokemon(pokeName, pokeJson):
    numeroPokedex = pokeJson['id']
    tipos = Tipos(pokeJson)
    habilidades = Habilidades(pokeJson)
    altura = pokeJson['height']
    peso = pokeJson['weight']
    stats = Estadisticas(pokeJson)
    movimientos = [movimiento['move']['name'] for movimiento in pokeJson['moves']]
    

    pokemonDicc[pokeName] = {
        "id" : numeroPokedex,
        "tipo" : tipos,
        "habilidades": habilidades,
        "altura" : altura,
        "peso" :peso,
        "estadisticas": stats,
        "movimientos": movimientos
    }

    with open("diccionarioLocal" +'.json', 'w', encoding='utf-8') as archivo:
        json.dump(pokemonDicc, archivo, ensure_ascii=False, indent=4)




