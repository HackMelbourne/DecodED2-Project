import pygame
from pygame import Vector2

from constants import ROW_JUMP_SIZE
from game_object import GameObject

# Enemies will be positioned in a grid layout where the enemy will spawn at random in any one of these grid
# squares

class Enemy(GameObject):
    direction = 1       # Positive to move right and negative to move left

    def __init__(self, coords):
        super.__init__()
        self.position = coords      # The coords will be generated from an outer function
        self.WIDTH = 30

        # Velocity of enemy remains constant? Or should we make it speed up and slow down at certain areas?
        self.velocity.x = 5

    def update(self, delta):
        super().update(delta, None)
        self.move_towards_player()
    
    def move_towards_player(self):
        if self.boundary_check():
            self.position.y += ROW_JUMP_SIZE
            self.velocity.x *= -1

    def render(self, display):
        # Arguments (pygame.Surface, (RGB), position, radius)
        pygame.draw.circle(display, (0, 0, 255), self.position, self.WIDTH / 2)
