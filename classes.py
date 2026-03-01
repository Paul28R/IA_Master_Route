# no necesito esto

class person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# Esto es un metodo.
    def walk(self):
        print(f"{self.name} {self.surname} está caminando")

# uso:
my_person =person("Paul", "Rodriguez")
my_person.walk() # Imprime: Paul Roxriguez esta caminando

print(my_person)