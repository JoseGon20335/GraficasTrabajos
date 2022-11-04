import pygame
from OpenGL.GL import *


def pixel(x, y, color, scale):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y, scale, scale)
    glClearColor(color[0], color[1], color[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)
