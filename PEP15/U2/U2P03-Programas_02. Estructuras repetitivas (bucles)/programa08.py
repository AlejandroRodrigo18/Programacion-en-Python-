import random

random1 = random.randrange(1, 21)

numero = int(input("Introduce un numero: "))

while True:
    if numero < random1:
        print("El número ", numero, "es menor al numero generado" )
        numero = int(input("Introduce de nuevo un número: "))

    elif numero > random1:
        print("El número ", numero, "es mayor al numero generado" )
        numero = int(input("Introduce de nuevo un número: "))
    else:
        print("¡Has acertado!", "El número generado de manera aleatrio es:", random1)
        break


