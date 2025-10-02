dividendo = int(input("Introduce un dividendo "))
divisor = int(input("Introduce el divisor: "))


if divisor != 0:

    resultado = dividendo / divisor

    print("El resultado de la división entre", dividendo, "y"
          , divisor, "es: ", resultado)

else:
    print("Error. No se puede dividir entre cero")
