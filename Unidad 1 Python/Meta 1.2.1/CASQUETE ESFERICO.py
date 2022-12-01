#CASQUETE ESFERICO

radio = float(input("Radio de  la esfera: "))
altura = float(input("Altura del casquete esferico: "))

area = 2* 3.1415 * radio * altura
volumen = 3.1415 * altura**2 * (3*radio - altura) / 3

print(f"El area es: {area:.2f}\nEl volumen es: {volumen:.2f}")