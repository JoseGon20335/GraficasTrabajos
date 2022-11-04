import pygame
from OpenGL.GL import *
from utils import pixel
import random
import numpy as np

pygame.init()

cols2 = 600
rows2 = 600

mundo = (cols2, rows2)

s = 10

cols = int(rows2/s)
rows = int(cols2/s)


def creaGrid(grid):
    for i in range(rows):
        arr = []
        for j in range(cols):
            arr.append(random.randint(0, 1))
        grid.append(arr)
    return grid


screen = pygame.display.set_mode(
    (cols2, rows2), pygame.OPENGL | pygame.DOUBLEBUF)

arrayInicial = [[0, 0], [1, 1]]


def count(grid, x, y):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (y+j+cols) % cols
            row = (x+i+rows) % rows
            c += grid[row][col]
    c -= grid[x][y]
    return c


def main():

    grid = []

    grid = creaGrid(grid)

    running = True
    while running:
        # clean
        color = [255, 0, 0]
        color = color[0]/255, color[1]/255, color[2]/255
        glClearColor(color[0], color[1], color[2], 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        for i in range(cols):
            for j in range(rows):
                x = i * s
                y = j * s
                if grid[j][i] == 1:
                    pixel(x, y, (255, 255, 255), s)
                elif grid[j][i] == 0:
                    pixel(x, y, (0.0, 0.0, 0.0), s)

        new_grid = []
        for i in range(rows):
            arr = []
            for j in range(cols):
                arr.append(0)
            new_grid.append(arr)

        for i in range(cols):
            for j in range(rows):
                neighbors = count(grid, j, i)
                state = grid[j][i]
                if state == 0 and neighbors == 3:
                    new_grid[j][i] = 1
                elif state == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[j][i] = 0
                else:
                    new_grid[j][i] = state

        grid = new_grid

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()
