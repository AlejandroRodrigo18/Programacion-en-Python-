import random

random1 = random.randrange(17, 21)

print("El bot ha sacado:", random1)

puntuacion = 0

while True:

    carta = random.randrange(1,5)
    print("Has sacado:", carta)
    puntuacion += carta
    print("Tu puntuacion es: ", puntuacion)

    if puntuacion > 21:
        print("Te has pasado de 21", "tu puntuacion es: ", puntuacion)
        break

    continuar = input("¿Quieres sacar otra carta? (s/n): ")
    if continuar == "n" or continuar == "N":
        break


if puntuacion <= 21:
    if puntuacion > random1:
        print("¡Has ganado! Tu puntuación es mayor que la de la banca.")
    else:
        print("Has perdido. Tu puntuación no supera al bot.")