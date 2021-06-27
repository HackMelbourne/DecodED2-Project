import pygame
from pygame import Vector2

from src.constants import ROW_JUMP_SIZE, ENEMY_SPEED
from src.entity import Entity


# Enemies will be positioned in a grid layout where the enemy will spawn at random in any one of these grid
# squares

class Enemy(Entity):
    turn = False  # Tells whether enemy needs to turn or not
    direction = 1

    def __init__(self, coords):
        super().__init__(coords.x, coords.y, 20, 20, 'res/enemy.png')
        self.velocity.x = ENEMY_SPEED

    def tick(self, delta, objects):
        if self.turn:
            self.direction *= -1
            self.velocity.y = ROW_JUMP_SIZE
            self.turn = False
        else:
            self.velocity.y = 0

            # Jump a row once the screen border is hit 
            # Updates static variable for all enemy instances
            if self.boundary_check():
                self.turn = True
        self.velocity.x = ENEMY_SPEED * self.direction
