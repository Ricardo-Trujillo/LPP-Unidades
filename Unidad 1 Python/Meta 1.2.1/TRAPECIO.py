# TRAPECIO

baseInf = float(input("Base inferior del trapecio: "))
baseSup = float(input("Base superior del trapecio: "))
altura = float(input("Altura del trapecio: "))
ladoA = float(input("Lado lado A del trapecio: "))
ladoC = float(input("Lado lado C del trapecio: "))
area = (baseInf + baseSup) * altura / 2
perimetro = baseInf + baseSup + ladoA + ladoC
print(f"El area es: {area:.2f}\nEl perimetro es: {perimetro:.2f}")