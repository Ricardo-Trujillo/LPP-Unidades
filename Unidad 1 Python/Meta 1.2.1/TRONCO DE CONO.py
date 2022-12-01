#TRONCO DE CONO

radioSup = float(input("Radio del circulo superior: "))
radioInf = float(input("Radio del circulo inferior: "))
generatriz = float(input("Generatriz del cono: "))
altura = float(input("Altura del cono: "))

area = 3.1415 * (generatriz*(radioSup+radioInf)+radioSup**2+radioInf**2)
volumen =3.1415*altura*(radioSup**2+radioSup**2+radioInf*radioSup) / 3

print(f"El area es: {area:.2f}\nEl volumen es: {volumen:.2f}")