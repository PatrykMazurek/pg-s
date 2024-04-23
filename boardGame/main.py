import pygame, os, random
import numpy as np
from board_game_map import *
BLACK = (0,0,0)

FPS = 60

WIDTH, HEIGHT = 800, 650

pygame.display.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("board Game")
clock = pygame.time.Clock()
run = True

def draw_window(win, board_grup):
    win.fill(BLACK)
    board_grup.draw(win)
    pygame.display.update()

print(board_map)

board_wall = pygame.sprite.Group()
col, row = board_map.shape
for r in range(row):
    for c in range(col):
        if board_map[c,r] != 0:
            board_wall.add(BoardTile(board_map[c,r], r, c))

print(board_wall)

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_w]:
        board_wall.update(0,1)
    if keyPressed[pygame.K_s]:
        board_wall.update(0,-1)
    if keyPressed[pygame.K_d]:
        board_wall.update(-1,0)
    if keyPressed[pygame.K_a]:
        board_wall.update(1,0)

    draw_window(win, board_wall)

pygame.quit()