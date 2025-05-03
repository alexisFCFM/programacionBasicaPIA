import os
import requests
import json

apiUrl = "https://pokeapi.co/api/v2/pokemon/"


pokemonDicc = {}


pokemonHabilidadesDicc = {}
pokemonHabilidades = []

pokemonMovimientosDicc = {}
pokemonMovimientos = [] 

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

def guardarPokemon(pokemonSave,pokemon):
     for ability in pokemon["abilities"]:
        pokemonHabilidades.append(ability["ability"]["name"])

     for movimiento in pokemon['moves'][:5]:
        pokemonMovimientos.append(movimiento['move']['name'])
   

     pokemonHabilidadesDicc["Habilidades"] = pokemonHabilidades
     pokemonMovimientosDicc["Movimientos"] = pokemonMovimientos

     pokemonDicc[pokemonSave] = pokemonHabilidadesDicc, pokemonMovimientosDicc  

     
     print(pokemonDicc)
     input()
