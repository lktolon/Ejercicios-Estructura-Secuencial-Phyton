sb = float(input("Valor del sueldo base:"))

v1 = float(input("Valor de la suma de la primera venta:"))
v2 = float(input("Valor de la suma de la segunda venta:"))
v3 = float(input("Valor de la suma de la tercera venta:"))

com = (v1 * 0.1) + (v2 * 0.1)+ (v3 * 0.1)

print("Comisión total:",com)
print("Sueldo total:", sb + com)
