from ray import *
from tools import *
from esfe import *

# falta arreglar


def main():
    white = Material(diffuse=color(255, 255, 255), albedo=[1, 0], spec=0)
    black = Material(diffuse=color(0, 0, 0), albedo=[0.9, 0.1], spec=30)
    metal = Material(diffuse=color(250, 250, 250), albedo=[0.9, 0.1], spec=50)

    brown = Material(diffuse=color(215, 158, 130), albedo=[1, 0], spec=0)
    dark_brown = Material(diffuse=color(152, 64, 18), albedo=[1, 0], spec=0)
    red = Material(diffuse=color(200, 0, 0), albedo=[0.6, 0.3], spec=50)

    r = RayT(1200, 500)
    r.light = Light(
        position=V3(0, 0, 0),
        intensity=2,
        color=color(255, 255, 255)
    )

    r.scene = [
        esfera(V3(-2, -2, -9), 2, white),  # face
        esfera(V3(-1.8, -1.8, -7.8), 0.95, white),  # mouth
        esfera(V3(-1.7, -1.8, -7.2), 0.4, black),  # mouth

        esfera(V3(-3.5, -3, -8), 0.9, white),  # ear
        esfera(V3(0, -3, -8.2), 0.9, white),  # ear

        esfera(V3(-2, 1, -9), 2.5, metal),  # body

        esfera(V3(-4, 0, -8), 1, white),  # arm
        esfera(V3(0.5, 0, -8.2), 1, white),  # arm

        esfera(V3(-4, 2.5, -8), 1, white),  # leg
        esfera(V3(0.5, 2.5, -8.2), 1, white),  # leg

        esfera(V3(-2.5, -2.2, -7.2), 0.2, black),  # eye
        esfera(V3(-0.95, -2.2, -7.4), 0.2, black),  # eye


        esfera(V3(5, -2, -9), 2, brown),  # face
        esfera(V3(4.8, -1.8, -7.8), 0.95, brown),  # mouth
        esfera(V3(4.7, -1.8, -7.2), 0.4, dark_brown),  # mouth

        esfera(V3(3, -3.1, -8), 0.9, dark_brown),  # ear
        esfera(V3(6, -3, -7.8), 0.9, dark_brown),  # ear

        esfera(V3(5, 1, -9), 2.5, red),  # body

        esfera(V3(3, 0, -8), 1, brown),  # arm
        esfera(V3(5.5, 0.1, -7.2), 1, brown),  # arm

        esfera(V3(3, 2.5, -8), 1, brown),  # leg
        esfera(V3(5.7, 2.1, -7.3), 1, brown),  # leg

        esfera(V3(5.55, -2.2, -7.15), 0.2, black),  # eye
        esfera(V3(3.7, -2.2, -7.2), 0.2, black),  # eye

    ]

    r.dense = 1
    r.point(100, 100)
    r.render()

    r.write('r.bmp')


main()
