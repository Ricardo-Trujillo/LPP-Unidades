#ORTOEDRO

largo = float(input("Largo del ortoedro: "))
ancho = float(input("Ancho del ortoedro: "))
alto = float(input("Alto del ortoedro: "))

area = 2 * ( largo*ancho + largo*alto + ancho*alto)
volumen = largo*ancho*alto

print("El area es: {area:.2f}\nEl volumen es: {volumen:.2f}")