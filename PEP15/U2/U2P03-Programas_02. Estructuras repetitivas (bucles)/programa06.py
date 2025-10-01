numero = int(input("Introduce un número del 1 al 10: "))

while numero < 1 or numero > 10:
    print("Número inválido")
    numero = int(input("Introduce un número del 1 al 10: "))

for i in range(1, 11):
    resultado = numero * i
    print(resultado)

repetir = int(input("¿Quieres repetir tirada? (1 sí, 2 no): "))

if repetir == 1:
    numero = int(input("Introduce un número del 1 al 10: "))
    while numero < 1 or numero > 10:
        print("Número inválido")
        numero = int(input("Introduce un número del 1 al 10: "))
    for i in range(1, 11):
        resultado = numero * i
        print(resultado)
else:
    print("Gracias por jugar")
