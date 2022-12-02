import pygame
from math import *
from pygame import mixer
import pygame_menu

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY = (135, 206, 235)
GROUND = (100, 0, 0)
TRANSPARENT = (152, 0, 136, 255)


def music(music):
    mixer.music.stop()
    mixer.music.load(music)
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)


def FPS():
    fps = str("FPS: "+str(int((pygame.time.Clock()).get_fps())))
    fps = (pygame.font.SysFont("Arial", 20)).render(
        fps, 10, pygame.Color("white"))
    return fps


def FAIL(screen):

    mixer.music.stop()
    mixer.music.load('./music/lose.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.4)

    screen.fill(BLACK)
    message = "FIN! No has escapado a tiempo"
    message = (pygame.font.SysFont("Helvetica", 40)).render(
        message, 10, pygame.Color("white"))
    screen.blit(message, (30, 200))
    pygame.display.flip()
    pygame.time.wait(5000)


def WIN(screen):

    mixer.music.stop()
    mixer.music.load('./music/victory.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)

    screen.fill(BLACK)
    message = "Excelente escapaste! AHORA CORRE"
    message = (pygame.font.SysFont("Helvetica", 40)).render(
        message, 10, pygame.Color("white"))
    screen.blit(message, (30, 200))
    pygame.display.flip()
    pygame.time.wait(5000)
