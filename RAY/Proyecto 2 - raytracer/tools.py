from ast import Try
from collections import namedtuple
import numpy
import struct
from math import *

V2 = namedtuple('Point2D', ['x', 'y'])
V3 = namedtuple('Point3D', ['x', 'y', 'z'])
V4 = namedtuple('Point4D', ['x', 'y', 'z', 'w'])

# -------------------------------------------------------------
# OP
# -------------------------------------------------------------


class V3(object):
    def __init__(self, x, y=None, z=None):
        if (type(x) == numpy.matrix):
            self.x, self.y, self.z = x.tolist()[0]
        else:
            self.x = x
            self.y = y
            self.z = z

    def norm(self):
        l = (self.x**2 + self.y**2 + self.z**2)**0.5
        return V3(self.x/l, self.y/l, self.z/l)

    def __repr__(self):
        return "V3(%s, %s, %s)" % (self.x, self.y, self.z)

    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __mul__(self, other):
        if(type(other) == int or type(other) == float):
            return V3(
                self.x * other,
                self.y * other,
                self.z * other
            )
        else:
            return V3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x,
            )

    def __add__(self, other):
        return V3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return V3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )


class V2(object):
    def __init__(self, x, y=None):
        if (type(x) == numpy.matrix):
            self.x, self.y = x.tolist()[0]
        else:
            self.x = x
            self.y = y

    def __repr__(self):
        return "V2(%s, %s)" % (self.x, self.y)


def sum(v0, v1):
    return V3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)


def sub(v0, v1):
    return V3(
        v0.x - v1.x,
        v0.y - v1.y,
        v0.z - v1.z
    )


def mul(v0, k):
    return V3(v0.x * k, v0.y * k, v0.z * k)


def dot(v0, v1):
    return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z


def cross(v0, v1):
    cx = v0.y * v1.z - v0.z * v1.y
    cy = v0.z * v1.x - v0.x * v1.z
    cz = v0.x * v1.y - v0.y * v1.x
    return V3(cx, cy, cz)


def length(v0):
    return (v0.x**2 + v0.y**2 + v0.z**2)**0.5


def norm(v0):
    l = length(v0)

    if l == 0:
        return V3(0, 0, 0)

    return V3(
        v0.x/l,
        v0.y/l,
        v0.z/l
    )


def bbox(*vertices):
    xs = [vertex.x for vertex in vertices]
    ys = [vertex.y for vertex in vertices]
    xs.sort()
    ys.sort()

    return V2(int(xs[0]), int(ys[0])), V2(int(xs[-1]), int(ys[-1]))


def barycentric(A, B, C, P):
    resul = cross(
        V3(B.x - A.x, C.x - A.x, A.x - P.x),
        V3(B.y - A.y, C.y - A.y, A.y - P.y)
    )

    if abs(resul.z) < 1:
        return (-1, -1, -1)

    return (
        1 - (resul.x + resul.y) / resul.z,
        resul.y / resul.z,
        resul.x / resul.z
    )


def allbarycentric(A, B, C, bbox_min, bbox_max):
    barytransform = numpy.linalg.inv(
        [[A.x, B.x, C.x], [A.y, B.y, C.y], [1, 1, 1]])
    grid = numpy.mgrid[bbox_min.x:bbox_max.x,
                       bbox_min.y:bbox_max.y].reshape(2, -1)
    grid = numpy.vstack((grid, numpy.ones((1, grid.shape[1]))))
    barycoords = numpy.dot(barytransform, grid)
    # barycoords = barycoords[:,numpy.all(barycoords>=0, axis=0)]
    barycoords = numpy.transpose(barycoords)
    return barycoords


def char(c):
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    return struct.pack('=h', w)


def dword(d):
    return struct.pack('=l', d)


def color(r, g, b):
    return bytes([b, g, r])


def createBmp(width, height, pixels):
    f = open('result.bmp', 'bw')

    f.write(char('B'))
    f.write(char('M'))
    f.write(dword(14 + 40 + width * height * 3))
    f.write(dword(0))
    f.write(dword(14 + 40))

    f.write(dword(40))
    f.write(dword(width))
    f.write(dword(height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(width * height * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    for x in range(height):
        for y in range(width):
            f.write(pixels[x][y].toBytes())
    f.close()


class Intersect:
    def __init__(self, distance, point, normal):
        self.distance = distance
        self.point = point
        self.normal = normal


class Material:
    def __init__(self, diffuse, albedo, spec):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec


class Light:
    def __init__(self, position, intensity, color):
        self.position = position
        self.intensity = intensity
        self.color = color


def reflect(I, N):
    return (norm(I - N * 2 * dot(I, N)))


class color(object):
    def __init__(this, r, g, b) -> None:
        this.r = r
        this.g = g
        this.b = b

    def __add__(this, other):
        return color(
            this.r + other.r,
            this.g + other.g,
            this.b + other.b
        )

    def __mul__(this, other):
        if type(other) is color:
            return color(
                this.r * other.r,
                this.g * other.g,
                this.b * other.b
            )
        else:
            return color(
                this.r * other,
                this.g * other,
                this.b * other
            )

    def toBytes(this) -> bytes:
        if this.b > 255:
            this.b = 255
        if this.g > 255:
            this.g = 255
        if this.r > 255:
            this.r = 255

        if this.b < 0:
            this.b = 0
        if this.g < 0:
            this.g = 0
        if this.r < 0:
            this.r = 0

        return bytes([int(this.b), int(this.g), int(this.r)])


class Envmap(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        with open(self.path, "rb") as image:
            image.seek(2 + 4 + 4)
            header_size = struct.unpack("=l", image.read(4))[0]
            image.seek(2 + 4 + 4 + 4 + 4)

            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size)

            self.pixels = [
                [bytes([0, 0, 0]) for y in range(self.height)]
                for x in range(self.width)
            ]

            for y in reversed(range(self.height)):
                self.pixels.append([])
                for x in reversed(range(self.width)):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))

                    c = color(r, g, b)

                    try:
                        self.pixels[y][x] = c
                    except:
                        pass

    def get_color(self, direction):
        direction = norm(direction)

        x = min((atan2(direction.z, direction.x) / (2 * pi) + 0.5)*2, 1)
        y = min((acos(-direction.y) / pi)*2, 1)

        x = int(x * self.width)
        y = int(y * self.height)

        if (x > 0):
            x -= 1
        else:
            0

        if (y > 0):
            y -= 1
        else:
            y = 0

        return self.pixels[y][x]


def refract(I, N, roi):
    eta_i = 1
    eta_t = roi

    # Coseno i para calcular la refracción.
    cos_i = (dot(I, N) * -1)

    # Recálculo de valores si el coseno i es negativo.
    if (cos_i < 0):
        cos_i *= -1
        eta_i *= -1
        eta_t *= -1
        N = mul(N, -1)

    # Valor eta, resultante de la división de las dos componentes.
    eta = (eta_i / eta_t)

    # Simplificación de la expresión a un valor k para luego obtener su raíz cuadrada.
    k = (1 - ((eta ** 2) * (1 - (cos_i ** 2))))

    # Retorno de un vector nulo si el valor k es negativo.
    if (k < 0):
        return V3(0, 0, 0)

    # Cálculo del coseno t con la raíz cuadrada del valor k.
    cos_t = (k ** 0.5)

    # Retorno del nuevo vector refractado.
    return norm(sum(mul(I, eta), mul(N, ((eta * cos_i) - cos_t))))
