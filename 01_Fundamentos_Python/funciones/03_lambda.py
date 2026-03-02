# lambda 
al_cuadrado = lambda x: x**2
print(al_cuadrado(5))

sumar = lambda a, b: a + b
print(sumar(10,10)) # Salida: 8
# Map
nums = [1, 2, 3, 4, 5]
al_cuadrado = list(map(lambda x: x**2, nums))
print(al_cuadrado)
# Filter
pares = list(filter(lambda x: x % 2==0, nums))
print(pares)
# Sorted()
estudiante = [("maria", 25),("luis",20)]
estudiantes_ordenados = sorted(estudiante, key=lambda x: x[1])
print(estudiantes_ordenados)


"""                      Evita su uso

si la lógica requiere bucles (for, while), múltiples pasos
o manejo de errores (try-except) es mejor una función 'def' """




