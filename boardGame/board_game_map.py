import numpy as np
import pygame, os, random

class BoardTile(pygame.sprite.Sprite):
    def __init__(self, type, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        size = (32,32)
        if type == 1:
            self.image = pygame.Surface(size)
            self.image.fill((0,220,0))
        elif type == 2:
            self.image = pygame.image.load(
                os.path.join("BoardGame", "assets", "map",
                    random.choice(["kafel_1.png","kafel_2.png","kafel_3.png"])))
            
            # self.image.fill((220,0,0)) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x *size[0], y* size[1])
        
    def update(self, offset) -> None:
        self.rect.x += offset.x
        self.rect.y += offset.y