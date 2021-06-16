import pygame
from pygame import Vector2

from constants import SCREEN_H, SCREEN_W

from game_object import GameObject


class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.position = Vector2(SCREEN_W / 2, SCREEN_H / 2)
        self.velocity = Vector2(0, 0.1)

    # TODO update method, rn using the game object update

    def render(self, display):
        pygame.draw.circle(display, (255, 0, 0), self.position, 20)
