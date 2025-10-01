numero_par = int(input("Introduce un número PAR (positivo o negativo): "))

numero_impar = int(input("Introduce un número IMPAR (positivo o negativo): "))

if numero_par % 2 != 0 and numero_impar % 2 == 0:
    print("Ninguno de los dos números es correcto.")
elif numero_par % 2 != 0:
    print("El primer número no es par.")
elif numero_impar % 2 == 0:
    print("El segundo número no es impar.")
else:
    print("¡Ambos números son correctos!")
