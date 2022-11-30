from ray import *
from tools import *
from esfe import *

WHITE = Material(diffuse=color(255, 255, 255), albedo=[1.5, 0], spec=0)
BLACK = Material(diffuse=color(0, 0, 0), albedo=[2, 0.1], spec=30)
PLASTIC = Material(diffuse=color(250, 250, 250),
                   albedo=[0.9, 0.1], spec=50)

BROWN = Material(diffuse=color(215, 158, 130), albedo=[1, 0], spec=0)
COFEE = Material(diffuse=color(152, 64, 18), albedo=[1, 0], spec=0)
RED = Material(diffuse=color(200, 0, 0), albedo=[0.6, 0.3], spec=50)


def main():

    r = RayT(1200, 500)
    r.light = Light(
        position=V3(0, 0, 0),
        intensity=2,
        color=color(255, 255, 255)
    )

    r.scene = [
        # cabeza izquierda
        esfera(V3(-2, -2, -9), 2, WHITE),
        esfera(V3(-3.2, -3, -8.2), 0.8, WHITE),
        esfera(V3(-0.5, -3, -8.2), 0.8, WHITE),
        esfera(V3(-1.75, -1.3, -7.8), 1, WHITE),
        esfera(V3(-1.5, -1.3, -6.5), 0.4, BLACK),
        esfera(V3(-1, -2, -6.5), 0.2, BLACK),
        esfera(V3(-2, -2, -6.5), 0.2, BLACK),
        # # # cuerpo izquierdo
        esfera(V3(-2, 2, -9), 2.5, PLASTIC),
        esfera(V3(-4.3, 0.7, -8.2), 1, WHITE),
        esfera(V3(0.3, 0.7, -8.2), 1, WHITE),
        esfera(V3(-4.3, 3.5, -8.2), 1, WHITE),
        esfera(V3(0.3, 3.5, -8.2), 1, WHITE),

        # cabeza izquierda
        esfera(V3(5.5, -2, -9), 2, BROWN),
        esfera(V3(3.8, -3, -8.2), 0.8, COFEE),
        esfera(V3(6.8, -3, -8.2), 0.8, COFEE),
        esfera(V3(5.4, -1.3, -7.8), 1, COFEE),
        esfera(V3(5, -1.3, -6.5), 0.4, BLACK),
        esfera(V3(4, -2, -6.5), 0.2, BLACK),
        esfera(V3(5.5, -2, -6.5), 0.2, BLACK),
        # cabeza derecha
        esfera(V3(5.5, 2, -9), 2.5, RED),
        esfera(V3(3.2, 0.7, -8.2), 1, BROWN),
        esfera(V3(8, 0.7, -8.2), 1, BROWN),
        esfera(V3(3.2, 3.5, -8.2), 1, BROWN),
        esfera(V3(8, 3.5, -8.2), 1, BROWN),
    ]

    r.dense = 1
    r.point(100, 100)
    r.render()

    r.write()


main()
