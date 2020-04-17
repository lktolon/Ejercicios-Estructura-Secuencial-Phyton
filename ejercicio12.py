import math

print("Coordenadas del primer número:")
x1 = int(input())
y1 = int(input())

print("Coordenadas del segundo número:")
x2 = int(input())
y2 = int(input())

distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print("La distancia entre los puntos:",distancia)
