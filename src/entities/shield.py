import pygame
from src.entity import Entity
from src.entities.bullet import Bullet

class Shield(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(x - 30, y, 60, 60, 'res/shield-1.png')
        self.hp = 10

    def tick(self, delta: int, objects):
        for obj in objects:
            if isinstance(obj, Bullet) and self.colliderect(obj):
                obj.kill()
                self.hp -= 1
        
        if self.hp <= 0:
            self.kill()
        
        if self.hp < 7:
            self.set_image("res/shield-2.png")
        if self.hp < 4:
            self.set_image("res/shield-3.png")

    def set_image(self, path_to_image):
        self.image = pygame.transform.smoothscale(pygame.image.load(path_to_image), (self.width, self.height))

    
