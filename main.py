from utilities import *

close = False

cargarPokemon()
    
while(close != True):
    print("PokeApi")
    pokeSelect = input("Ingrese el pokemon que desea consultar: ").lower()

    if(re.fullmatch(verificacionNombre, pokeSelect)):
       respuesta = requests.get(apiUrl + pokeSelect.lower())
       if(respuesta.status_code != 200):
         print("Ingrese un valor valido...")
         input("Pulse cualquier tecla para continuar")
         limpiarConsola()
    
       else:
            pokeJson = respuesta.json()
            descargarPokemon(pokeSelect.lower(),pokeJson)

            while(close != True):
               limpiarConsola()
               print(f"Pokedex de {pokeSelect}\n")

               print(f"Nombre de pokemon: {pokemonDicc[pokeSelect]['nombre']}")
               print(f"Numero de pokedex: {pokemonDicc[pokeSelect]['id']}")
               print(f"Tipos: {pokemonDicc[pokeSelect]['tipos']}")
               print(f"Habilidades: {pokemonDicc[pokeSelect]['habilidades']}")
               print(f"Altura: {pokemonDicc[pokeSelect]['altura']}m")
               print(f"Peso: {pokemonDicc[pokeSelect]['peso']}kg")

               print("\nMas opciones:")
               print("1. Mostrar estadisticas")
               print("2. Mostrar movimientos")
               print("3. Guardar pokemon ya buscadoes en txt")       
               print("4. Cambiar pokemon seleccionado" )
               print("5. Salir")

               opc = input("Ingrese el numero de la opcion que desee consultar: ")

               if(opc == "1"):
                  print("")
                  Estadisticas(pokeSelect)
                  print("")
                  input("Pulse cualquier tecla para continuar")
                  limpiarConsola()

               elif(opc == "2"):
                  print("")
                  Movimientos(pokeSelect)
                  print("")
                  input("Pulse cualquier tecla para continuar")
                  limpiarConsola()

               elif(opc == "3"):
                  nombreUsuario = input("Seleccione un nombre para su archivo txt: ")
               
                  with open(nombreUsuario +'.txt', 'w', encoding='utf-8') as archivo:
                     json.dump(pokemonDicc, archivo, ensure_ascii=False, indent=4)
              
                  print("Archivo exportado")
                  input("Pulse cualquier tecla para continuar")
                  limpiarConsola()

               elif(opc == "4"):
                  limpiarConsola()
                  break
            
               elif(opc == "5"):
                  close = True
               

               else:
                  print("Elija una opcion valida...")
                  input("Precione cualquier tecla para continuar...")
                  limpiarConsola()     

    else:
        input("Ingrese un nombre valido...")
        limpiarConsola()
        
       
    
    
      
      
