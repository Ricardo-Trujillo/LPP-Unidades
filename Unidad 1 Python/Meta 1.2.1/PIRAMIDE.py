#PIRAMIDE

apotema = float(input("Apotema de la piramide: "))
apotemaBase = float(input("Apotema de la base: "))
altura = float(input("Altura de la piramide: "))

areaBase= apotemaBase*2 * apotemaBase*2
perimetro = apotemaBase*2 *4
area = perimetro * (apotemaBase + apotema)/2
volumen = areaBase * altura / 3

print(f"El area es: {area:.2f}\nEl volumen es: {volumen:.2f}")