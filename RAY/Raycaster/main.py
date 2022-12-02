import pygame
from math import *
import pygame_menu
from pygame import mixer
from Raycaster import *
from tools import *
from temasPygame import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY = (0, 0, 0)
GROUND = (36, 36, 36)
TRANSPARENT = (152, 0, 136, 255)


def running(screen, map, musica, level):
    r = Raycaster(screen)
    r.load_map(map)

    music(musica)

    clock = pygame.time.Clock()

    running = True
    x = r.player['x']
    y = r.player['y']
    a = r.player['a']

    movement = 5
    first_time = True

    while running:
        screen.fill(BLACK, (0, 0, 100, r.height))
        screen.fill(SKY, (100, 0, 900, r.height/2))
        screen.fill(GROUND, (100, r.height/2, 900, r.height/2))

        try:
            r.render()
            r.clearZ()
        except:
            r.player['x'] = x
            r.player['y'] = y

        fps = FPS()
        screen.blit(fps, (525, 10))

        if pygame.time.get_ticks() < 6000000:
            message = "Time: " + \
                str(60 - pygame.time.get_ticks()//1000)
            message = (pygame.font.SysFont("Helvetica", 20)).render(
                message, 10, pygame.Color("white"))
            screen.blit(message, (110, 10))
        else:
            FAIL(screen)
            running = False

        x = r.player['x']
        y = r.player['y']

        if(level == 1):
            if 420 <= x <= 440 and 420 <= y <= 440:
                WIN(screen)
                running = False
            if 340 <= x <= 360 and 420 <= y <= 440:
                WIN(screen)
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()

            if event.type == pygame.MOUSEMOTION:
                r.player['a'] += event.rel[0]/200

            if keys[pygame.K_a]:
                r.player['a'] -= pi/10
            if keys[pygame.K_d]:
                r.player['a'] += pi/10

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                r.player['x'] += cos(r.player['a']) * movement
                r.player['y'] += sin(r.player['a']) * movement

                # sonido de pasos
                effect = mixer.Sound('./steps.mp3')
                effect.set_volume(0.2)
                effect.play()

            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                r.player['x'] -= cos(r.player['a']) * movement
                r.player['y'] -= sin(r.player['a']) * movement

                # sonido de pasos
                effect = mixer.Sound('./steps.mp3')
                effect.set_volume(0.2)
                effect.play()

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                r.player['x'] -= cos(r.player['a'] + pi/2) * movement
                r.player['y'] -= sin(r.player['a'] + pi/2) * movement
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                r.player['x'] += cos(r.player['a'] + pi/2) * movement
                r.player['y'] += sin(r.player['a'] + pi/2) * movement

        clock.tick(60)
        pygame.display.update()

    music('./music/pista1.mp3')


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))

    # pantalla de menu
    h = harry()
    menu = pygame_menu.Menu('Harry Potter Maze', 600, 500, theme=h)
    menu.add.button('Escape del gulag', running, screen,
                    './niveles/map.txt', './music/scape.mp3', 1)
    menu.add.button('Escape de Alcatraz', running, screen,
                    './niveles/map2.txt', './music/scape.mp3', 2)
    menu.add.button('Cerrar', pygame_menu.events.EXIT)

    # musica de patanlla de inicio
    mixer.music.stop()
    mixer.music.load('./music/pista1.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)

    menu.mainloop(screen, fps_limit=60.0)


main()
