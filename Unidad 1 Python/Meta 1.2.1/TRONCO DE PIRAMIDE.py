# TRONCO DE PIRAMIDE

perimetro1 = float(input("Perimetro de la primera base: "))
perimetro2 = float(input("Perimetro de la segunda base: "))

area1 = float(input("Area de la primera base: "))
area2= float(input("area de la segunda base: "))

areaPared = float(input("area de la pared: "))
altura = float(input("Altura de la piramide: "))

area = ((perimetro1+perimetro2)/2) * areaPared + area1 + area2
volumen = ((area1 + area2 + (area1*area2)**.5) * altura )/ 3

print(f"El area es: {area:.2f}\nEl volumen es: {volumen:.2f}")