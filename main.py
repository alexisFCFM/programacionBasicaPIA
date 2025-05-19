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
               print(f"1. Mostrar estadisticas de {pokeSelect}")
               print(f"2. Mostrar movimientos de {pokeSelect}")
               print(f"3. Sacar promedio de las estadisticas de {pokeSelect}")
               print(f"4. Sacar mediana de las estadisticas de {pokeSelect}")
               print(f"5. Sacar moda de las estadisticas de {pokeSelect}")
               print(f"6. Sacar la desviación estándar de las estadisticas de {pokeSelect}")
               print("7. Exportar todas las estadisticas de todos los pokemon registrados")



               print("")
               print("10. Cambiar pokemon seleccionado" )
               print("11. Salir")

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
                  print("")
                  print(f"El promedio de las estadisticas de {pokeSelect} es de {sacarMedia(pokeSelect)}")
                  print("")
                  input("Pulse cualquier tecla para continuar")
                  limpiarConsola()

               elif(opc == "4"):
                   print("")
                   print(f"La mediana de las estadisticas de {pokeSelect} es {sacarMediana(pokeSelect)}")  
                   print("")
                   input("Pulse cualquier tecla para continuar")
                   limpiarConsola()

               elif(opc == "5"):
                   print("")
                   print(f"La moda de las estadisticas de {pokeSelect} es {sacarModa(pokeSelect)}")  
                   print("")
                   input("Pulse cualquier tecla para continuar")
                   limpiarConsola()

               elif(opc == "6"):
                   print("")
                   print(f"La desviación estándar de las estadisticas de {pokeSelect} es {sacarDerivacionEstandar(pokeSelect)}")  
                   print("")
                   input("Pulse cualquier tecla para continuar")
                   limpiarConsola()

               elif(opc == "7"):
                  print("")
                  exportarExel(pokeSelect)
                  print("")
                  input("Pulse cualquier tecla para continuar")
                  limpiarConsola()


               elif(opc == "10"):
                  limpiarConsola()
                  break
            
               elif(opc == "11"):
                  close = True
               

               else:
                  print("Elija una opcion valida...")
                  input("Precione cualquier tecla para continuar...")
                  limpiarConsola()     

    else:
        input("Ingrese un nombre valido...")
        limpiarConsola()
        
       
    
    
      
      
