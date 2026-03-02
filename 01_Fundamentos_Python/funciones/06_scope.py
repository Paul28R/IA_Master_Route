###     SCOPE (ALCANCE)

""" LEGB: Local(L),Enclosing(E),Global(G),Built-in (B) """

# Local 
x = "global" # Global

def function():
    x = "local" # Local (no afecta a la x del afuera)
    print(x)

function() # Imprime local
print(x) # Imprime global