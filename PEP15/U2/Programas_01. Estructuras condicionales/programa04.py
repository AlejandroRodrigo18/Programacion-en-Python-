numero = int(input("Ingresa un número (0 al 10): "))

if numero < 0 or numero > 10:
    print("Número introducido fuera del rango establecido. Saliendo del programa.")
else:
    match numero:
        case 0 | 1 | 2 | 3 | 4:
            print("Nota Insuficiente:", numero)
        case 5:
            print("Nota Suficiente:", numero)
        case 6:
            print("Nota Bien:", numero)
        case 7 | 8:
            print("Nota Notable:", numero)
        case 9 | 10:
            print("Nota Sobresaliente:", numero)
