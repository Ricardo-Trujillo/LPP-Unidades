# TRIANGULO
base = float(input("Base del triangulo: "))
altura = float(input("Altura del triangulo: "))
ladoA = float(input("Lado A del triangulo: "))
ladoC = float(input("Lado C del triangulo: "))
area = (base * altura) / 2
perimetro = ladoA + base + ladoC
print(f"El area es: {area:.2f}\nEl perimetro es: {perimetro:.2f}")