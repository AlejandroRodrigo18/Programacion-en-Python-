def entrada(nombre, apellido1, apellido2):
    return f"{nombre} {apellido1} {apellido2}"


nombre = input("Escribe tu nombre: ")
apellido1 = input("Escribe tu primer apellido: ")
apellido2 = input("Escribe tu segundo apellido: ")


print("¡Hola!", entrada(nombre, apellido1, apellido2))
