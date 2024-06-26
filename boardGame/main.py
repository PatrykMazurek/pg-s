import pygame, os, random
import numpy as np
from board_game_map import *
from board_map import *
from player import Player
from enemy import Enemy
from object_map import ObjectMap

BLACK = (0,0,0)
FPS = 60
WIDTH, HEIGHT = 800, 650

pygame.display.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("board Game")
clock = pygame.time.Clock()
run = True
offset = pygame.math.Vector2(0,0)
maps = BoardMap()

def draw_window(win, board_grup, player, enemy_group, object_group):
    win.fill(BLACK)
    board_grup.draw(win)
    enemy_group.draw(win)
    object_group.draw(win)
    win.blit(player.image, player.rect)
    pygame.display.update()

board_wall = pygame.sprite.Group()
col, row = board_map.shape
for r in range(row):
    for c in range(col):
        if board_map[c,r] != 0:
            board_wall.add(BoardTile(board_map[c,r], r, c))

player = Player(45,45)
# player_g = pygame.sprite.Group()
# player_g.add(player)
all_object = pygame.sprite.Group()
all_object.add(ObjectMap("coin", 4,5, player, None))
all_object.add(ObjectMap("box", 6,5, player, 1))
all_object.add(ObjectMap("task", 9,5, player, 1))

all_enemies = pygame.sprite.Group()
all_enemies.add(Enemy(player, 4,5))
all_enemies.add(Enemy(player, 9,9))

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                current_cursor_pos = pygame.mouse.get_pos() - player.global_offset
                row, coll, _ = maps.get_element_from_table(pygame.math.Vector2(current_cursor_pos))
                player.move(row, coll)
            if event.button == 3:
                print("kilknięto prawy przycisk myszy")

    offset = maps.determine_offset(pygame.mouse.get_pos(), WIDTH, HEIGHT)
    player.global_offset += offset
    board_wall.update(offset)
    player.update(offset)
    all_enemies.update(offset)
    all_object.update(offset)

    draw_window(win, board_wall, player, all_enemies, all_object)

pygame.quit()