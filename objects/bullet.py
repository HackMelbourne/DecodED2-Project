import pygame
from pygame import Vector2
from pygame.locals import K_LEFT, K_RIGHT, KEYDOWN, KEYUP

from constants import SCREEN_H, SCREEN_W, BULLET_SPEED
from game_object import GameObject
from objects.enemy import Enemy

class Bullet(GameObject):
    def __init__(self, player_position):
        super().__init__(10, 10, 'res/bullet.png')
        self.position.x = player_position.x
        self.position.y = player_position.y
        # Bullet speed needs to be negative since its travelling upwards
        self.velocity.y = -BULLET_SPEED

    def update(self, delta, events, objects):
        super().update(delta, events, objects)
        # check if bullet hits enemy
        for obj in objects:
            if isinstance(obj, Enemy) and self.rect.colliderect(obj.rect):
                self.expired = True
                obj.expired = True
        # Remove bullet once out of bounds
        if self.position.y < 0:
            self.expired = True


