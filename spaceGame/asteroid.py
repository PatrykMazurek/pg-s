import pygame, random, os

class Asteroid():

    def __init__(self, position) -> None:
        tempTab = ["a10000.png", "a30000.png", "a30013.png"]
        self.position = position
        self.speed = pygame.math.Vector2( random.randint(-3, 3), 3)
        path = random.choice(tempTab)
        self.img = pygame.image.load(os.path.join("assets", path))
    
    def update_position(self):
        self.position += self.speed

    def draw_aseroid(self, win):
        win.blit(self.img, self.position)