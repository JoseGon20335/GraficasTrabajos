from gl import Renderer
from texture import Texture
from collections import namedtuple

V2 = namedtuple('Point2D', ['x', 'y'])
V3 = namedtuple('Point3D', ['x', 'y', 'z'])
V4 = namedtuple('Point4D', ['x', 'y', 'z', 'w'])


def main():
    glO = Renderer()
    glO.glInit()
    glO.glColor(1, 1, 1)
    glO.glClearColor(0, 0, 0)
    glO.glCreateWindow(1000, 1000)
    glO.glViewPort(0, 0, 1000, 1000)

    # Medium shot
    # glO.look(V3(0, 0, 20), V3(0, 1, 0), V3(0, 1, 1))
    # texture = Texture('./models/link.bmp')
    # glO.glLoad('./models/link.obj', (-1, -2, 0),
    #            (0.5, 0.5, 0.5), (0, 0, 0), texture=texture)

    # Low angle
    # glO.look(V3(2, -5, 10), V3(0, 0, 0), V3(0, 1, 1))
    # texture = Texture('./models/link.bmp')
    # glO.glLoad('./models/link.obj', (-1, -2.5, 0),
    #            (0.8, 0.8, 0.8), (0, 0, 0), texture=texture)

    # High angle
    # glO.look(V3(0, 9.5, 20), V3(0, 1, 0), V3(0, 1, 1))
    # texture = Texture('./models/link.bmp')
    # glO.glLoad('./models/link.obj', (-1, -2.8, 0),
    #            (0.7, 0.7, 0.7), (0, 0, 0), texture=texture)

    # Dutch angle
    glO.look(V3(9, -5, 10), V3(0, 0, 0), V3(0, 1, 1))
    texture = Texture('./models/link.bmp')
    glO.glLoad('./models/link.obj', (-1, -3, 0),
               (0.8, 0.8, 0.8), (0, -1, 0), texture=texture)

    glO.glFinish()


main()
