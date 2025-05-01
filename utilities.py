import os
import requests

apiUrl = "https://pokeapi.co/api/v2/pokemon/"

def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
