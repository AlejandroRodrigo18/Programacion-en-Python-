import random

random1 = random.randrange(17, 21)
print("La banca ha sacado:", random1)

num_jugadores = int(input("¿Cuántos jugadores van a jugar?: "))

for jugador in range(1, num_jugadores + 1):
    print(f"\n Turno del jugador {jugador}")
    puntuacion = 0

    while True:
        carta = random.randrange(1, 5)
        print("Has sacado:", carta)
        puntuacion += carta
        print("Tu puntuación es:", puntuacion)

        if puntuacion > 21:
            print("❌ Te has pasado de 21. Tu puntuación es:", puntuacion)
            break

        continuar = input("¿Quieres sacar otra carta? (s/n): ")
        if continuar.lower() == "n":
            break

    if puntuacion <= 21:
        if puntuacion > random1:
            print("¡Has ganado! Tu puntuación es mayor que la de la banca.")
        else:
            print("Has perdido. Tu puntuación no supera a la banca.")
