import pygame, os

class Ship:

    def __init__(self, position, speed) -> None:
        self.position = position
        self.speed = speed
        self.size = None
        self.img = None
    
    def update_position(self, win_w, win_h):
        if (self.position.x + self.size.width) > win_w or self.position.x < 0:
            self.speed.x *= -1
        if (self.position.y + self.size.height) > win_h or self.position.y < 0:
            self.speed.y *= -1
        self.position += (self.speed * 0.5)

    def draw_ship(self, win):
        win.blit(self.img, self.position)