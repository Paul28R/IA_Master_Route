# Revertir texto

def invertir_cadena(texto):
    return texto[::-1]

print(invertir_cadena("python"))

###########

def invertir_cadena(texto):
    invertida = ""
    for caracter in texto:
        invertida = caracter + invertida
    return invertida

print(invertir_cadena("python2")) 

## contador de vocales


def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vocales:
            contador += 1

    return contador

palabra_usuario = input("Ingresa una palabra: ")
resultado = contar_vocales(palabra_usuario)
print(f"la palabra {palabra_usuario} tiene {resultado} vocales.")

##########

def contar_vocales(palabra):
    # suma 1 por cada letra que sea una vocal (incluyendo tildes y dieresis)
    return sum(1 for letra in palabra.lower() if letra in 'aeiouAEIOU')

usuario = input("Escribe algo: ")
print(f"Total de vocales: {contar_vocales(usuario)}")