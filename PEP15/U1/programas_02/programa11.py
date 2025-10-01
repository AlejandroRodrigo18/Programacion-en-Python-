print("Introduce la hora de salida:")
HH = int(input("Horas (HH): "))
MM = int(input("Minutos (MM): "))
SS = int(input("Segundos (SS): "))

N = int(input("Duración del viaje en segundos: "))

total_salida = HH * 3600 + MM * 60 + SS

total_llegada = total_salida + N

hora = (total_llegada // 3600) % 24
minuto = (total_llegada % 3600) // 60
segundo = total_llegada % 60

print("Hora de llegada a la ciudad B: {:02d}:{:02d}:{:02d}".format(hora, minuto, segundo))
