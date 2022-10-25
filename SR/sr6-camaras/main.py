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
    glO.glCreateWindow(800, 800)
    glO.glViewPort(0, 0, 500, 500)

    glO.look(V3(0, 0, 5), V3(0, 0, 2), V3(0, 1, 1))
    texture = Texture('./models/mo.bmp')
    glO.glLoad('./models/mo.obj', (-1, -3, 0),
               (0.5, 0.5, 0.5), (0, 0, 0), texture=texture)

    # glO.look(V3(0, 0, 5), V3(0, 0, 2), V3(0, 1, 1))
    # texture = Texture('./models/xwing.bmp')
    # glO.glLoad('./models/xwing.obj', (-1, -3, 0),
    #            (0.5, 0.5, 0.5), (0, 0, 0), texture=texture)

    glO.glFinish()


main()
