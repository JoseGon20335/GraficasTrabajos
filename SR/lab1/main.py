from gl import Renderer


def main():

    glO = Renderer()
    glO.glInit()
    glO.glColor(1, 1, 1)
    glO.glClearColor(0, 0, 0)
    glO.glCreateWindow(1000, 1000)
    glO.glViewPort(0, 0, 1000, 1000)

    glO.glColor(1, 1, 0)
    glO.glModels('lab1/models/figura1.txt')
    glO.glFill('lab1/models/figura1.txt')

    glO.glColor(0, 0, 1)
    glO.glModels('lab1/models/figura2.txt')
    glO.glFill('lab1/models/figura2.txt')

    glO.glColor(0.5, 0, 0.5)
    glO.glModels('lab1/models/figura4.txt')
    glO.glFill('lab1/models/figura4.txt')

    glO.glColor(0, 0, 0)
    glO.glModels('lab1/models/figura5.txt')
    glO.glFill('lab1/models/figura5.txt')

    glO.glColor(1, 0, 0)
    glO.glModels('lab1/models/figura3.txt')
    glO.glFill('lab1/models/figura3.txt')

    glO.glFinish()


main()
