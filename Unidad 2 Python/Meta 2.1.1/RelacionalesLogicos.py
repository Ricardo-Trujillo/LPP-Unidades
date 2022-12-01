#haga un programa en python que pregunte al usuario el valor a=10 y b =5,
#y luego evalue si las siguientes expresiones son verdadero o falso

a = int(input("Dame el valor de a:"))
b = int(input("Dame el valor de b:"))
resultado = (((3+5*8)<3) and ((-6/3*4)+2<2)) or (a>b)
#print(((3+5*8)<3)) = false
#print(((-6/3*4)+2<2))True
print(resultado) #((false AND TRUE) or ? )

a = int(input("Dame el valor de a:"))
b = int(input("Dame el valor de b:"))
#print(((2+5*7)>3)) True
#print(((-5/7*5)+2>2)) false 
resultado = ((((2+5*7)>3) or ((-5/7*5)+2>2)) and (a<b))
print(resultado) #(True or False) and ?

a = int(input("Dame el valor de a:"))
b = int(input("Dame el valor de b:"))
#print(((4+5*6)<=3)) false
#print(((-4/6*6)+2<=2)) true
resultado = (((4+5*6)<=3) or not ((-4/6*6)+2<=2)) or (a>=b)
print(resultado) #false or not(true) or ?

a = int(input("Dame el valor de a:"))
b = int(input("Dame el valor de b:"))
#print((6-5*5)>=3) false
#print(((-3/5*7)+2>=2)) false
resultado = ((6-5*5)>=3 and ((-3/5*7)+2>=2)) or not (a<=b) #(false and false) or not ?
print(resultado)

a = int(input("Dame el valor de a:"))
b = int(input("Dame el valor de b:"))
#print((8-5*4)<3) true
#print(((-2/4*8)+2<2)) true
resultado = ((8-5*4)<3 and ((-2/4*8)+2<2)) and (a==b) #true and true and ?
print(resultado)

a = int(input("Dame el valor de a:"))
b = int(input("Dame el valor de b:"))
#print((3-5*3)>3) false
#print(((-1/3*9)+2>2)) false
resultado = ((3-5*3)>3 or ((-1/3*9)+2>2)) or (a!=b) #false or false or ?
print(resultado)