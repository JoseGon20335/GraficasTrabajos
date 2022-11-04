from ast import Try
from utils import *
from obj import Obj
from collections import namedtuple
from matrix import *
from numpy import sin, cos, matrix

V2 = namedtuple('Point2D', ['x', 'y'])
V3 = namedtuple('Point3D', ['x', 'y', 'z'])
V4 = namedtuple('Point4D', ['x', 'y', 'z', 'w'])

# -------------------------------------------------------------
# OP
# -------------------------------------------------------------


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


# -------------------------------------------------------------
# START RENDER
# -------------------------------------------------------------


class Renderer(object):

    def glInit(self):
        self.color = color(250, 250, 250)
        self.clean_color = color(0, 0, 0)

        self.filename = 'modelo.bmp'

        self.pixels = [[]]
        self.pixelsZBuffer = [[]]
        self.light = V3(0, 0, 1)

        self.width = 0
        self.height = 0
        self.OffsetX = 0
        self.OffsetY = 0
        self.ImageHeight = 0
        self.ImageWidth = 0

    def glLoad(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0), texture=None):
        model = Obj(filename)
        self.loadMatrix(translate, scale, rotate)

        light = V3(0, 0, 1)

        for face in model.faces:
            vcount = len(face)

            if vcount == 3:
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1
                a = self.transform(model.vertices[f1])
                b = self.transform(model.vertices[f2])
                c = self.transform(model.vertices[f3])

                normal = norm(cross(sub(b, a), sub(c, a)))
                intensity = dot(normal, light)

                if not texture:
                    grey = round(255 * intensity)
                    if grey < 0:
                        continue
                    self.triangle(a, b, c, color=color(grey, grey, grey))
                else:
                    t1 = face[0][1] - 1
                    t2 = face[1][1] - 1
                    t3 = face[2][1] - 1
                    tA = V3(*model.tvertices[t1])
                    tB = V3(*model.tvertices[t2])
                    tC = V3(*model.tvertices[t3])

                    self.triangle(a, b, c, texture=texture, texture_coords=(
                        tA, tB, tC), intensity=intensity)
            else:
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1
                f4 = face[3][0] - 1

                vertices = [
                    self.transform(model.vertices[f1]),
                    self.transform(model.vertices[f2]),
                    self.transform(model.vertices[f3]),
                    self.transform(model.vertices[f4])
                ]

                normal = norm(cross(sub(vertices[0], vertices[1]), sub(
                    vertices[1], vertices[2])))
                intensity = dot(normal, light)
                grey = round(255 * intensity)

                A, B, C, D = vertices

                if not texture:
                    grey = round(255 * intensity)
                    if grey < 0:
                        continue
                    self.triangle(A, B, C, color(grey, grey, grey))
                    self.triangle(A, C, D, color(grey, grey, grey))
                else:
                    t1 = face[0][1] - 1
                    t2 = face[1][1] - 1
                    t3 = face[2][1] - 1
                    t4 = face[3][1] - 1
                    tA = V3(*model.tvertices[t1])
                    tB = V3(*model.tvertices[t2])
                    tC = V3(*model.tvertices[t3])
                    tD = V3(*model.tvertices[t4])

                    self.triangle(A, B, C, texture=texture, texture_coords=(
                        tA, tB, tC), intensity=intensity)
                    self.triangle(A, C, D, texture=texture, texture_coords=(
                        tA, tC, tD), intensity=intensity)

    def glCreateWindow(self, width, height):
        # if (width < 0) or (height < 0):
        #     raise Exception('unexpected windows size')

        self.width = width
        self.height = height

        self.glClear()

    def glViewPort(self, x, y, width, height):
        if (width > self.width) or (height > self.height):
            raise Exception('Viewport larger than window')

        self.OffsetX = int(x)
        self.OffsetY = int(y)

        self.ImageWidth = int(width)
        self.ImageHeight = int(height)

    def glVertex(self, x, y):
        if not (-1 <= x <= 1) or not (-1 <= y <= 1):
            raise Exception('unexpected vertex offset')

        x = int((x+1)*(self.ImageWidth/2)+self.OffsetX)
        y = int((y+1)*(self.ImageHeight/2)+self.OffsetY)

        self.pixels[y-1][x-1] = self.current_color  # AQUI CUIDADO

    def glClear(self):
        self.pixels = [
            [self.clean_color for x in range(self.width)]
            for y in range(self.height)
        ]
        self.pixelsZBuffer = [
            [-99999 for x in range(self.width)]
            for y in range(self.height)
        ]

    def glClearColor(self, r, g, b):
        if not (0 <= r <= 1) or not (0 <= g <= 1) or not (0 <= b <= 1):
            raise Exception('unexpected color value')

        self.clean_color = color(int(r * 255), int(g * 255), int(b * 255))

    def glColor(self, r, g, b):
        if not (0 <= r <= 1) or not (0 <= g <= 1) or not (0 <= b <= 1):
            raise Exception('unexpected color value')

        self.current_color = color(int(r * 255), int(g * 255), int(b * 255))

    def glFinish(self):
        f = open(self.filename, 'bw')

        f.write(char('B'))

        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        for x in range(self.width):
            for y in range(self.height):
                f.write(self.pixels[x][y])

    def glPoint(self, x, y):
        if not (-1 <= x <= 1) or not (-1 <= y <= 1):
            raise Exception('unexpected value')

        self.glVertex(x, y)

    def glLine(self, x0, y0, x1, y1):

        ImgH = self.ImageHeight/2
        ImgW = self.ImageWidth/2

        x0 = int((x0+1)*(ImgW)+self.OffsetX)
        x1 = int((x1+1)*(ImgW)+self.OffsetX)
        y0 = int((y0+1)*(ImgH)+self.OffsetY)
        y1 = int((y1+1)*(ImgH)+self.OffsetY)

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

            dy = abs(y1 - y0)
            dx = abs(x1 - x0)

        offset = 0 * 2 * dx
        threshold = 0.5 * 2 * dx
        y = y0

        points = []

        for x in range(x0, x1):
            if steep:
                points.append((y, x))
            else:
                points.append((x, y))

            offset += (dy/dx) * 2 * dx
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += 1 * 2 * dx

        for point in points:
            self.glPoint(((point[0]-self.OffsetX)*(2/self.ImageWidth)-1),
                         ((point[1]-self.OffsetY)*(2/self.ImageHeight)-1))

    def zBuffer(self):
        f = open('zbuffer.bmp', 'bw')

        # File header (14 bytes)
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # Image header (40 bytes)
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        for y in range(0, self.height-1):
            for x in range(0, self.width):

                try:

                    toWrite = color(
                        self.pixelsZBuffer[x][y], self.pixelsZBuffer[x][y], self.pixelsZBuffer[x][y])

                except:
                    toWrite = color(0, 0, 0)

                f.write(toWrite)

        f.close()

    def triangle(self, A, B, C, color=None, texture=None, texture_coords=(), intensity=1):
        xmin, xmax, ymin, ymax = bbox(A, B, C)
        xmin, xmax, ymin, ymax = int(xmin), int(xmax), int(ymin), int(ymax)

        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                P = V2(x, y)
                w, v, u = barycentric(A, B, C, P)

                if w < 0 or v < 0 or u < 0:
                    continue

                if texture:
                    tA, tB, tC = texture_coords
                    tx = tA.x * w + tB.x * v + tC.x * u
                    ty = tA.y * w + tB.y * v + tC.y * u
                    color = texture.get_color(tx, ty, intensity)

                z = A.z * w + B.z * v + C.z * u

                tempx = int(((x/self.width)+1) *
                            (self.ImageWidth/2)+self.OffsetX)
                tempy = int(((y/self.height)+1) *
                            (self.ImageHeight/2)+self.OffsetY)

                try:
                    if z > self.pixelsZBuffer[tempx][tempy]:
                        self.current_color = color
                        self.glVertex(x/self.width, y/self.height)
                        self.pixelsZBuffer[tempx][tempy] = z
                except:
                    pass

    def transform(self, vertex):
        augmentedVertex = V4(vertex[0], vertex[1], vertex[2], 1)

        matrix1 = product_matrix_vector(self.model, augmentedVertex)
        matrix2 = product_matrix_vector(self.View, matrix1)
        matrix3 = product_matrix_vector(self.Projection, matrix2)
        transformedVertex = product_matrix_vector(self.Viewport, matrix3)

        transformedVertex = V4(*transformedVertex)

        return V3(
            transformedVertex.x / transformedVertex.w,
            transformedVertex.y / transformedVertex.w,
            transformedVertex.z / transformedVertex.w
        )

    def look(self, eye, center, up):
        z = norm(sub(eye, center))
        x = norm(cross(up, z))
        y = norm(cross(z, x))
        self.ViewMatrix(x, y, z, center)
        self.loadProjectionMatrix(-1 / length(sub(eye, center)))
        self.loadViewportMatrix()

    def loadMatrix(self, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
        translate = V3(*translate)
        scale = V3(*scale)
        rotate = V3(*rotate)

        translateMatrix = [
            [1, 0, 0, translate.x],
            [0, 1, 0, translate.y],
            [0, 0, 1, translate.z],
            [0, 0, 0, 1]
        ]

        scaleMatrix = [
            [scale.x, 0, 0, 0],
            [0, scale.y, 0, 0],
            [0, 0, scale.z, 0],
            [0, 0, 0, 1]
        ]

        rotateXMatrix = [
            [1, 0, 0, 0],
            [0, cos(rotate.x), -sin(rotate.x), 0],
            [0, sin(rotate.x), cos(rotate.x), 0],
            [0, 0, 0, 1]
        ]

        rotateYMatrix = [
            [cos(rotate.y), 0, sin(rotate.y), 0],
            [0, 1, 0, 0],
            [-sin(rotate.y), 0, cos(rotate.y), 0],
            [0, 0, 0, 1]
        ]

        rotateZMatrix = [
            [cos(rotate.z), -sin(rotate.z), 0, 0],
            [sin(rotate.z), cos(rotate.z), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

        rotateMatrix = product_matrix(product_matrix(
            rotateYMatrix, rotateZMatrix), rotateZMatrix)
        self.model = product_matrix(product_matrix(
            translateMatrix, scaleMatrix), rotateMatrix)

    def ViewMatrix(self, x, y, z, center):
        Mi = [
            [x.x, x.y, x.z,  0],
            [y.x, y.y, y.z, 0],
            [z.x, z.y, z.z, 0],
            [0,     0,   0, 1]
        ]

        Op = [
            [1, 0, 0, -center.x],
            [0, 1, 0, -center.y],
            [0, 0, 1, -center.z],
            [0, 0, 0, 1]
        ]

        self.View = product_matrix(Mi, Op)

    def loadProjectionMatrix(self, coeff):
        self.Projection = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, coeff, 1]
        ]

    def loadViewportMatrix(self, x=0, y=0):
        self.Viewport = [
            [self.width/2, 0, 0, x + self.width/2],
            [0, self.height/2, 0, y + self.height/2],
            [0, 0, 128, 128],
            [0, 0, 0, 1]
        ]
