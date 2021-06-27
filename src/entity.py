from src.constants import SCREEN_W

import pygame
from pygame import Vector2


# TODO should we teach these concepts? Or stick to vanilla python?
# If not we can use pure python with no abc/other libs other than pygame


class Entity(pygame.Rect):
    position: Vector2
    velocity: Vector2
    width: int
    height: int
    image: pygame.Surface
    
    # Could have acceleration but we won't have complex motion here.
    def __init__(self, x: int, y: int, width: int, height: int, sprite_img: str):
        super().__init__(x, y, width, height)
        self.velocity = Vector2()

        # Whether this object should be removed next game loop
        self.expired = False

        # Sprite
        self.image = pygame.transform.smoothscale(pygame.image.load(sprite_img), (width, height))

    def kill(self):
        """
        Expire the entity so it is removed from the world at the next game tick
        """
        self.expired = True

    def boundary_check(self):
        """
        Teleports the object back into the screen if they go outside.
        :return true if the user was outside and teleported, false otherwise
        """
        if self.x < self.width / 2:
            self.x = self.width / 2
            return True

        elif self.x > SCREEN_W - self.width / 2:
            self.x = SCREEN_W - self.width / 2
            return True

        return False

    def tick(self, delta: int, objects):
        """
        Game logic specific to the entity
        """
        pass

    def move(self, delta: int):
        """
        Move this entity according to the delta parameter

        delta=the time since the last frame draw, used to ensure objects animate at the correct speed,
        regardless of FPS count. (aka runs the same on a potato, or a supercomputer. Only difference will be framerate)

        """
        self.update(
            self.x + self.velocity.x * delta, 
            self.y + self.velocity.y * delta, 
            self.width, 
            self.height
        )

    def render(self, display: pygame.Surface):
        display.blit(self.image, (self.x - self.width / 2, self.y - self.height / 2))
