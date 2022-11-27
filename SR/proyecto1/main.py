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

    glO.look(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 1))

    # background = Texture('./models/background.bmp')
    # glO.pixels = background.pixels

    background = Texture('./models/back.bmp')
    glO.pixels = background.pixels

    # work
    texture = Texture('./models/deku.bmp')
    glO.glLoad('./models/deku.obj', (-1.3, -1.5, 1),
               (0.25, 0.25, 0.25), (0, 0, 0), texture=texture)

    # work
    texture = Texture('./models/link.bmp')
    glO.glLoad('./models/link.obj', (-2, -2.4, 0),
               (0.3, 0.3, 0.3), (0, 0, 0), texture=texture)

    # work
    texture = Texture('./models/navy.bmp')
    glO.glLoad('./models/navy.obj', (0, -1, 0),
               (0.2, 0.2, 0.2), (1, 2, 0), texture=texture)

    # work
    texture = Texture('./models/jaron.bmp')
    glO.glLoad('./models/jaron.obj', (-1, -2.5, 0),
               (1.5, 1.5, 1.5), (0, 0, 0), texture=texture)

    # work
    texture = Texture('./models/sword.bmp')
    glO.glLoad('./models/sword.obj', (-2.6, -1.2, 0),
               (1.5, 1.5, 1.5), (2, 0, 1.7), texture=texture)

    glO.glFinish()


main()
