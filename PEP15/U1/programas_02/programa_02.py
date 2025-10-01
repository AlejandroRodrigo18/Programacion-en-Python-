
entero = 6

#Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto
#al que apunta la variable (deben ser iguales)

print("La variable", entero, "es de tipo:",type(entero))

#Cree otra variable a la que se asigne la primera variable.

enteroSustituto = entero

"""
Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto
al que apunta la variable (deben ser iguales)
"""

print("La variable", enteroSustituto, "es lo mismo que", entero, "por tanto debe de devolver un entero" ,type(enteroSustituto))

print("")
print("Utilizando variables de IS and IS NOT")
print("Resultando usando IS:", entero is enteroSustituto)
print("Resultando usando IS NOT:",entero is not enteroSustituto)

print("")

valor_anterior= entero

entero = "Hola"

print("La variable", entero, "es de tipo:",type(entero))

print("El primer valor que tiene la variable entero es un int ",isinstance(enteroSustituto,int))

print("El segundo valor que tiene la variable entero es str", isinstance(entero,str))

