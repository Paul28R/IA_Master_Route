

# class Personaje:
#     def __init__(self, nombre, vida=100, ataque=1000):
#         self.nombre = nombre
#         self.vida = vida
#         self.ataque = ataque
        
#         self.atacar 



class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        # Metodo
    def atacar(self, objetivo):
        # Le restamos la vida al otro objetivo
        objetivo.vida -= self.ataque # objetivo.vida = objetivo.vida - self.ataque
        if objetivo.vida <= 0:
            print("El enemigo ha sido derrotado!")
        else:
            print(f"{self.nombre} ha atacado a {objetivo.nombre}")

            print(f"A {objetivo.nombre} le quedan {objetivo.vida} puntos de vida.")


jugador = Personaje("Pythoru", vida=100, ataque=52)

Enemigo = Personaje("Bot malvado", vida=50, ataque=5)

jugador.atacar(Enemigo)
        