import pygame
from pygame import Vector2

from constants import ROW_JUMP_SIZE, ENEMY_SPEED
from game_object import GameObject

# Enemies will be positioned in a grid layout where the enemy will spawn at random in any one of these grid
# squares

class Enemy(GameObject):
    turn = False            # Tells whether enemy needs to turn or not
    jump = False
    direction = 1

    def __init__(self, coords):
        super().__init__() 
        self.position = coords # The coords will be generated from an outer function
        self.WIDTH = 20

        # Velocity of enemy remains constant? Or should we make it speed up and slow down at certain areas?
        self.velocity.x = ENEMY_SPEED

    def update(self, delta, events):
        if self.jump:
            self.velocity.x = 0
            self.velocity.y = ROW_JUMP_SIZE
        elif self.turn:
            self.velocity.x = ENEMY_SPEED
            self.velocity.y = 0
            self.velocity *= self.direction
            self.turn = False

        super().update(delta, None)
        self.move_towards_player()
    
    def move_towards_player(self):
        if self.jump:
            self.jump = False
            self.turn = True
        elif self.boundary_check():
            self.direction *= -1
            self.jump = True

    def render(self, display):
        # Arguments (pygame.Surface, (RGB), position, radius)
        pygame.draw.circle(display, (0, 0, 255), self.position, self.WIDTH / 2)
