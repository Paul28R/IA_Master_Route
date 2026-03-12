# funciones

# 

def operacion(num1,num2, tipo="suma"):
    if tipo == "suma":
        return num1 + num2
    elif tipo == "resta":
        return num1 - num2
    elif tipo == "div":
        return num1 / num2
    elif tipo == "mult":
        return num1 * num2
    
print(operacion(2, 7, "resta"))



def operacion(num1,num2, tipo="suma"):
    operaciones = {"resta": num1 - num2, "div": num1 / num2, 
                   "mult": num1 * num2 if num2 != 0 else
                     "Error: Division por cero"}
    return operaciones.get(tipo, "Operacion no valida")

print(operacion(2, 7, "div"))

####################################

import string

def contar_letras(texto):
    # convertir a minuscula
    texto = texto.lower()
    # (str.translate) esto quita comas, puntos, signos de interrogacion, etc.
    texto = texto.translate(str.maketrans('','', string.punctuation))
    # Dividir el texto en palabras (por espacios en blanco)
    palabras = texto.split()
    # crea el diccionario de frecuencias
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    return frecuencia_palabras

texto_largo = "Podrías intentar usar .replace(), " \
"pero tendrías que escribir una línea para el punto, " \
"otra para la coma, otra para el signo de exclamación, " \
"y así sucesivamente. Con la combinación de maketrans y " \
"translate, lo haces todo de golpe."

print(contar_letras(texto_largo))

##############################################

import string
# 1. Obtener el texto del diccionario kwargs
def El_contador_de_text(**kmargs):
    # usamos .get() para evitar errores si no pasan la llave "texto"
    texto = kmargs.get("texto", "")
    if not texto:
        return "no hay texto para procesar"
# 2. Limpieza minusculas y quitar puntuacion
    texto_limpio = texto.lower().translate(str.maketrans('','', string.punctuation))
# 3. separar palabras 
    palabras = texto_limpio.split()
# 4. conteo de frecuencias
    frecuencias = {}
    for p in palabras:
        frecuencias[p] = frecuencias.get(p, 0) + 1
    return frecuencias

# ---Ahora lo ponemos a funcionar--- #

resultado = El_contador_de_text(texto="todo lo que agregues aqui aqui tiene que que que contarse (pull)")
print(resultado)


### Funsion mas corta con (Counter) de la libreria estardar de python:
from collections import Counter

def Contado_corto(**kwargs):
    texto = kwargs.get("texto","").lower().translate(str.maketrans('','', string.punctuation))
# Esto hace todo el trabajo de contar por ti
    return dict(Counter(texto.split()))

resultado = Contado_corto(texto="Espero este (si) sí que funsione bien bien")
print(resultado)

####################################

# lambda
numeros = [1, 5, 8, 12, 15, 20, 21]
division = list(filter(lambda x: x % 3 == 0, numeros))
print(division)
     
## Devision segura

def dev_segura(num1, num2):
    try:
        return num1 / num2 
    except ZeroDivisionError:
        return "no se puede dividir por 0"
    
print(dev_segura(10, 2))
print(dev_segura(10, 0))

def dividir(a, b):
    if b == 0:
        return "No se puede diviir por cero"
    return a / b

print(dividir(10, 2))
print(dividir(10, 0))


# otra practica
def limpia_lista_python(datos: list) -> list:
    
    def es_convertible(x):
        try:
            float(x)
            return True
        except:
            return None

celsius = 25 
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} C equivalen a {int(fahrenheit)} F")


# celsius = float(input("Ingresa los grados celsius:"))
# fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} a {fahrenheit}")

#########################

def convertir_a_fahrenheit(c):
    return (c * 9/5) + 32

print(convertir_a_fahrenheit(200))

######################

def es_par(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False
    

print(es_par(3))

#####################

def mayor_sin_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(mayor_sin_max(10,5,8))
print(mayor_sin_max(15,25, 20))
print(mayor_sin_max(3, 3, 1))











