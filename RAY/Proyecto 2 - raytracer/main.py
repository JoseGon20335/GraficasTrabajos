from plane import Plane
from square import Square
from ray import *
from tools import *
from esfe import *

grass = Material(diffuse=color(126, 200, 80),
                 albedo=[0.9,  0.1, 0, 0], spec=10)
white = Material(diffuse=color(255, 255, 255),
                 albedo=[0.8, 0.2, 0, 0], spec=0)
black = Material(diffuse=color(0, 0, 0),
                 albedo=[0.9, 0.1, 0, 0], spec=0)
blue = Material(diffuse=color(44, 66, 133),
                albedo=[0.9, 0.1, 0, 0], spec=0)
brown = Material(diffuse=color(101, 67, 33),
                 albedo=[0.9, 0.1, 0, 0], spec=0)
leaves = Material(diffuse=color(8, 107, 32),
                  albedo=[0.9, 0.1, 0, 0], spec=0)
camisa = Material(diffuse=color(21, 187, 186),
                  albedo=[0.9, 0.1, 0, 0], spec=0)
steve = Material(diffuse=color(255, 221, 168),
                 albedo=[0.9, 0.1, 0, 0], spec=0)
pantalon = Material(diffuse=color(17, 119, 178),
                    albedo=[0.9, 0.1, 0, 0], spec=0)
zapatos = Material(diffuse=color(46, 75, 80),
                   albedo=[0.9, 0.1, 0, 0], spec=0)
pelo = Material(diffuse=color(78, 37, 8),
                albedo=[0.9, 0.1, 0, 0], spec=0)


def main():

    r = RayT(500, 500)
    r.light = Light(
        position=V3(-20, 40, 20),
        intensity=3,
        color=color(255, 255, 255)
    )
    r.dense = 1

    # r.envmap = Envmap('./minesky.bmp')
    r.envmap = Envmap('./sky.bmp')

    r.scene.extend([
        Plane(V3(0, -5, -15), 25, 15, "y", grass),

        *(Square(V3(-4, -3, -13), (30, 30), brown)).planes,
        *(Square(V3(-4, -1, -13), (30, 30), brown)).planes,
        *(Square(V3(-4, 1, -13), (30, 30), brown)).planes,
        *(Square(V3(-3.6, 5, -12), (30, 30), leaves)).planes,
        *(Square(V3(-4, 3, -11), (30, 30), leaves)).planes,
        *(Square(V3(-2, 3, -11), (30, 30), leaves)).planes,
        *(Square(V3(-2, 3, -13), (30, 30), leaves)).planes,
        *(Square(V3(-2, 3, -15), (30, 30), leaves)).planes,
        *(Square(V3(-6, 3, -11), (30, 30), leaves)).planes,
        *(Square(V3(-6, 3, -13), (30, 30), leaves)).planes,
        *(Square(V3(-6, 3, -15), (30, 30), leaves)).planes,


        *(Square(V3(-1.6, -0, -11), (17, 17), steve)).planes,
        *(Square(V3(-1.6, 0.1, -11), (17, 17), pelo)).planes,
        *(Square(V3(-1, 0.6, -11), (5, 5), pelo)).planes,
        *(Square(V3(-1, 0.6, -10.5), (5, 5), pelo)).planes,
        *(Square(V3(-1, 0.6, -10.3), (5, 5), pelo)).planes,
        *(Square(V3(-2.1, 0.6, -10.3), (5, 5), pelo)).planes,
        *(Square(V3(-1.6, 0.65, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-1.8, 0.65, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-2, 0.65, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-2.2, 0.65, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-1.4, 0.65, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-1.2, 0.65, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-1.2, 0.65, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-1, 0.65, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-1.6, -0.6, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-1.5, -0.6, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-1.7, -0.6, -10.3), (3, 3), pelo)).planes,
        *(Square(V3(-2, 0, -10.3), (2.5, 2.5), white)).planes,
        *(Square(V3(-1.8, 0, -10.3), (2.5, 2.5), blue)).planes,
        *(Square(V3(-1.4, 0, -10.3), (2.5, 2.5), blue)).planes,
        *(Square(V3(-1.2, 0, -10.3), (2.5, 2.5), white)).planes,

        *(Square(V3(-1.6, -2, -11), (15, 15), camisa)).planes,
        *(Square(V3(-1.6, -1, -11), (15, 15), camisa)).planes,

        *(Square(V3(-0.7, -1.2, -11), (7.5, 7.5), camisa)).planes,
        *(Square(V3(0, -1.2, -11), (7.5, 7.5), camisa)).planes,
        *(Square(V3(0.7, -1.2, -11), (7.5, 7.5), steve)).planes,
        *(Square(V3(0.6, -0.7, -11), (3.5, 3.5), steve)).planes,

        *(Square(V3(-2.7, -1.2, -11), (7.5, 7.5), camisa)).planes,
        *(Square(V3(-2.7, -1.9, -11), (7.5, 7.5), camisa)).planes,
        *(Square(V3(-2.7, -2.6, -11), (7.5, 7.5), steve)).planes,


        *(Square(V3(-1.6, -3, -11), (15, 15), pantalon)).planes,
        *(Square(V3(-1.6, -3.6, -11), (15, 15), pantalon)).planes,
        *(Square(V3(-1.6, -4, -11), (15, 15), zapatos)).planes,

    ])

    r.render()

    r.write()


main()
