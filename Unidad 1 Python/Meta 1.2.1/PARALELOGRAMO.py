# PARALELOGRAMO

altura = float(input("Altura del paralelogramo: "))
base = float(input("Base del paralelogramo: "))
ladoP = float(input("Lado del paralelogramos: "))
area = base * altura
perimetro = 2 * (base + ladoP)
print(f"El area es : {area:.2f}\nEl perimetro es: {perimetro:.2f}")