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

      
      
      
      while(close != True):
            limpiarConsola()
            print(f"Pokedex de {pokeSelect}\n")
            print("1. Estadisticas base")
            print("2. Habilidades")
            print("3. Moviminetos")
            print("4. Guardar pokemon en txt")

            

            """print("1. Moves")
            print("2. Abilities")
            print("3. Pokémon (including various forms)")
            print("4. Types")
            print("5. Egg Groups")
            print("6. Game Versions")
            print("7. Items")
            print("8. Pokédexes")
            print("9. Pokémon Evolution Chains")"""
            
            print("10. Cambiar pokemon seleccionado" )
            print("11. Salir")

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
               guardarPokemon(pokeSelect.lower(),pokeData)
               input("Pulse cualquier tecla para continuar")
               limpiarConsola()

            elif(opc == "10"):
               break
            
            elif(opc == "11"):
               close = True
               

            else:
               print("Elija una opcion valida...")
               input("Precione cualquier tecla para continuar...")
               limpiarConsola()
      
      
