import pygame

class SpriteSheet():
    def __init__(self, image, row, cell, step, width, height):
        self.sheet = image
        self.rect = pygame.math.Vector2(self.get_pos(row, cell))
        self.list_img = []
        for x in range(step):
            self.list_img.append(self.cut_image(x, width, height, 1 ))
        self.frame = 0

    def cut_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width* scale, height*scale))
        image.set_colorkey()
        return image
    
    def get_image(self):
        return self.list_img[self.frame]
    
    def get_pos(self, row, cell):
        temp_pos = pygame.math.Vector2([0,0])
        temp_pos.x = cell * 32 + 16
        temp_pos.y = row * 32 + 16
        return temp_pos
    
    def update(self, offset) -> None:
        self.rect.x += offset.x
        self.rect.y += offset.y