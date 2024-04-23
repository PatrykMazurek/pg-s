import pygame, os, random

class Ship:

    def __init__(self, position, speed, enemy) -> None:
        self.position = position
        self.speed = speed
        if enemy:
            enemy_ship = random.choice(['1.png', '1B.png', '6.png', '6B.png', '10.png', '10B.png'])
            self.img = pygame.image.load(os.path.join("assets", enemy_ship))
            self.img = pygame.transform.rotate(self.img, 180)   
        else:
            self.img = pygame.image.load(os.path.join("assets", "ship.png"))
        self.size = self.img.get_rect()
        self.img = pygame.transform.scale(self.img, (self.img.get_width() /2,
                                                    self.img.get_height() /2 ))
        self.lasers = [] 
    
    def update_position(self, win_h, win_w):
        if self.position.x + (self.size.width /2) > win_w or self.position.x < 0:
            self.speed.x *= -1
        if self.position.y + (self.size.height /2) > win_h or self.position.y < 0:
            self.speed.y *= -1
        self.position += self.speed

    def enemy_update_position(self, win_h):
        if self.position.y > win_h:
            return True
        self.position += self.speed
        return False

    def draw_ship(self, win):
        win.blit(self.img, self.position)