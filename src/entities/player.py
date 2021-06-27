import pygame
from pygame import Vector2
from pygame.locals import K_LEFT, K_RIGHT, KEYDOWN, KEYUP

from src.constants import SCREEN_H, SCREEN_W, PLAYER_START_VECTOR, PLAYER_START_SPEED, BULLET_COOLDOWN
from src.entity import Entity
from src.entities.enemy import Enemy
from src.entities.bullet import Bullet

class Player(Entity):
    def __init__(self):
        super().__init__(PLAYER_START_VECTOR.x, PLAYER_START_VECTOR.y, 40, 40, 'res/player.png')
        self.move_direction = 0
        self.shooting = False
        self.bullet_cooldown = BULLET_COOLDOWN
        self.speed = PLAYER_START_SPEED

    def move_left(self):
        self.move_direction = -1
    
    def move_right(self):
        self.move_direction = 1
    
    def stop_moving(self):
        self.move_direction = 0

    def shoot(self):
        if self.bullet_cooldown == BULLET_COOLDOWN:
            self.shooting = True

    def tick(self, delta, objects):
        # Keep track of bullet cooldown
        if self.bullet_cooldown >= BULLET_COOLDOWN:
            self.bullet_cooldown = BULLET_COOLDOWN
        else:
            self.bullet_cooldown += delta

        # Shoot a bullet
        if self.shooting:
            objects.append(Bullet(Vector2(self.x, self.y)))
            self.shooting = False
            self.bullet_cooldown = 0

        # Set the movement velocity of the player based on its current direction
        self.velocity.x = self.move_direction * self.speed

        # teleport player back to screen
        self.boundary_check()
        
        # check if player is dead
        for obj in objects:
            if isinstance(obj, Enemy) and self.colliderect(obj):
                self.expired = True
