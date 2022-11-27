from gl import Renderer


def main():

    glO = Renderer()
    glO.glInit()
    glO.glClearColor(0, 0, 0)
    glO.glCreateWindow(1000, 500)
    glO.glViewPort(0, 0, 1000, 500)

    glO.glColor(1, 0.5, 0.5)
    glO.glModels('models/poligono1.txt')
    glO.glFill('models/poligono1.txt')

    glO.glColor(0, 1, 1)
    glO.glModels('models/poligono2.txt')
    glO.glFill('models/poligono2.txt')

    glO.glColor(1, 1, 1)
    glO.glModels('models/poligono4.txt')
    glO.glFill('models/poligono4.txt')

    glO.glColor(0, 0, 0)
    glO.glModels('models/poligono5.txt')
    glO.glFill('models/poligono5.txt')

    glO.glColor(1, 0, 0)
    glO.glModels('models/poligono3.txt')
    glO.glFill('models/poligono3.txt')

    glO.glFinish()


main()
