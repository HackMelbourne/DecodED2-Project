import pygame
from pygame.locals import *

SCREEN_W = 640
SCREEN_H = 480
WHITE = (255, 255, 255)


def main():
    display = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
    running = True

    while(running):
        display.fill(WHITE)
        for e in pygame.event.get():
            if e.type == QUIT:
                running = False

        pygame.display.update()

if __name__ == "__main__":
    main()