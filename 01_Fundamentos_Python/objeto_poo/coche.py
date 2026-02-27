
class Coche: 
        # Metodo (Dunder) Double underscore
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
    
    def arrancar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "se ha arrancado")

    def parar(self):
        self.arrancado = False
        print("El", self.marca, self.modelo, "se ha parado")

laguna = Coche("Renault", "Laguna")
tesla = Coche("Tesla", "Model 3")

print(type(laguna))
print(type(tesla))

print(laguna.marca, laguna.modelo)
print(tesla.marca, tesla.modelo)
# una vez que arranca el arrancado es True
laguna.arrancar()
tesla.arrancar()

print(laguna.arrancado)
print(tesla.arrancado)
# una vez que se para el arrancado es false
laguna.parar()
tesla.parar()

print(laguna.arrancado)
print(tesla.arrancado)