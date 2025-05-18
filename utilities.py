import os
import requests
import json
import re
import numpy
import statistics
import matplotlib

apiUrl = "https://pokeapi.co/api/v2/pokemon/"
verificacionNombre = r'^[A-Za-z]+$'


pokemonDicc = {}


def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def Estadisticas(pokemon):
    print(f"Puntos de vida: {pokemonDicc[pokemon]['estadisticas']['Hp']}")
    print(f"Puntos de ataque: {pokemonDicc[pokemon]['estadisticas']['Attack']}")
    print(f"Puntos de defensa: {pokemonDicc[pokemon]['estadisticas']['Defense']}")
    print(f"Puntos de ataque especial: {pokemonDicc[pokemon]['estadisticas']['Special-attack']}")
    print(f"Puntos de defensa especial: {pokemonDicc[pokemon]['estadisticas']['Special-defense']}")
    print(f"Puntos de velocidad: {pokemonDicc[pokemon]['estadisticas']['Speed']}")
          
def Movimientos (pokemon):
    verificacionNumero = r'^(?!(0+(\.0+)?$))\d+(\.\d+)?$'
  
    movMax = input("Ingrese la catidad maxima de movimientos que desea ver: ")
    print()
    if (re.fullmatch(verificacionNumero, movMax)):
        for movimiento in pokemonDicc[pokemon]["movimientos"][:int(movMax)]:
            print(movimiento)

    else:
        print("Ingrese un valor valido...")
         

def sacarMedia(pokemon):
    tempHp = int(pokemonDicc[pokemon]['estadisticas']['Hp'])
    tempAttack = int(pokemonDicc[pokemon]['estadisticas']['Attack'])
    tempDefense = int(pokemonDicc[pokemon]['estadisticas']['Defense'])
    tempSpecialAtt = int(pokemonDicc[pokemon]['estadisticas']['Special-attack'])
    tempSpecialDef = int(pokemonDicc[pokemon]['estadisticas']['Special-defense'])
    tempSpeed = int(pokemonDicc[pokemon]['estadisticas']['Speed'])
    
    tempListaStats = [tempHp, tempAttack, tempDefense, tempSpecialAtt, tempSpecialDef, tempSpeed]  

    return numpy.mean(tempListaStats)


def sacarModa(pokemon):
    tempHp = int(pokemonDicc[pokemon]['estadisticas']['Hp'])
    tempAttack = int(pokemonDicc[pokemon]['estadisticas']['Attack'])
    tempDefense = int(pokemonDicc[pokemon]['estadisticas']['Defense'])
    tempSpecialAtt = int(pokemonDicc[pokemon]['estadisticas']['Special-attack'])
    tempSpecialDef = int(pokemonDicc[pokemon]['estadisticas']['Special-defense'])
    tempSpeed = int(pokemonDicc[pokemon]['estadisticas']['Speed'])
    
    tempListaStats = [tempHp, tempAttack, tempDefense, tempSpecialAtt, tempSpecialDef, tempSpeed]

    return statistics.mode(tempListaStats)


def sacarMediana(pokemon):
    tempHp = int(pokemonDicc[pokemon]['estadisticas']['Hp'])
    tempAttack = int(pokemonDicc[pokemon]['estadisticas']['Attack'])
    tempDefense = int(pokemonDicc[pokemon]['estadisticas']['Defense'])
    tempSpecialAtt = int(pokemonDicc[pokemon]['estadisticas']['Special-attack'])
    tempSpecialDef = int(pokemonDicc[pokemon]['estadisticas']['Special-defense'])
    tempSpeed = int(pokemonDicc[pokemon]['estadisticas']['Speed'])
    
    tempListaStats = [tempHp, tempAttack, tempDefense, tempSpecialAtt, tempSpecialDef, tempSpeed]

    return numpy.median(tempListaStats)


def sacarDerivacionEstandar(pokemon):
    tempHp = int(pokemonDicc[pokemon]['estadisticas']['Hp'])
    tempAttack = int(pokemonDicc[pokemon]['estadisticas']['Attack'])
    tempDefense = int(pokemonDicc[pokemon]['estadisticas']['Defense'])
    tempSpecialAtt = int(pokemonDicc[pokemon]['estadisticas']['Special-attack'])
    tempSpecialDef = int(pokemonDicc[pokemon]['estadisticas']['Special-defense'])
    tempSpeed = int(pokemonDicc[pokemon]['estadisticas']['Speed'])
    
    tempListaStats = [tempHp, tempAttack, tempDefense, tempSpecialAtt, tempSpecialDef, tempSpeed]

    return statistics.stdev(tempListaStats)


def descargarPokemon(pokeName, pokeJson):
   
    if(re.fullmatch(verificacionNombre, pokeJson['name'])):

        nombrePokemon = pokeJson['name']
        numeroPokedex = pokeJson['id']
        tipos = [types["type"]["name"] for types in pokeJson["types"]] #Tipos(pokeJson)
        habilidades = [ability["ability"]["name"] for ability in pokeJson["abilities"]] #Habilidades(pokeJson)
        altura = pokeJson['height']
        peso = pokeJson['weight']
        stats = {stat['stat']['name'].capitalize(): stat['base_stat'] for stat in pokeJson['stats']} #Estadisticas(pokeJson)
        movimientos = [movimiento['move']['name'] for movimiento in pokeJson['moves']]
    

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

    else:
        print("Datos corruptos. Cancelando registro")
        input("Precione cualquier tecla para continuar...")

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




