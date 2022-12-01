#PRISMA RECTO

apotema = float(input("Apotema del poligono regular: "))
numLados = float(input("Numero de lados: "))
sizeLados = float(input("Tamaño de los lados: "))
altura = float(input("Altura del prisma recto: "))

perimetro = numLados * sizeLados
areaBase = perimetro * apotema / 2
area = perimetro * ( altura + apotema)
volumen = areaBase * altura

print(f"El area del Prisma recto es: {area:.2f}\nEl volumen Prisma recto es: {volumen:.2f}")