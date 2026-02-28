
def puntuacion(alumno1, alumno2, alumno3):
    suma = alumno1 + alumno2 + alumno3
    media =suma / 3 # return suma / 3 
    return media


media = puntuacion(7, 8, 9)
print("La puntuación de esta clase es:", media)

media = puntuacion(3, 5, 6)
print("La puntuación de esta clase es:", media)

# Estructura de datos #

def puntuacion(clase):
    return sum(clase) / len(clase)

clase = [7, 8, 9]
media = puntuacion(clase)
print("La puntuación de esta clase es:", media)

clase = [5, 7, 9, 8, 3]
media = puntuacion(clase)
print("La puntuación de esta clase es:", media)

###

# def mostrar_linea(num, linea):

def mostrar_linea(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


numero = 2
mostrar_linea(7)

###################

# Argumentos

def super_funcion(*args, **kwargs):
    suma = sum(args)
    usuario = kwargs.get("nombre", "Anonimo")
    return f"{usuario}, la suma es {suma}"
print(super_funcion(10, 20, 30, nombre="jose"))

# Funsiones Lambda (Anónimas)

al_cuadrado = lambda x: x**2
print(al_cuadrado(5))





    


