import pygame
from pygame import Vector2
from pygame.locals import K_LEFT, K_RIGHT, KEYDOWN, KEYUP

from src.constants import SCREEN_H, SCREEN_W, BULLET_SPEED
from src.entity import Entity
from src.entities.enemy import Enemy

class Bullet(Entity):
    def __init__(self, player_position):
        super().__init__(player_position.x, player_position.y, 10, 10, 'res/bullet.png')
        # Bullet speed needs to be negative since its travelling upwards
        self.velocity.y = -BULLET_SPEED

    def tick(self, delta, objects):
        # check if bullet hits enemy
        for obj in objects:
            if isinstance(obj, Enemy) and self.colliderect(obj):
                self.kill()
                obj.kill()
                
        # Remove bullet once out of bounds
        if self.y < 0:
            self.kill()

