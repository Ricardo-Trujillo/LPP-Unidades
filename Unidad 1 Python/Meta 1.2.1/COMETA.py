# COMETA
distanciaD = float(input("Ditancia D del cometa: "))
distancia_d = float(input("Distancia d del cometa: "))
ladoA = float(input("Lado A del rombo: "))
ladoB = float(input("Lado B del rombo: "))

area = distanciaD * distancia_d / 2
perimetro = 2*( ladoB + ladoA)

print(f"El area es: {area:.2f}\nEl perimetro es: {perimetro:.2f}")