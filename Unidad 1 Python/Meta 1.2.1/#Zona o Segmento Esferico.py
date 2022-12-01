#Zona o Segmento Esferico

radio = float(input("Radio de la esfera: "))
radioBase = float(input("Radio de la base del casquete esferico: "))
radioSuperficie = float(input("Radio de la superficie del casquete espferico: "))
altura = float(input("Altura del casquete esferico: "))

area = 2 * 3.1415 * radio * altura
volumen = 3.1415 * altura *( altura**2 +(3 * radioBase**2)+(3* radioSuperficie**2)) / 6

print(f"El area es: {area:.2f}\nEl volumen es: {volumen:.2f}")