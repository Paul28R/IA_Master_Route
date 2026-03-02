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
numero = [1, 5, 8,12, 15, 21]

multiplos_de_3 = list(filter(lambda n: n % 3 == 0 , numero))
print(multiplos_de_3)
     



