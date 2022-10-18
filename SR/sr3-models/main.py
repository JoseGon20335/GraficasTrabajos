from gl import Renderer


def main():

    glO = Renderer()
    glO.glInit()
    glO.glColor(1, 1, 1)
    glO.glClearColor(0, 0, 0)
    glO.glCreateWindow(1000, 1000)
    glO.glViewPort(0, 0, 1000, 1000)

    glO.glLoad('./models/objeto.obj', (0, 0.5), (0.05, 0.05))

    glO.glFinish()


main()
