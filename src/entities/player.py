import pygame
from pygame import Vector2
from pygame.locals import K_LEFT, K_RIGHT, KEYDOWN, KEYUP

from src.constants import SCREEN_H, SCREEN_W, PLAYER_START_VECTOR, PLAYER_START_SPEED
from src.entity import Entity
from src.entities.enemy import Enemy


class Player(Entity):
    speed: float

    def __init__(self):
        super().__init__(40, 40, 'res/player.png')
        # Movement trackings
        self.move_direction = 0

        self.position.x = PLAYER_START_VECTOR.x  # Could put these in constants.py?
        self.position.y = PLAYER_START_VECTOR.y
        self.speed = PLAYER_START_SPEED

    def move_left(self):
        self.move_direction = -1
    
    def move_right(self):
        self.move_direction = 1
    
    def stop_moving(self):
        self.move_direction = 0

    def update(self, delta, events, objects):
        super().update(delta, events, objects)

        # Set the movement velocity of the player based on its current direction
        self.velocity.x = self.move_direction * self.speed

        for event in events:
            if event.type == KEYUP:
                if event.key == K_LEFT and self.move_direction < 0:
                    self.stop_moving()
                if event.key == K_RIGHT and self.move_direction > 0:
                    self.stop_moving()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.move_left()
                if event.key == K_RIGHT:
                    self.move_right()

        # teleport player back to screen
        self.boundary_check()
        # check if player is dead
        for obj in objects:
            if isinstance(obj, Enemy) and self.rect.colliderect(obj.rect):
                self.expired = True
