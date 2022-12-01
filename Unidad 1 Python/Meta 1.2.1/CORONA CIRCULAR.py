#CORONA CIRCULAR

radioExterior = float(input("Radio del circulo exterior: "))
radioInterior = float(input("radio del circulo interior: "))

area = 3.141516 * ( radioExterior**2 - radioInterior**2)

print(f"El area es: {area:.2f}")