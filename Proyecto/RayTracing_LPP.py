from PIL import Image
import numpy as np

objetos = []
epsilon = 1e-3
z_min = 200
z_max = 1000
posicion_luz = [500, 500, 500]
componente_ambiente = 0.05
color_ambiente = [255, 255, 255]
prundidad_max = 2


class Plano:

    def __init__(self, punto, normal, color, k_difuso, k_reflejo):
        self.normal = convertir_unidad_vector(normal)
        self.punto = punto
        self.color = color
        self.k_difuso = k_difuso
        self.k_reflejo = k_reflejo

    def getNormal(self, puntoSuperficie):
        return self.normal


class Esfera:

    def __init__(self, centro, radios, color, k_difuso, k_reflejo):
        self.centro = centro
        self.radios = radios
        self.color = color
        self.k_difuso = k_difuso
        self.k_reflejo = k_reflejo

    def getNormal(self, puntoSuperficie):
        return np.subtract(puntoSuperficie, self.centro) / self.radios


class Ray:

    def __init__(self, punto, dir):
        self.punto = punto
        self.dir = dir


def toma_de_entrada():
    print("Tomando entradas desde: entrada.txt")
    file = open("entrada.txt", "r")
    numeroEsferas = int(file.readline())

    #Añade esferas al objeto
    for i in range(numeroEsferas):
        color = [int(x) for x in file.readline().split(",")]
        centro = [int(x) for x in file.readline().split(",")]
        radios = int(file.readline())
        k_difuso = float(file.readline())
        k_reflejo = float(file.readline())
        esfera = Esfera(centro, radios, color, k_difuso, k_reflejo)
        objetos.append(esfera)

    numeroPlanos = int(file.readline()) #Añade planos al objeto.
    
    for i in range(numeroPlanos):
        color = [int(x) for x in file.readline().split(",")]
        punto = [int(x) for x in file.readline().split(",")]
        normal = [int(x) for x in file.readline().split(",")]
        k_difuso = float(file.readline())
        k_reflejo = float(file.readline())

        plano = Plano(punto, normal, color, k_difuso, k_reflejo)
        objetos.append(plano)

    print("Entrada exitosa!!!")


def encontrar_interseccion_plano(ray, plano):
    direccionNormalRayo = np.dot(plano.normal, ray.dir)
    if np.abs(direccionNormalRayo) < epsilon:
        return None  #No hubo interseccion
    t = np.dot(convertir_unidad_vector(plano.normal), (np.subtract(plano.punto, ray.punto))) / np.dot(ray.dir, plano.normal)
    return t if t > epsilon else None


def encontrar_interseccion_esfera(ray, esfera):
    distancia = np.subtract(ray.punto, esfera.centro)
    a = np.dot(ray.dir, ray.dir)
    b = 2 * np.dot(distancia, ray.dir)
    c = np.dot(distancia, distancia) - esfera.radios ** 2
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return None, None
    elif delta == 0:
        punto = - b / (2 * a)
        return punto, None
    else:
        t1 = (-b - np.sqrt(delta)) / (2 * a)
        t2 = (-b + np.sqrt(delta)) / (2 * a)
        return t1, t2  # t2>t1


def es_visible(t_para_comprobar, t_max, ray):
    z_punto = ray.punto[2] + t_para_comprobar * ray.dir[2]  #2 = z
    return epsilon < t_para_comprobar < t_max and z_min < z_punto < z_max


def encontrar_objeto_cercano(ray):
    mas_cercano = [99999999, None]  # indice 0 = t , indice 1 = objeto

    for objeto in objetos:
        if type(objeto) is Esfera:
            t1, t2 = encontrar_interseccion_esfera(ray, objeto)

            if t1 is None:
                pass
            elif es_visible(t1, mas_cercano[0], ray):
                mas_cercano = [t1, objeto]
            elif es_visible(t2, mas_cercano[0], ray):
                mas_cercano = [t2, objeto]

        elif type(objeto) is Plano:
            t = encontrar_interseccion_plano(ray, objeto)
            if t is None:
                pass
            elif es_visible(t, mas_cercano[0], ray):
                mas_cercano = [t, objeto]

    return mas_cercano  # return the object and t


def convertir_unidad_vector(vector):
    magnitud = np.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    return np.divide(vector, magnitud)


def reflejo_ray(ray, plano_normal, punto):
    nueva_dir = ray.dir - 2 * (np.dot(ray.dir, plano_normal)) * plano_normal
    nueva_dir = convertir_unidad_vector(nueva_dir)

    return Ray(punto + epsilon * plano_normal, nueva_dir)


def rayo_fundido(ray, profundidad):
    #Encuentra objetos por colisiones de luz
    color = [0, 0, 0]
    interseccion = encontrar_objeto_cercano(ray)  # index 0 = t , index 1 = object
    if interseccion[1] is not None and profundidad < prundidad_max:
        #Verifica si hay sombra con un raoy de luz por debajo
        punto_interseccion = ray.punto + np.multiply(ray.dir, interseccion[0])
        direccion_luz = np.subtract(posicion_luz, punto_interseccion)
        unidad_direccion_luz = convertir_unidad_vector(direccion_luz)
        rayo_luz = Ray(punto_interseccion, unidad_direccion_luz)
        interseccion_luz = encontrar_objeto_cercano(rayo_luz)

        luz = 1
        if type(interseccion_luz[1]) is Esfera and interseccion_luz[1] != interseccion[1]:
            luz = 0

        ambiente_col = np.multiply(color_ambiente, componente_ambiente, np.divide(interseccion[1].color, 256))
        unidad_normal = convertir_unidad_vector(interseccion[1].getNormal(punto_interseccion))
        difuso_col = np.multiply(interseccion[1].k_difuso * max(0, np.dot(unidad_direccion_luz, unidad_normal)),
                                  interseccion[1].color)

        nuevo_rayo = reflejo_ray(ray, interseccion[1].getNormal(punto_interseccion), punto_interseccion)
        color = ambiente_col + difuso_col * luz
        color += np.multiply(interseccion[1].k_reflejo, rayo_fundido(nuevo_rayo, profundidad + 1)) / (profundidad + 1)

    return color


def generar_pixel_color(x, y):
    pixel_x = -49.95 + x * 0.1
    pixel_y = (999 - y) * 0.1 - 49.95
    pixel_z = 100

    dir = [pixel_x, pixel_y, pixel_z]
    punto_de_vista = [0, 0, 0]
    profundidad = 0
    rayo_inicial = Ray(punto_de_vista, dir)
    color = rayo_fundido(rayo_inicial, profundidad)

    return color


def generar_imagen():
    print("Calculando imagen...")
    image = np.zeros((1000, 1000, 3))

    for x in range(1000):
        for y in range(1000):
            color = generar_pixel_color(x, y)

            image[y][x][0] = int(min(color[0], 255))
            image[y][x][1] = int(min(color[1], 255))
            image[y][x][2] = int(min(color[2], 255))

    print("Calculo de la imagen listo.")

    return image


def print_imagen(image):
    print("Generando Imagen...")
    im = Image.fromarray(image.astype('uint8'))
    im.save('output.png')
    print("Imagen generada.")


def main():
    toma_de_entrada()
    image = generar_imagen()
    print_imagen(image)


if __name__ == "__main__":
    main()