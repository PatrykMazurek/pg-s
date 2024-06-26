import pygame

class Laser:
    def __init__(self, pos, speed) -> None:
        self.position = pos
        self.img = pygame.Surface((4, 8))
        self.img.fill((0, 255, 0))
        self.speed = speed
        self.point = 10

    def update(self):
        self.position += self.speed

    def draw_laser(self, win):
        win.blit(self.img, self.position)
        
        