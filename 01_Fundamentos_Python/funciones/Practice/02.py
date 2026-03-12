# 3 Avancado 

# promedio de notas: crea una funcion que reciba 
# una lista de numero y devuelva su promedio.

mi_lista = [84, 25, 35, 46, 87]

def lista_numeros(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


print(lista_numeros(mi_lista))
print(sum(mi_lista))
print(lista_numeros([85, 90, 79, 92]))

# list_comprehencion

import statistics

def calcular_promedio(lista):
    return statistics.mean(lista) if lista else 0

print(calcular_promedio([85, 90, 79, 92]))

# bucles for para recorrer manuelmente

def calcular_promedio_bucle(lista):
    if not lista:
        return 0
    total = 0
    for l in lista:
        total += l
    return total / len(lista)

# NumPy para bibliotecas muy largas

import numpy as np

notas = [85, 90, 78, 92]
promedio = np.mean(notas)
