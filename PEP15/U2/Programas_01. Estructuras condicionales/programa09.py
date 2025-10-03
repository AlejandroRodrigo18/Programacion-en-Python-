
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
print("Selecciona una opción")

jugador1 = int(input("Jugador 1, elige tu opción (1-3): "))
jugador2 = int(input("Jugador 2, elige tu opción (1-3): "))


if jugador1 > 3 or jugador2 > 3:
    print("No se puede elegir esa opcion")

elif jugador1 == 1 and jugador2 == 2:
    print("El jugador 2 ha ganado")
elif jugador1 == 2 and jugador2 == 3:
    print("El jugador 2 ha ganado")
elif jugador1 == 3 and jugador2 == 1:
    print("El jugador 2 ha ganado")
elif jugador1 == 3 and jugador2 == 2:
    print("El jugador 1 ha ganado")
elif jugador1 == 1 and jugador2 == 3:
    print("El jugador 1 ha ganado")
elif jugador1 == 2 and jugador2 == 3:
    print("El jugador 1 ha ganado")
else:
    print("Se ha producido un empate")