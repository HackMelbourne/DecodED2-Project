import abc  # Stands for Abstract Base Classes
from src.constants import SCREEN_W

import pygame
from pygame import Vector2


# TODO should we teach these concepts? Or stick to vanilla python?
# If not we can use pure python with no abc/other libs other than pygame


class Entity:
    position: Vector2
    velocity: Vector2
    width: int
    height: int
    image: pygame.Surface
    rect: pygame.Rect
    # Whether this object should be removed next game loop
    expired = False

    # Could have acceleration but we won't have complex motion here.
    def __init__(self, width: int, height: int, sprite_img: str):
        self.width = width
        self.height = height
        self.position = Vector2()
        self.velocity = Vector2()
        # Sprite and collision
        self.image = pygame.transform.smoothscale(pygame.image.load(sprite_img), (width, height))
        self.rect = pygame.rect.Rect(0, 0, width, height)

    def boundary_check(self):
        """
        Teleports the object back into the screen if they go outside.
        :return true if the user was outside and teleported, false otherwise
        """
        if self.position.x < self.width / 2:
            self.position.x = self.width / 2
            return True

        elif self.position.x > SCREEN_W - self.width / 2:
            self.position.x = SCREEN_W - self.width / 2
            return True

        return False

    # objects is a list of all objects in the game (can't type since we have to refer to this class,
    # and plan to remove types when development finishes
    def update(self, delta: int, objects):
        """
        Update this object

        delta=the time since the last frame draw, used to ensure objects animate at the correct speed,
        regardless of FPS count. (aka runs the same on a potato, or a supercomputer. Only difference will be framerate)

        """
        # Position
        self.position += delta * self.velocity
        # Collision helper with rect
        self.rect.update(self.position.x - self.width / 2, self.position.y - self.height / 2, self.width, self.height)

    def render(self, display: pygame.Surface):
        display.blit(self.image, (self.position.x - self.width / 2, self.position.y - self.height / 2))
