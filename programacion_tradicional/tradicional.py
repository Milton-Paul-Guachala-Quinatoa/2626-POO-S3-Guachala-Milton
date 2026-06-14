# Programa 1: Programación Tradicional
# Sistema de gestión de mascotas sin clases ni objetos

def registrar_mascota():
    """Solicita los datos de una mascota por teclado"""
    print("\n--- Registrar Mascota ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (perro, gato, etc.): ")
    edad = int(input("Ingrese la edad de la mascota: "))
    return nombre, especie, edad

def mostrar_mascota(nombre, especie, edad):
    """Muestra la información de una mascota de forma organizada"""
    print("\n--- Información de la Mascota ---")
    print(f"Nombre  : {nombre}")
    print(f"Especie : {especie}")
    print(f"Edad    : {edad} años")
    print("---------------------------------")

# Programa principal
nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)