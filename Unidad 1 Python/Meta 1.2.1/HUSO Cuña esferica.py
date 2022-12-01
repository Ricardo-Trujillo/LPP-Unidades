# HUSO Cuña esferica

radio = float(input("Radio de  la esfera: "))
angulo = float(input("Angulo de la Cuña esferica: "))

area = 4 * 3.1415 * radio**2 * angulo / 360
volumen = 4* 3.1415 * (radio**3) * angulo / (3*360)

print(f"El area es: {area:.2f}\nEl volumen es: {volumen:.2f}")