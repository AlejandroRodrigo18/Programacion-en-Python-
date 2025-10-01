
nota = float(input("Ingrese la nota: "))

ra1 = round(nota * 0.80, 2)
ra2 = round(nota * 0.40,2)
ra3 = round(nota * 0.80,2)

notaFinal = ra1+ra2+ra3

print("La nota original es:", nota)
print("La nota en el RA1 es:", ra1)
print("La nota en el RA2 es:", ra2)
print("La nota en el RA3 es:", ra3)
print("La nota final es:", notaFinal)