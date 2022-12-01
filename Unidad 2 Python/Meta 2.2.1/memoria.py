
#cartas del memorama
vector = ["rojo","verde","azul","blanco","amarillo","azul","rojo","blanco","amarillo","verde",
          "negro","celeste","turquesa","naranja","cafe","turquesa","naranja","negro","cafe"]
print("Cantidad de cartas = 20 Posicion de 0 a 19")

#primer intento
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0): #cero significa que la carta ya se encontro junto con su par
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i]) #se le dice cual carta encontro   
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i): #no se puede levantar 2 veces la carta de un mismo lugar
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x]) == 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada") #no hizo caso a que no puede levantar la misma carta del mismo lugar    
elif((vector[i]==vector[x] and (x != i))): #verifica si son pares
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")     
#segundo intento
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0):
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i])    
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i):
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x]) == 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada")    
elif((vector[i]==vector[x] and (x != i))):
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")     
#tercer
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0):
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i])    
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i):
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x]) == 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada")    
elif((vector[i]==vector[x] and (x != i))):
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")
#cuarto
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0):
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i])    
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i):
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x]) == 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada")    
elif((vector[i]==vector[x] and (x != i))):
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")
#quinto
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0):
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i])    
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i):
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x]) == 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada")    
elif((vector[i]==vector[x] and (x != i))):
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")
#sexto
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0):
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i])    
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i):
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x]) == 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada")    
elif((vector[i]==vector[x] and (x != i))):
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")
#septimo
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0):
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i])    
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i):
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x]) == 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada")    
elif((vector[i]==vector[x] and (x != i))):
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")
#octavo
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0):
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i])    
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i):
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x])== 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada")    
elif((vector[i]==vector[x] and (x != i))):
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")
#noveno
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0):
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i])    
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i):
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x]) == 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada")    
elif((vector[i]==vector[x] and (x != i))):
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")
#decimo
i = int(input("Ingresa la posicion de la carta 1: "))
if(vector[i]== 0):
    print("carta no disponible")
else:    
     print("Levantaste la carta ",vector[i])    
x = int(input("Ingresa la posicion de la carta 2: "))
if(vector[x]== 0):
    print("carta no disponible")
else:
    if(x==i):
        print("no se puede levantar la misma carta")
    else:    
        print("Levantaste la carta ",vector[x])    
if((vector[i] or vector[x])== 0): #si se vuelven a buscar las cartas ya encontradas
    print("cartas ya encontradas")
elif(x==i):
    print("misma carta levantada")    
elif((vector[i]==vector[x] and (x != i))):
    print("Encontraste el par",vector[i])
    vector[i] = 0
    vector[x] = 0
else:
    print("No son Pares")

print("se termino el juego")
