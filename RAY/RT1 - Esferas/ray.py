from tools import *
from esfe import *
from math import *
import random


class RayT (object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = color(0, 0, 0)
        self.current_color = color(255, 255, 255)
        self.scene = []
        self.dense = 1
        self.clear()

    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]

    def point(self, x, y, color=None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = color or self.current_color

    def write(self):
        createBmp(self.width, self.height, self.framebuffer)

    # rayo inifinitio
    def cast_ray(self, origin, direction):

        for esfe in self.scene:
            intersection = esfe.ray_intersect(origin, direction)
            if intersection:
                return esfe.color

        return self.background_color

    def render(self):
        fov = int(pi/2)  # apertura del angulo de la camara
        ar = self.width/self.height  # aspect ratio
        tana = tan(fov/2)  # tan del angulo de la camara

        black = color(0, 0, 0)
        white = color(255, 255, 255)
        orange = color(255, 165, 0)

        self.scene.append(Sphere(V3(0.5, -3, -14), 0.2, black))
        self.scene.append(Sphere(V3(-0.5, -3, -14), 0.2, black))
        self.scene.append(Sphere(V3(0, -3, -14), 0.2, orange))

        self.scene.append(Sphere(V3(0, 1.8, -14), 0.3, black))
        self.scene.append(Sphere(V3(0, 0.5, -14), 0.3, black))
        self.scene.append(Sphere(V3(0, -0.8, -14), 0.3, black))

        self.scene.append(Sphere(V3(0, 4, -14), 2.5, white))
        self.scene.append(Sphere(V3(0, 0, -14), 2, white))
        self.scene.append(Sphere(V3(0, -2.8, -14), 1.5, white))

        for y in range(self.height):
            for x in range(self.width):
                r = random.uniform(0, 1)
                if r < self.dense:
                    i = ((2 * (x + 0.5) / self.width) - 1) * ar * tana
                    j = (1 - 2 * (y + 0.5) / self.height) * tana

                    direction = V3(i, j, -1).norm()
                    origin = V3(0, 0, 0)

                    c = self.cast_ray(origin, direction)

                    self.point(x, y, c)
