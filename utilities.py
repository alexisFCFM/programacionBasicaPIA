import os
import requests
import json



apiUrl = "https://pokeapi.co/api/v2/pokemon/"



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
    print("")
    input("Pulse cualquier tecla para continuar")   

def Habilidades(pokemon):
    for ability in pokemon["abilities"]:
                print(ability["ability"]["name"])
    print("")
    input("Pulse cualquier tecla para continuar")
    
