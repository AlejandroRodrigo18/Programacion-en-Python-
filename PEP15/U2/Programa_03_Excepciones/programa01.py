contador = 0
try:
    while True:
        numero = int(input("Introduce un número entre 1 y 10: "))

        if 1 <= numero <= 10:
            print("Número añadido correctamente")
            contador += 1
        else:
            print("Numero fuera de rango")
except ValueError:
    print("El numero no valido.")
    print("Has introducido: ", contador, "numeros")
