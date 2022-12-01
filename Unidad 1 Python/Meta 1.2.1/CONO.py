#CONO

radio = float(input("Radio del cono: "))
altura = float(input("Altura del cono: "))
generatriz = float(input("Generatriz del cono: "))

area = 3.1415 * radio * (radio + generatriz)
volumen = 3.1415 * radio**2 * altura / 3

print(f"El area es: {area:.2f}\nEl volumen es: {volumen:.2f}")