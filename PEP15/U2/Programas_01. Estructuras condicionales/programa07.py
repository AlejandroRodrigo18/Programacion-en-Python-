
year = int(input("Ingresa un año: "))

bisiesto = year % 4 == 0 and year % 100 !=0 or year %  400 ==0

if bisiesto is True:
    print("El año",year ,"introducido es bisiesto")
else:
    print("El año",year ,"introducido no es bisiesto")

