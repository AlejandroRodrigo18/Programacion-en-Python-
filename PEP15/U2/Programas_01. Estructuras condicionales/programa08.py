import random

jugador1 = random.randrange(1,7)
jugador2 = random.randrange(1,7)

puntuacion1 = jugador1 + jugador1
puntuacion2 = jugador2 + jugador2

print("El jugador 1", puntuacion1)
print("El jugador 2", puntuacion2)

if puntuacion1 > puntuacion2:
    print("El jugador 1 ha ganado la partida: ", puntuacion1)
elif puntuacion1 < puntuacion2:
    print("El jugador 2 ha ganado la partida: ", puntuacion2)
else:
    print("Las puntuaciones es igual, por tanto es un empate")
