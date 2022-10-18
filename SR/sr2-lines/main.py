from gl import Renderer


def main():

    glO = Renderer()
    glO.glInit()
    glO.glColor(1, 1, 1)
    glO.glClearColor(0, 0, 0)
    glO.glCreateWindow(1000, 1000)
    glO.glViewPort(0, 0, 1000, 1000)

    glO.glLoad('./models/archivo.obj', (0, -1.3), (0.45, 0.45))

    glO.glFinish()


main()