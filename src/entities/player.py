import pygame
from pygame import Vector2
from pygame.locals import K_LEFT, K_RIGHT, KEYDOWN, KEYUP

from src.constants import SCREEN_H, SCREEN_W
from src.entity import Entity
from src.entities.enemy import Enemy

PLAYER_START_VECTOR = Vector2(370, 480)
PLAYER_START_SPEED = 0.8


class Player(Entity):
    speed: float

    def __init__(self):
        super().__init__(40, 40, 'res/player.png')
        # Movement tracking
        self.moving_right = False
        self.moving_left = False

        self.position.x = PLAYER_START_VECTOR.x  # Could put these in constants.py?
        self.position.y = PLAYER_START_VECTOR.y
        self.speed = PLAYER_START_SPEED

    def update(self, delta, events, objects):
        super().update(delta, events, objects)
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
            self.velocity.x = -self.speed
        elif self.moving_right:
            self.velocity.x = self.speed
        else:
            self.velocity.x = 0
        # teleport player back to screen
        self.boundary_check()
        # check if player is dead
        for obj in objects:
            if isinstance(obj, Enemy) and self.rect.colliderect(obj.rect):
                self.expired = True
