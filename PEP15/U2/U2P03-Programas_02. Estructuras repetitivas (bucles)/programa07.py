numero = int(input("Elige numero (1 para break, 2 sin break): "))
contador = 0

match numero:
    case 1:

        while numero != 0:
            numero = int(input("Ingresa un numero: "))
            contador += numero
            if numero == 0:
                print("La suma de todos los números es: ", contador)
                break


    case 2:

        while numero != 0:

            numero = int(input("Ingresa un numero: "))

            contador += numero

            if numero == 0:
                print("La suma de todos los números es: ", contador)
