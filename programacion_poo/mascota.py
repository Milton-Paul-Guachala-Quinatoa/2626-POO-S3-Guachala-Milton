# Clase Mascota - Programación Orientada a Objetos

class Mascota:

    def __init__(self, nombre, especie, edad):
        # Atributos de la mascota
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        # Muestra la información básica de la mascota
        print("\n--- Información de la Mascota ---")
        print(f"Nombre  : {self.nombre}")
        print(f"Especie : {self.especie}")
        print(f"Edad    : {self.edad} años")
        print("---------------------------------")

    def hacer_sonido(self):
        # Simula el sonido según la especie
        if self.especie.lower() == "perro":
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif self.especie.lower() == "gato":
            print(f"{self.nombre} dice: ¡Miau miau!")
        else:
            print(f"{self.nombre} dice: ...")