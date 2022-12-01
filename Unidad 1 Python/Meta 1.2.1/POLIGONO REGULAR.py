# POLIGONO REGULAR
apotema = float(input("Apotema del poligono regular: "))
numLados = float(input("Numero de lados: "))
sizeLados = float(input("Tamaño de los lados: "))

perimetro = numLados * sizeLados
area = perimetro * apotema / 2

print(f"El area es : {area:.2f}\nEl perimetro es: {perimetro:.2f}")