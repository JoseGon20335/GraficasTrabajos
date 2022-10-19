from gl import Renderer
from texture import Texture


def main():

    glO = Renderer()
    glO.glInit()
    glO.glColor(1, 1, 1)
    glO.glClearColor(0, 0, 0)
    glO.glCreateWindow(800, 800)
    glO.glViewPort(0, 0, 500, 500)

    # texture = Texture('./models/figura.bmp')
    # glO.glLoad('./models/figura.obj', (0, -4, 0),
    #            (130, 130, 130), texture=texture)

    # texture = Texture('./models/TIE.bmp')
    # glO.glLoad('./models/TIE.obj', (0, -4, 0),
    #            (130, 130, 130), texture=texture)

    texture = Texture('./models/xwing.bmp')
    glO.glLoad('./models/xwing.obj', (6, 6, 6),
               (50, 50, 50), texture=texture)

    glO.glFinish()


main()
