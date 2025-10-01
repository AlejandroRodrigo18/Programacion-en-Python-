
minutos = int(input("Introduce minutos:\n"))

minutoHora= minutos/60

minutoRestantes = int(minutos % 60)

print("El minuto introducido es:", minutos)
print("Cambio de Minuto a Hora introducido es :", minutoHora , "horas")
print("Los minutos restantes son:", minutoRestantes ,"minutos")

##print("En total", minutos, "minutos es en Horas y minutos", minutoHora, "", minutoRestantes)