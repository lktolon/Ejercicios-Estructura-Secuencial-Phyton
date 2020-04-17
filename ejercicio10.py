par1 = float(input("Nota del primer parcial:"))
par2 = float(input("Nota del segundo parcial:"))
par3 = float(input("Nota del tercer parcial:"))
ex= float(input("Nota del exámen:"))
trbj = float(input("Nota del trabajo:"))

total = (((par1 + par2 + par3) / 3) * 0.55) + (0.3 * ex) + (0.15 * trbj)

print("La nota final asciende a:", nota)
