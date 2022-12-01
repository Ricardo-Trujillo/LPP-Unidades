morse = {"a":"*-","b":"-***","c":"-*-*","d":"-**","e":"*","f":"**-*","g":"--*","h":"****","i":"**","j":"*---","k":"-*-","l":"*-**","m":"--","n":"-*",
         "o":"---","p":"*--*","q":"--*-","r":"*-*","s":"***","t":"-","u":"**-","v":"***-","w":"*--","x":"-**-","y":"-*--","z":"--**",
          "1":"*----","2":"**---","3":"***--","4":"****-","5":"*****","6":"-****","7":"--***","8":"---**","9":"----*","0":"-----"," ":"/","/":" "}
caracteres = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","/")
lenguaje =("*","-","/")
f = True
j=0
while(f):     #comprueba que no se ingresen letras y solo sea un codigo morse no comprueba que ese codigo sea correcto
    cad  = input("Ingresa tu cadena: ")
    for i in cad:
      try:
        if(lenguaje.index(i)>=0): 
          j = j  + 1    
          if(j == len(cad)):
            if(cad[j-1]=='/'): #verifica que tenga el simbolo de terminacion de caracter /
              f = False
            else:
              j=0
              print("debe terminar en /")   
      except:
        j=0
        print("No {} pertenece al lenguaje: ",i)
        print("caracteres permitidos:  ** -- //")        
        break
res = ""
aux =""
cont = 0
for c in cad:
   if(c!="/"):
     aux = aux + c
   else:
     if(c == "/"):
       cont = cont +1
     for k in caracteres:
       if(cont ==2):
         res= res + " "
         cont = 0  
       if(morse.get(k)== aux):
         cont = 0
         res= res + k
         aux =""
print(res)         