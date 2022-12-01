def areaCuadrado(lado=0):
    area = lado * lado
    return area

def perimetroCuadrado(lado=0):
    perimetro = lado * 4
    return perimetro

def areaTrinagulo(base,altura):
    return (base*altura) /2

def perimetroTriangulo(ladoA,ladoB,ladoC):
    return ladoA+ladoB+ladoC

def areaRectangulo(base,altura):
    return base*altura

def perimetroCuadrilatero(base,altura): #figuras cuadrilateras
    return 2*(base+altura)

def areaRomboCometa(D,d):
    return (D*d)/2

def areaTrapecio(B,b,h):
    return (B + b) * h / 2

def perimetroTrapecio(B,b,a,c):
    return B + b + a + c

def areaCirculo(radio):
    return 3.141516 * radio**2

def perimetroCirculo(radio):
    return 2*3.141516 * radio

def areaPoligonoRegular(apotema,perimetro):
    return perimetro * apotema / 2

def perimetroPoligonoRegular(n,b):
    return n * b

def coronaCircular(R,r):
    return 3.141516 * ( R**2 - r**2)

def sectorCircular(r,n):
    return 3.141516 * r**2 * n /360

def areaCubo(lado):
    return 6 * lado**2

def volumenCubo(lado):
    return lado**3

def areaCilindro(radio,altura):
    return 2 * 3.1415 * radio *(altura + radio)

def volumenCilindro(radio,altura):
    return 3.1415* radio**2 * altura

def areaOrtoedro(largo,ancho,alto):
    return 2 * ( largo*ancho + largo*alto + ancho*alto)

def volumenOrtoedro(largo,ancho,alto):
    return largo*ancho*alto

def areaPrimasRecto(altura,apotema,nLados,ntamano):
    return perimetroPoligonoRegular(nLados,ntamano) * (altura + apotema)

def volumenPrismaRecto(altura,apotema,nLados,ntamano):
    ab= perimetroPoligonoRegular(nLados,ntamano) * apotema / 2
    return ab * altura

def areaCono(radio,generatriz):
    return 3.1415 * radio * (radio + generatriz)

def volumenCono(radio,altura):
    return 3.1415 * radio**2 * altura / 3

def areaTroncoCono(genratriz,radioSuperior,radioInferior):
    return 3.1415 * (genratriz*(radioSuperior+radioInferior)+radioSuperior**2+radioInferior**2)

def volumenTroncoCono(radioSuperior,radioInferior,altura):
    return 3.1415*altura*(radioSuperior**2+radioSuperior**2+radioInferior*radioSuperior) / 3

def areaEsfera(radio):
    return 4 * areaCirculo(radio)

def volumenEsfera(radio):
    return 4 * 3.1415 * radio**3 / 3

def areaPiramide(apotenmaB,apotemaP):
    P = apotenmaB*2 *4
    return  P * (apotenmaB + apotemaP)/2  

def volumenPiramide(apotemaB,altura):
    Ab = apotemaB*2 * apotemaB*2
    return  Ab * altura / 3

def areaTetraedoRegular(lado):
    return lado**2 * 3**.5

def volumenTetraedoRegular(lado):
    return 2**.5 * lado**3 /12    

def areaOctraedoRegular(lado):
    return 2 * lado**2 * 3**.5

def volumenOctraedoRegular(lado):
    return 2**.5 * lado**3 /3    

def areaTroncoPiramide(perimetroB,perimetroSB,apotemaP,areaPared,areaPB):
    return ((perimetroB+perimetroSB)/2) * areaPared + areaPB + apotemaP

def volumenTroncoPiramide(areaPB,apotemaP,altura):
    return (areaPB + apotemaP + (areaPB*apotemaP)**.5) * altura / 2

def areaCasqueteEsferico(radio,altura):
    return 2* 3.1415 * radio * altura

def volumenCasqueteEsferico(radio,altura):
    return 3.1415 * altura**2 * (3*radio - altura) / 3    

def areaCunaEsferica(radio,angulo):
    return 4 * 3.1415 * radio**2 * angulo /360

def volumenCunaEsferica(radio,angulo):
    return 4* 3.1415 * (radio**3) * angulo / (3*360)

def areaSegmentoEsferico(radioEsfera,alturaCasquete):
    return 2 * 3.1415 * radioEsfera * alturaCasquete

def volumenSegmentoEsferico(radioCasquete,radioSuperficie,altura):
    return 3.1415 * altura *( altura**2 +(3 * radioCasquete**2)+(3* radioSuperficie**2)) / 6
