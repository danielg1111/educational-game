import pygame
from pygame.locals import *

_quit = False
fs = False
SW, SH = 640, 480
FSW, FSH = SW, SH


def toggle_full_screen():
    global fs, screen, SW, SH
    if fs:
        pygame.display.set_mode((SW, SH))
        fs = False
    else:
        pygame.display.set_mode((FSW, FSH), pygame.FULLSCREEN)
        fs = True


def resize_screen(ev):
    global FSW, FSH, fs

    resize = True
    if ev.key == K_RETURN:
        resize = False
        toggle_full_screen()
    elif ev.key == K_1:
        FSW = 640
        FSH = 480
    elif ev.key == K_2:
        FSW = 1280
        FSH = 720
    elif ev.key == K_3:
        FSW = 1920
        FSH = 1080
    elif ev.key == K_4:
        FSW = 2560
        FSH = 1600
    else:
        resize = False

    if resize:
        pygame.display.set_mode((FSW, FSH), pygame.FULLSCREEN)
        fs = True


def handle_input():
    global _quit
    for e in pygame.event.get():
        if e.type is KEYDOWN:
            resize_screen(e)
            if e.key == K_ESCAPE:
                _quit = True
        if e.type is QUIT:
            _quit = True


if __name__ == '__main__':
    pygame.display.set_mode((SW, SH))
    pygame.display.set_caption('HackUMass 2019')
    pygame.display.init()

    while not _quit:
        handle_input()
        screen = pygame.display.get_surface()
        screen.fill([0, 0, 0])

        pygame.display.flip()

    pygame.display.quit()
