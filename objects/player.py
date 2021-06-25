import pygame
from pygame import Vector2
from pygame.locals import K_LEFT, K_RIGHT, KEYDOWN, KEYUP

from constants import SCREEN_H, SCREEN_W
from game_object import GameObject


class Player(GameObject):
    moving_left = False
    moving_right = False
    # Player attributes

    def __init__(self):
        super().__init__()
        self.position = Vector2(370, 480) # Could put these in constants.py?
        self.SPEED = 0.8
        self.WIDTH = 40

    def update(self, delta, events):
        super().update(delta, events)
        for event in events:
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    self.moving_left = False
                if event.key == K_RIGHT:
                    self.moving_right = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.moving_left = True
                if event.key == K_RIGHT:
                    self.moving_right = True
        if self.moving_left:
            self.velocity.x = -self.SPEED
        elif self.moving_right:
            self.velocity.x = self.SPEED
        else:
            self.velocity.x = 0
        
        self.boundary_check()

    def render(self, display):
        pygame.draw.circle(display, (255, 0, 0), self.position, self.WIDTH / 2)
