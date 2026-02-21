import sys
# sys.argv: Una lista que python crea automanticamente. contiene todos los
# "argumentos" (palabras) que escribiste en la terminal al lanzar el script.
if len(sys.argv) > 1: # > 1 : porque el primer elemento siempre es (sys.argv)[0]
# si la posicion anterior es verdadera tomamos el valor de la posicion 1
# (el primer dato despues del nombre del archivo) 
    name = sys.argv[1] # y se guarda en la variable name
# imprime el saludo usando una f-string. inserta la variable(name)dentro del texto
    print(f"Hello, {name}!")
# opcion b
else:
    print("Hello, there!")