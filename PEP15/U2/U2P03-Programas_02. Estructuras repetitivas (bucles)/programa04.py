numero_secreto = 45


option = int(input("Elige numero (1 para bucle infinito, 2 para bucle funcional): "))

match option:
    case 1:
        numero = int(input("Introduce un número: "))
        while numero != numero_secreto:
            print("Número indicado no es el de salida. Introduce otro número")
            # No se actualiza 'numero' por tanto es un bucle infinito a propósito

        # Este bloque nunca se alcanza
        if numero == numero_secreto:
            print("¡Has dejado el bucle con éxito!", numero)

    case 2:
        numero = int(input("Introduce un número: "))
        while numero != numero_secreto:
            print("Número indicado no es el de salida. Introduce otro número")
            numero = int(input("Introduce un número: "))  # Aquí sí se actualiza
        print("¡Has dejado el bucle con éxito!")
