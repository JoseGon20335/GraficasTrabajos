from ast import Try
from collections import namedtuple
import numpy
import struct

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


def bbox(A, B, C):
    xs = [A.x, B.x, C.x]
    xs.sort()
    ys = [A.y, B.y, C.y]
    ys.sort()
    return xs[0], xs[-1], ys[0], ys[-1]


def barycentric(A, B, C, P):
    resul = cross(
        V3(B.x - A.x, C.x - A.x, A.x - P.x),
        V3(B.y - A.y, C.y - A.y, A.y - P.y)
    )

    if abs(resul[2]) > 1:
        return (
            1 - (resul[0] + resul[1]) / resul[2],
            resul[1] / resul[2],
            resul[0] / resul[2]
        )
    elif(abs(resul[2]) > 1):
        return -1, -1, -1
    else:
        return 0, 0, 0


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
    return bytes([int(b), int(g), int(r)])


def createBmp(width, height, pixels):
    filename = "result.bmp"
    f = open(filename, 'bw')

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

    for x in range(width):
        for y in range(height):
            f.write(pixels[x][y])
