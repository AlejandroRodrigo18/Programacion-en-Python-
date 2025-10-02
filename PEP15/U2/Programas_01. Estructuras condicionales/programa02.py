numero = int(input("Ingresa un número par (positivo o negativo): "))

if numero % 2 != 0:
    print("Error: El número ingresado no es par. Saliendo del programa...")
else:
    print("Número par introducido correctamente...", numero)

    numero2 = int(input("Ingresa ahora un número impar (positivo o negativo): "))

    if numero2 % 2 == 0:
        print("Error: El número ingresado no es impar. Saliendo del programa...", numero2)
    else:
        print("Número impar introducido correctamente...")
