

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def condece(self):
        print("Conduciendo vehiculo generico")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def conduce(self):
        print(f"Conduce un coche marca {self.marca} modelo {self.modelo} de {self.num_puertas} puertas")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo,)
        self.cilindraje = cilindraje

    def conduce(self):
        print(f"Conduce una moto {self.marca} de {self.cilindraje}cc por la carretera.")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, cargamento):
        super().__init__(marca, modelo)
        self.cargamento = cargamento

    def conduce(self):
        print(f"Transportando {self.cargamento} toneladas con el camion {self.marca}")

vehiculos = [Coche("Toyota", "Corolla", 4), Moto("Yamaha", "1600", 689), Camion("Volvo", "f13", 20)]

for v in vehiculos:
    v.conduce()

