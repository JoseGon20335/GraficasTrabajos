from gl import Renderer
from texture import Texture


def main():

    glO = Renderer()
    glO.glInit()
    glO.glColor(1, 1, 1)
    glO.glClearColor(0, 0, 0)
    glO.glCreateWindow(800, 800)
    glO.glViewPort(0, 0, 800, 800)

    texture = Texture('./models/model.bmp')
    glO.glLoad('./models/model.obj', (0, -4, 0),
               (130, 130, 130), texture=texture)
    glO.glFinish()


main()
