class Persona:
    def __init__(self, nombre=' ', edad=0, sexo=' ', estatura=0):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.estatura = estatura

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):

        self.nombre = nombre
    def getEdad(self):

        return self.edad
    def setEdad(self, edad):

        self.edad = edad
    def getSexo(self):

        return self.sexo
    def setSexo(self, sexo):
        self.sexo = sexo

    def getEstatura(self):
        return self.estatura

    def setEstatura(self, estatura):
        self.estatura = estatura

class Facultad:
    def __init__(self, nombre='', carrera=0):
        self.nombre = nombre
        self.carrera = carrera

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCarrera(self):
        return self.carrera

    def setCarrera(self, carrera):
        self.carrera = carrera
class Materia:
    def __init__(self, nombreMateria='', id=0):
        self.nombreMateria = nombreMateria
        self.id = id

    def getNombreMateria(self):
        return self.nombreMateria

    def setNombreMateria(self, nombreMateria):
        self.nombreMateria = nombreMateria

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

class Materias:
    def __init__(self, nombre, id):
        self.materias = Materia(nombre, id)

    def getMaterias(self):
        return self.materias

    def setMaterias(self, materias):
        self.materias = materias
class Alumno(Persona):
    def __init__(self, nombre=''):
        Persona.__init__(self, nombre)
        self.matricula = 0
        self.facultad = Facultad()
        self.materias = []

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getFacultad(self):
        return self.facultad

    def setFacultad(self, facultad):
        self.facultad = facultad

    def getMaterias(self):
        return self.materias

    def addMateria(self, nombre, id):
        self.materias.append(Materia(nombre, id))
class Trabajador(Persona):
    def __init__(self, nombre='', edad=0, sex='', estatura=0):
        Persona.__init__(self,nombre,edad,sex,estatura)
        self.numTrabajador = 0
        self.salario = 0
        self.antiguedad = 0
    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario = salario

    def getAntiguedad(self):
        return self.antiguedad

    def setAntiguedad(self, antiguedad):
        self.antiguedad = antiguedad

class Profesor(Trabajador):
    def __init__(self, nombre=''):
        Trabajador.__init__(self, nombre)
        self.facultad = Facultad()
    def getFacultad(self):
        return self.facultad
    def setFacultad(self, facultad):
        self.facultad = facultad
    def getNumTrabajador(self):
        return self.numTrabajador
    def setNumTrabajador(self, numero):
        self.numTrabajador = numero
    def getFacultad(self):
        return self.facultad
    def setFacultad(self, facultad):
        self.facultad = facultad

class Universidad:
    def __init__(self, nombre):
        self.nombre
        self.facultades = []
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getFacultades(self):
        return self.facultades

    def addFacultad(self, nombre, carrera):
        self.facultades.append(Facultad(nombre, carrera))