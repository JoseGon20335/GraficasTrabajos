from gl import Renderer


def main():

    glO = Renderer()
    glO.glInit()
    glO.glColor(1, 1, 1)
    glO.glClearColor(0, 0, 0)
    glO.glCreateWindow(800, 800)
    glO.glViewPort(0, 0, 800, 800)

    glO.glLoad('./models/archivo.obj', (0, -50, 0), (10, 10, 10))

    glO.glFinish()
    glO.zBuffer()


main()
