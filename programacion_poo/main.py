# Programa principal - Programación Orientada a Objetos
# Se importa la clase Mascota desde mascota.py

from mascota import Mascota

# Crear objeto 1
mascota1 = Mascota("Toby", "perro", 3)

# Crear objeto 2
mascota2 = Mascota("Luna", "gato", 5)

# Mostrar información y sonido de cada mascota
mascota1.mostrar_informacion()
mascota1.hacer_sonido()

mascota2.mostrar_informacion()
mascota2.hacer_sonido()