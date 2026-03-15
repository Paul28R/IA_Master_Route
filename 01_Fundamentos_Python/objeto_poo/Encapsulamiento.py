
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.__sueldo = sueldo #atributo privado

    # Getter para leer el sueldo
    @property
    def sueldo(self):
        return self.__sueldo
    

    # Método para aumentar el sueldo con validación
    def aumentar_sueldo(self, porcentaje):
        if 0 < porcentaje <= 20:
            aumento = self.__sueldo * (porcentaje / 100)
            self.__sueldo += aumento
            print(f"Aumento aplicado. Nuevo sueldo de {self.nombre}: ${self.__sueldo:.2f}")
        else:
            print("Error: El aumento debe ser mayor a 0% y no puede superar el 20%.")

empleado1 = Empleado("Ana", 2000)

# Intentar accede directamente daria un error de atributo
# print(empleado1.__sueldo)


# Acceso correcto via getter
print(f"Sueldo actual de {empleado1.nombre}: ${empleado1.sueldo}")

# Intento de aumento no razonable
empleado1.aumentar_sueldo(50)

# Aumento permitido
empleado1.aumentar_sueldo(10)