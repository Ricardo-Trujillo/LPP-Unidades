def triangulo(n):
    if(n == 0):
        return n
    return n + triangulo(n-1)

x = int(input("ingresa el valor: "))
print(triangulo(x))