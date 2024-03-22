import pygame

class Asteroid():

    def __init__(self, position, speed, path) -> None:
        self.position = position
        self.speed = speed
        self.img = pygame.image.load(path)
    
    def update_position(self):
        self.position += self.speed

    def draw_aseroid(self, win):
        win.blit(self.img, self.position)