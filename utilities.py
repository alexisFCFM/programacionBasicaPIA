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
    
def Movimientos (pokemon):
     print("")
     print("ADVERTENCIA")
     print("La mayoria de pokemon aprenden una gran cantidad de movmientos")
     try:

        numMov = int(input("Por favor elija la cantidad de movmientos que desee ver: "))
        movimientos = [movimiento['move']['name'] for movimiento in pokemon['moves'][:numMov]]
        print(f"{','.join(movimientos).capitalize()}")
        print("")
        input("Pulse cualquier tecla para continuar")

     except:
          print("")
          input("Ingrese un valor valido")

