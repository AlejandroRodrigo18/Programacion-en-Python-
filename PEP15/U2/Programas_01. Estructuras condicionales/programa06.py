from datetime import datetime

dia = int(input("Ingresa un día: "))
mes = int(input("Ingresa un mes: "))
year = int(input("Ingresa un año: "))

if dia < 1 or dia > 31:
    print("El día es inválido")
elif mes < 1 or mes > 12:
    print("El mes es inválido")
else:
    fecha = datetime(year, mes, dia)
    print("La fecha es:", fecha.strftime("%d/%m/%Y"))
