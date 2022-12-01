from io import open
# Captura del alumno y su matricula
alumno = input("Ingresa el nombre del alumno: \n")
matricula = input("Ingresa la matricula del alumno: \n")

# Abre un archivo para agregarle nueva información.
# El puntero se coloca al final del archivo. Se crea un nuevo archivo si no existe uno con el mismo nombre
miArchivo = open("MIArchivo.txt","a")
alumno = alumno + " " + matricula + " " "\n" # nombre,espacio,matricula,espacio,salto de linea
miArchivo.write(alumno)
miArchivo.close()

miArchivo= open("MIArchivo.txt")
miTexto = miArchivo.readlines()
miArchivo.close()

print(miTexto)