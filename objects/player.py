import pygame
from pygame import Vector2
from pygame.locals import K_LEFT, K_RIGHT, KEYDOWN, KEYUP

from constants import SCREEN_H, SCREEN_W
from game_object import GameObject


class Player(GameObject):
    moving_left: bool = False
    moving_right: bool = False
    # Player attributes
    SPEED: float = 0.8
    WIDTH = 40

    def __init__(self):
        super().__init__()
        self.position = Vector2(SCREEN_W / 2, SCREEN_H / 2)

    def update(self, delta: int, events: list[pygame.event.Event]):
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

        # teleport user back if they are walking off screen
        if self.position.x < self.WIDTH / 2:
            self.position.x = self.WIDTH / 2
        elif self.position.x > SCREEN_W - self.WIDTH / 2:
            self.position.x = SCREEN_W - self.WIDTH / 2

    def render(self, display):
        pygame.draw.circle(display, (255, 0, 0), self.position, self.WIDTH / 2)
