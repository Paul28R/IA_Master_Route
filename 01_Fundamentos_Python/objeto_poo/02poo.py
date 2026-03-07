# 1. nivel Basico

### 1. 1. Nivel Básico: Clases y Atributos 
# Crea una clase llamada Libro. 
# Atributos: titulo, autor y paginas.
# Método: mostrar_info que imprima: "El libro [titulo] de [autor] tiene [paginas] páginas."
# Práctica: Instancia dos objetos diferentes de esta clase y llama a su método. 

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        return f"El libro {self.titulo} de {self.autor} tiene {self.paginas} páginas."
    
libro1 = Libro("Vamurta", "Leon David", 500)
libro2 = Libro("Quouft", "quijones", 832) 

print(libro1.mostrar_info())
print(libro2.mostrar_info())

### 1. 2. Nivel Intermedio: Métodos y Lógica
# Diseña una clase CuentaBancaria. 
# Atributos: titular y saldo (inicializado en 0).
# Métodos:
# depositar(cantidad): Suma el monto al saldo.
# retirar(cantidad): Resta el monto solo si hay saldo suficiente; si no, muestra un error.
# ver_saldo(): Muestra el estado actual de la cuenta.

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.saldo = saldo
        self.titutar = titular

    def depositar(self, monto):
        self.saldo += monto
        print("deposito completado", monto) 
        

    def retirar(self, monto):
        
        if monto <= self.saldo:
            self.saldo -= monto
            print("Retiro completado", monto)
        else:
            print("No se completo, Saldo insuficiente")     
                
    def ver_saldo(self):
        return f"Uste tiene {self.saldo} en fondo"

mi_cuenta = CuentaBancaria("paul", 0)

mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.retirar(1000)

print(mi_cuenta.ver_saldo())

### 1. 3. Nivel Avanzado: Herencia y Polimorfismo
# Crea un sistema de gestión de empleados. 
# Clase Base: Empleado con atributos nombre y sueldo_base.
# Clase Hija 1: Vendedor que añade una comision. Su método calcular_sueldo debe sumar base + comisión. 
# Clase Hija 2: Gerente que añade un bono. Su método calcular_sueldo debe sumar base + bono.
# Práctica: Crea una lista con un vendedor y un gerente, y recorre la lista llamando al método calcular_sueldo de cada uno (Polimorfismo).

