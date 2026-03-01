# youtube

# 1. Definicion de la CLASE (el molde)
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

# Gemini

# 1. Definicion de la CLASE (el molde)
class Coche:
    # El constructor (__init__) inicializa el objeto
    def __init__(self, marca, color):
        # ATRIBUTOS (Estado)
        self.marca = marca
        self.color = color
        self.__velocidad = 0 # The double underscore makes it private (Encapsulation)
    
    # METODOS (comportamiento)
    def acelerar(self):
        self.__velocidad += 10
        print(f"El coche {self.marca} acelera. Velocidad actual: {self.__velocidad} km/h")
    
    def obtener_velocidad(self):
        return self.__velocidad
    
# 2. Creacion de OBJETOS (Instancias)
mi_coche = Coche("Ford", "Rojo")
tu_coche = Coche("Toyota", "Azul")

# 3. Uso de los objetos
print(f"Micoche es un {mi_coche.marca} de color {mi_coche.color}")
mi_coche.acelerar()
mi_coche.acelerar()
mi_coche.acelerar()

# print(mi_coche.__velocidad) # esto daria error, esta encapsulado
print(f"Velocidad final: {mi_coche.obtener_velocidad()} km/h")

    