import pygame, random, os
from pygame.math import Vector2


class Item(pygame.sprite.Sprite):

    def __init__(self, name, nr, type, row, cell) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.type = type
        self.nr = nr
                # zakładame że mamy do dyspozycji skrzynki, pytajniki z zadaniami, monety
        if type == "box":
            # skrzynka, która może zawierać jakieś przedmoity
            file_name = random.choice(["box_1.png", "box_2.png", "box_3.png"])
        elif type == "task":
            # pytajnik z zadaniem
            file_name = random.choice(["task_1.png", "task_2.png"])
            
        else:
            # moneta
            file_name = random.choice(["coin_1.png", "coin_2.png"]) 
        self.image = pygame.image.load(os.path.join("boardGame","assets", "objects", file_name))
        self.rect = self.image.get_rect()
        self.pos = Vector2(self.get_pos(row, cell))
        self.rect.center = self.pos

    def update(self, offset) -> None:
        self.rect.x += offset.x
        self.rect.y += offset.y

    def get_pos(self, row, cell):
        temp_pos = pygame.math.Vector2([0,0])
        temp_pos.x = cell * 30 + 15
        temp_pos.y = row * 30 + 15
        temp_pos += self.player.global_offset
        return temp_pos
    
