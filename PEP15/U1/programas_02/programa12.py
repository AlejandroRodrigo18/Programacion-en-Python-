
milla = int(input("Ingrese la cantidad milla: "))

km = int(input("Ingrese la cantidad kmil: "))

kmilToMilla = round(milla * 1.609344, 2)

millaToKm = round (km / 1.609344,2)

print("La milla introducida", milla, "en km es:", kmilToMilla)
print("El km introducido", km, "en millas es:", millaToKm)