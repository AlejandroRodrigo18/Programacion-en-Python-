while True:
    try:
        numero = int(input("Introduce un número entre 1 y 10: "))

        if 1 <= numero <= 10:
            print("Número dentro del rango pedido")
        else:
            print("Numero fuera de rango")
    except ValueError:
        print("El numero no valido.")

    print("Lista de números:")
    for i in range(1, numero + 1):
        print(i)