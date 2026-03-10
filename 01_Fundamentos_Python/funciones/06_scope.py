###     SCOPE (ALCANCE)

""" LEGB: Local(L),Enclosing(E),Global(G),Built-in (B) """

# Local 
x = "global" # Global

def function():
    x = "local" # Local (no afecta a la x del afuera)
    print(x)

function() # Imprime local
print(x) # Imprime global

# Type hiting:

def saludar(nombre: str) -> str:
    return f"Hola {nombre}"

# Manejo de errores (try / except):

def calcular_promedio(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        return "La lista esta vacia, no puedo dividir por cero."
    except TypeError:
        return "Entrada invalida, Debe ser una lista de numeros."