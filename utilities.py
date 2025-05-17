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
    movimientos = [movimiento['move']['name'] for movimiento in pokemon['moves'][:4]]
    print(f"{','.join(movimientos).capitalize()}")
        
        
    
def descargarPokemon(pokeName, pokeJson):
    nombrePokemon = pokeJson['name']
    numeroPokedex = pokeJson['id']
    tipos = Tipos(pokeJson)
    habilidades = Habilidades(pokeJson)
    altura = pokeJson['height']
    peso = pokeJson['weight']
    stats = Estadisticas(pokeJson)
    movimientos = [movimiento['move']['name'] for movimiento in pokeJson['moves'][:4]]
    

    pokemonDicc[pokeName] = {
        "nombre" : nombrePokemon, 
        "id" : numeroPokedex,
        "tipos" : tipos,
        "habilidades": habilidades,
        "altura" : altura,
        "peso" :peso,
        "estadisticas": stats,
        "movimientos": movimientos
    }
   
    with open("diccionarioLocal.json", 'w', encoding='utf-8') as archivo:
        json.dump(pokemonDicc, archivo, ensure_ascii=False, indent=4)


def cargarPokemon():
    with open("diccionarioLocal.json", 'r') as diccLocal:
        tempDicc = json.load(diccLocal)
    
    for nombre in tempDicc.keys():
        nombrePokemon = tempDicc[nombre]['nombre']
        numeroPokedex = tempDicc[nombre]['id']
        tipos = tempDicc[nombre]['tipos']
        habilidades = tempDicc[nombre]['habilidades']
        altura = tempDicc[nombre]['altura']
        peso = tempDicc[nombre]['peso']
        stats = tempDicc[nombre]['estadisticas']
        movimientos = tempDicc[nombre]['movimientos']
    

        pokemonDicc[nombre] = {
            "nombre" : nombrePokemon, 
            "id" : numeroPokedex,
            "tipos" : tipos,
            "habilidades": habilidades,
            "altura" : altura,
            "peso" :peso,
            "estadisticas": stats,
            "movimientos": movimientos
        }




