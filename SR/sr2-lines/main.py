from gl import Renderer


def main():

    glO = Renderer()
    glO.glInit()
    glO.glColor(1, 1, 1)
    glO.glClearColor(0, 0, 0)
    glO.glCreateWindow(1000, 1000)
    glO.glViewPort(0, 0, 1000, 1000)

    glO.glLine(-0.57, -0.28, -0.14, -0.6)
    glO.glLine(-0.57, -0.28, -0.57, 0.05)
    glO.glLine(-0.57, 0.05, -0.14, -0.28)
    glO.glLine(-0.14, -0.6, -0.14, -0.28)
    glO.glLine(-0.57, 0.05, -0.14, 0.6)
    glO.glLine(-0.14, -0.28, 0.27, 0.27)

    glO.glLine(-0.14, 0.6, 0.27, 0.27)
    glO.glLine(-0.14, -0.6, 0.71, -0.34)
    glO.glLine(0.18, -0.5, 0.18, -0.31)
    glO.glLine(0.18, -0.31, 0.4, -0.26)
    glO.glLine(0.4, -0.45, 0.4, -0.26)
    glO.glLine(0.71, -0.34, 0.71, -0.06)
    glO.glLine(-0.15, -0.28, 0.71, -0.065)
    glO.glLine(0.25, 0.28, 0.71, -0.065)
    glO.glLine(0.01, 0.48, 0.01, 0.56)
    glO.glLine(0.10, 0.4, 0.10, 0.50)
    glO.glLine(0.01, 0.56, 0.1, 0.49)
    glO.glLine(0.01, 0.56, 0.12, 0.59)
    glO.glLine(0.12, 0.59, 0.2, 0.53)
    glO.glLine(0.10, 0.50, 0.20, 0.525)
    glO.glLine(0.20, 0.33, 0.20, 0.53)

    glO.glFinish()


main()
