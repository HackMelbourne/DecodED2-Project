import pygame
from pygame import Vector2

from src.constants import ROW_JUMP_SIZE, ENEMY_SPEED
from src.entity import Entity


# Enemies will be positioned in a grid layout where the enemy will spawn at random in any one of these grid
# squares

class Enemy(Entity):
    def __init__(self, coords):
        super().__init__(coords.x, coords.y, 20, 20, 'res/enemy.png')
        self.turn = False
        self.direction = 1

    def tick(self, delta, objects):
        # Jump a row once the screen border is hit 
        # Updates static variable for all enemy instances
        if self.boundary_check():
            self.turn = True
            
        if self.turn:
            self.direction *= -1
            self.velocity.y = ROW_JUMP_SIZE
            self.turn = False
        else:
            self.velocity.y = 0
        self.velocity.x = ENEMY_SPEED * self.direction
