mon2 = int(input("Cantidad de monedas de 2 euros:"))
mon1 = int(input("Cantidad de monedas de 1 euro:"))
mon50 = int(input("Cantidad de monedas de 50 céntimos:"))
mon20 = int(input("Cantidad de monedas de 20 céntimos:"))
mon10 = int(input("Cantidad de monedas de 10 céntimos:"))

euros = (mon2 * 2) + mon1
cent = (mon50 * 50) + (mon20 * 20) + (mon10 * 10)
euros = euros + (cent // 100)
cent = cent % 100

print("El total es de:", euros," euros y", cent," céntimos.")
