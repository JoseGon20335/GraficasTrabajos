from gl import glObject


def main():

    glCreador = glObject()

    glCreador.glInit()
    glCreador.glCreateWindow(50, 50)
    glCreador.glViewPort(5, 5, 40, 40)
    glCreador.glColor(0.9, 0.9, 0.9)
    glCreador.glVertex(1, 1)
    glCreador.glFinish()


main()
