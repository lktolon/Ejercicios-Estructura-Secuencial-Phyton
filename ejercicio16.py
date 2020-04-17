v1 = float(input("Velocidad del primer vehículo:"))
v2 = float(input("Velocidad del segundo vehículo):"))
dist = float(input("Distancia entre ambos vehículos:"))

t = dist / abs(v1 - v2)
t = t * 60

print("El primer vehículo alcanzará al segundo en ", tiempo,"minutos.")
