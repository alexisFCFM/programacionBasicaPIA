import os
import requests
import json
import re
import numpy
import statistics
import matplotlib.pyplot as plt
import openpyxl
import pandas

apiUrl = "https://pokeapi.co/api/v2/pokemon/"
verificacionNombre = r'^[A-Za-z]+$'


pokemonDicc = {}


def limpiarConsola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def Estadisticas(pokemon):
    tempHP = int(pokemonDicc[pokemon]['estadisticas']['Hp'])
    tempAtt = int(pokemonDicc[pokemon]['estadisticas']['Attack'])
    tempDef = int(pokemonDicc[pokemon]['estadisticas']['Defense'])
    tempAttSpe = int(pokemonDicc[pokemon]['estadisticas']['Special-attack'])
    tempDefSpe = int(pokemonDicc[pokemon]['estadisticas']['Special-defense'])
    tempSpeed = int(pokemonDicc[pokemon]['estadisticas']['Speed'])


    fig, ax = plt.subplots()

    nomStats = ['vida', 'ataque', 'defensa', 'ataque especial', 'defensa especial', 'velocidad']
    numStats = [tempHP, tempAtt, tempDef, tempAttSpe, tempDefSpe, tempSpeed]
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange','tab:red', 'tab:blue']

    ax.bar(nomStats, numStats, color=bar_colors)

    ax.set_ylabel('Puntos de estadística')
    ax.set_title('Estadísticas del personaje')

    plt.show()

    
          
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


def exportarExel(pokemon):
    diccExel = {}
  
    for nombre in pokemonDicc.keys():

        diccExel[nombre] = pokemonDicc[nombre]['estadisticas']
    

    exportar =  pandas.DataFrame(diccExel)
    exportar.index = ["vida","ataque","defensa","ataque especial", "defensa especial", "velocidad"]

    nom = input("Ingrese el nombre del archivo de excel que desee: ")

    archivoExcel = pandas.ExcelWriter(nom + ".xlsx", engine='openpyxl')
    exportar.to_excel(archivoExcel, sheet_name="Hoja1", index=True)
    archivoExcel._save()
    print("Archivo exportado")

    



def descargarPokemon(pokeName, pokeJson):
   
    if(re.fullmatch(verificacionNombre, pokeJson['name'])):

        nombrePokemon = pokeJson['name']
        numeroPokedex = pokeJson['id']
        tipos = [types["type"]["name"] for types in pokeJson["types"]] 
        habilidades = [ability["ability"]["name"] for ability in pokeJson["abilities"]] 
        altura = pokeJson['height']
        peso = pokeJson['weight']
        stats = {stat['stat']['name'].capitalize(): stat['base_stat'] for stat in pokeJson['stats']} 
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




