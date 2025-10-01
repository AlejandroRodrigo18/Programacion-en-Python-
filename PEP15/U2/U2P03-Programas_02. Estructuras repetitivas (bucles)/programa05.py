numero = int(input("Introduce un número: "))
contador = 1

while contador <= numero:
    if numero > 10 or numero < 1:
        print("Numero invalido")
        break

    print(contador, end=" ")
    contador += 1
