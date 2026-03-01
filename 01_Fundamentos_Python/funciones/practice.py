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

# def El_contador_de_text(**kmargs):


 


