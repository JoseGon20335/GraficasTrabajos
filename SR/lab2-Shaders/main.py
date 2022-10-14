from gl import Renderer
from texture import Texture
from collections import namedtuple

V2 = namedtuple('Point2D', ['x', 'y'])
V3 = namedtuple('Point3D', ['x', 'y', 'z'])
V4 = namedtuple('Point4D', ['x', 'y', 'z', 'w'])


def main():
    glO = Renderer()
    glO.glInit()
    glO.glCreateWindow(1000, 1000)
    glO.glViewPort(0, 0, 1000, 1000)

    glO.look(V3(0, -9, 50), V3(0, 0, 0), V3(0, 1, 10))
    glO.stars()

    glO.glLoad('./models/sphere.obj', (-1, -1, 0),
               (1.2, 1.2, 1.5), (0, 0, 0), shader="sphere")

    glO.glFinish()


main()
