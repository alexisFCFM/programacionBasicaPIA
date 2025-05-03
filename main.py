from utilities import *

close = False

while(close != True):
    print("PokeApi")
    pokeSelect = input("Ingrese el pokemon que desea consultar: ")
    
    respuesta = requests.get(apiUrl + pokeSelect.lower())

    if(respuesta.status_code != 200):
       print("Ingrese un valor valido...")
       input("Pulse cualquier tecla para continuar")
       limpiarConsola()
    
    else:
      pokeData = respuesta.json()
      guardarPokemon(pokeSelect.lower(),pokeData)

      while(close != True):
            limpiarConsola()
            print(f"Pokedex de {pokeSelect}\n")
            print("1. Estadisticas base")
            print("2. Habilidades")
            print("3. Moviminetos")
            print("4. Guardar pokemon ya buscadoes en txt")       
            print("5. Cambiar pokemon seleccionado" )
            print("6. Salir")

            opc = input("Ingrese el numero de la opcion que desee consultar: ")

            if(opc == "1"):
               print("")
               Estadisticas(pokeData)
               print("")
               input("Pulse cualquier tecla para continuar")
               limpiarConsola()
              

            elif(opc == "2"):
               print()
               Habilidades(pokeData)
               print("")
               input("Pulse cualquier tecla para continuar")
               limpiarConsola()

            elif(opc == "3"):
               Movimientos(pokeData)
               print("")
               input("Pulse cualquier tecla para continuar")
               limpiarConsola()

            elif(opc == "4"):
               nombreUsuario = input("Seleccione un nombre para su archivo txt: ")
               
               with open(nombreUsuario +'.txt', 'w', encoding='utf-8') as archivo:
                  json.dump(pokemonDicc, archivo, ensure_ascii=False, indent=4)
              
               print("Archivo exportado")
               input("Pulse cualquier tecla para continuar")
               limpiarConsola()

            elif(opc == "5"):
               limpiarConsola()
               break
            
            elif(opc == "6"):
               close = True
               

            else:
               print("Elija una opcion valida...")
               input("Precione cualquier tecla para continuar...")
               limpiarConsola()
      
      
