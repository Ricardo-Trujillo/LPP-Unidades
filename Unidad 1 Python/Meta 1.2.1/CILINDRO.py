# CILINDRO
radio = float(input("Radio del cilindro: "))
altura = float(input("Altura del cilindro: "))

area = 2 * 3.1415 * radio *(altura + radio)
volumen = 3.1415* radio**2 * altura

print(f"El area es: {area:.2f}\nEl volumen es: {volumen:.2f}")