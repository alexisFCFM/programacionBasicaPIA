import os

def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
