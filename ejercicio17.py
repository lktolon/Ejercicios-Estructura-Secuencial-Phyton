horainicial = int(input("Hora de salida:"))
mininicial = int(input("Minutos de salida:"))
seginicial = int(input("Segundos de salida:"))

total = int(input("Tiempo total del viaje en segundos:"))

totalinicial = (horainicial * 3600) + (mininicial * 60) + seginicial;

final = totalinicial + total;

horafinal = total // 3600;
minfinal = (total % 3600) // 60;
segfinal = (total % 3600) % 60;

print("Hora de llegada", horafinal,":",minfinal,":",segfinal)

