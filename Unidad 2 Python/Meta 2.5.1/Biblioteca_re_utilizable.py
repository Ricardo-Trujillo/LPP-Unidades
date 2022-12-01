import miBiblioteca as mp

#cuadrado
a = float(input("Lado del cuadrado: "))
print("El area es :",mp.areaCuadrado(a),"\nEl perimetro es:",mp.perimetroCuadrado(a))

#triangulo
b = float(input("base del triangulo: "))
h = float(input("altura del triangulo: "))
a = float(input("lado a del triangulo: "))
c = float(input("lado c del triangulo: "))

print("El area es :",mp.areaTrinagulo(b,h),"\nEl perimetro es:",mp.perimetroTriangulo(a,b,c))

#Rectangulo

a = float(input("altura del rectangulo: "))
b = float(input("base del rectangulo: "))

print("El area es :",mp.areaRectangulo(b,a),"\nEl perimetro es:",mp.perimetroCuadrilatero(b,a))


#paralelogramo
h = float(input("altura del paralelogramo: "))
b = float(input("base del paralelogramo: "))
a = float(input("lado del paralelogramos: "))

print("El area es :",mp.areaRectangulo(b,h),"\nEl perimetro es:",mp.perimetroCuadrilatero(b,a))

#Rombo
D = float(input("Ditancia D del Rombo: "))
d = float(input("Distancia d del rombo: "))
a = float(input("Lado del rombo: "))

print("El area es :",mp.areaRomboCometa(D,d),"\nEl perimetro es:",mp.perimetroCuadrado(a))

#Cometa
D = float(input("Ditancia D del cometa: "))
d = float(input("Distancia d del cometa: "))
a = float(input("Lado a del cometa: "))
b = float(input("Lado b del cometa: "))


print("El area es :",mp.areaRomboCometa(D,d),"\nEl perimetro es:",mp.perimetroCuadrilatero(b,a))

#trapecio
B = float(input("Base inferior del trapecio: "))
b = float(input("base superior del trapecio: "))
h = float(input("altura del trapecio: "))
a = float(input("Lado a del trapecio: "))
c = float(input("Lado c del trapecio: "))
print("El area es :",mp.areaTrapecio(B,b,h),"\nEl perimetro es:",mp.perimetroTrapecio(B,b,a,c))

#circulo
r = float(input("radio del circulo: "))

print("El area es :",mp.areaCirculo(r),"\nEl perimetro es:",mp.perimetroCirculo(r))

#Poligono Regular
a = float(input("apotena del poligono regular: "))
n = float(input("Numero de lados: "))
b = float(input("Tamaño de los lados: "))
p = mp.perimetroPoligonoRegular(n,b)
print("El area es :",mp.areaPoligonoRegular(a,p),"\nEl perimetro es:",p)

#corona circular
R = float(input("Radio del circulo exterior: "))
r = float(input("radio del circulo interior: "))

print("El area es : ",mp.coronaCircular(R,r))
#Sector circular
r = float(input("radio del circulo: "))
n = float(input("angulo del sector circular n: "))

print("EL area es: ",mp.sectorCircular(r,n))

### segunda seccion

#cubo
a = float(input("lado del cubo: "))
print("El area es: ",mp.areaCubo(a),"\nEl volumen es: ",mp.volumenCubo(a))

#cilindro
r = float(input("Radio del cilindro: "))
h = float(input("Altura del cilindro: "))
print("El area es: ",mp.areaCilindro(r,h),"\nEl volumen es: ",mp.volumenCilindro(r,h))

#ortoedro
a = float(input("Largo del ortoedro: "))
b = float(input("Ancho del ortoedro: "))
c = float(input("Alto del ortoedro: "))
print("El area es: ",mp.areaOrtoedro(a,b,c),"\nEl volumen es: ",mp.volumenOrtoedro(a,b,c))

#Prisma recto
a = float(input("apotena del poligono regular: "))
n = float(input("Numero de lados: "))
b = float(input("Tamaño de los lados: "))
h = float(input("Altura del prisma recto: "))
print("El area del Prisma recto es: ",mp.areaPrimasRecto(h,a,n,b),"\nEl volumen Prisma recto es: ",mp.volumenPrismaRecto(h,a,n,b))

#Cono
r = float(input("radio del cono: "))
h = float(input("Altura del cono: "))
g = float(input("Generatriz del cono: "))
print("El area es: ",mp.areaCono(r,g),"\nEl volumen es: ",mp.volumenCono(r,h))

#Tronco de Cono
r = float(input("radio del circulo superior: "))
R = float(input("radio del circulo inferior: "))
g = float(input("generatriz del cono: "))
h = float(input("Altura del cono: "))
print("El area es: ",mp.areaTroncoCono(g,r,R),"\nEl volumen es: ",mp.volumenTroncoCono(r,R,h))

#Esfera
R = float(input("radio de la esfera: "))
print("El area es: ",mp.areaEsfera(R),"\nEl volumen es: ",mp.volumenEsfera(R))

#Piramide
a = float(input("Apotema de la base: "))
A = float(input("Apotema de la piramide: "))
h = float(input("Altura de la piramide: "))
print("El area es: ",mp.areaPiramide(a,A),"\nEl volumen es: ",mp.volumenPiramide(a,h))

#Tetraedo Regular
a = float(input("Lado del Tetraedro Regular: "))
print("El area es: ",mp.areaTetraedoRegular(a),"\nEl volumen es: ",mp.volumenTetraedoRegular(a))

#Octaedro regular
a = float(input("Lado del Octaedro Regular: "))
print("El area es: ",mp.areaOctraedoRegular(a),"\nEl volumen es: ",mp.volumenOctraedoRegular(a))

#Tronco de Piramide
p =float(input("Perimetro de la primera base: "))
P =float(input("Perimetro de la segunda base: "))
A = float(input("Apotema de la piramide: "))
a =float(input("Area de la primera base: "))
aa=float(input("area de la segunda base: "))
ar = float(input("area de la pared: "))
h = float(input("Altura de la piramide: "))
print("El area es: ",mp.areaTroncoPiramide(p,P,A,ar,a),"\nEl volumen es: ",mp.volumenTroncoPiramide(aa,A,h))

#Casquete Esferico
R = float(input("Radio de  la esfera: "))
h = float(input("Altura del casquete esferico: "))
print("El area es: ",mp.areaCasqueteEsferico(R,h),"\nEl volumen es: ",mp.volumenCasqueteEsferico(R,h))

#Huso: cuna esferica
R = float(input("Radio de  la esfera: "))
n = float(input("Angulo de la Cuña esferica: "))
print("El area es: ",mp.areaCunaEsferica(R,n),"\nEl volumen es: ",mp.volumenCunaEsferica(R,n))

#Zona o Segmento Esferico
R = float(input("radio de la esfera: "))
r = float(input("radio de la base del casquete esferico: "))
ra = float(input("radio de la superficie del casquete espferico"))
h = float(input("altura del casquete esferico: "))
area = 2 * 3.1415 * R * h
volumen = 3.1415 * h *( h**2 +(3 * r**2)+(3* ra**2)) / 6
print("El area es: ",mp.areaSegmentoEsferico(R,h),"\nEl volumen es: ",mp.volumenSegmentoEsferico(r,ra,h))