
cadenaEncontrar = "Aleister, the invoker"
cadenaAux = cadenaEncontrar
cadenaRes =""
bandera = 0
flag =0
cont = 0
j=0
cont2 = 0
print(len(cadenaEncontrar))
while(not bandera):
    c = input("Ingresa una letra: ")
    for i in cadenaEncontrar:
        if(c==i):
            print("letra encontrada")
            flag = not flag
            cadenaRes = ""
            cadenaEncontrar= cadenaEncontrar.replace(c," ")
            break 
    if(flag):    
        for cad in cadenaEncontrar:
            if(cad == " "):
                cadenaRes = cadenaRes + cadenaAux[j]
            else:
                cadenaRes = cadenaRes + " "    
            j =j+1    
        j=0
    print("La subacadena encontrada es: ",cadenaRes)    
   # print(cadenaRes)      
    if(not flag):
        cont = cont + 1
        print(" te quedan", 6 - cont,"oportunidades")
    else:
        flag = not flag     
    if(cont>=6):
        bandera = not bandera
        print("perdiste")        
    for i in cadenaEncontrar:
        l = len(cadenaEncontrar)
        if(i ==' '):
            cont2 = cont2 +1
            if(cont2 == len(cadenaEncontrar)):
                break
        else:
            cont2=0               
    if(cont2 == len(cadenaEncontrar) ):
        print("Ganaste")
        bandera = not bandera                    
