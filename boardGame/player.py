from typing import Any
import pygame, math
from pygame.math import Vector2
from board_map import board_map
from collections import deque
from graph import Graph

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((0,0,180))
        self.rect = self.image.get_rect()
        self.pose = pygame.math.Vector2(x,y)
        self.rect.center = self.pose
        self.dest_pos = pygame.math.Vector2(x,y)
        self.global_offset = pygame.math.Vector2(0,0)
        self.current_map_pos = (1,1)
        self.dest_map_pos = (1,1)
        self.path = []
        self.graph = Graph(board_map.shape[0], board_map.shape[1], board_map)

    def update(self, offset) -> None:
        self.pose += self.move_to()
        if offset.x != 0 or offset.y != 0:
            self.pose += offset
            self.dest_pos += offset
        self.rect.center = self.pose

    def move_to(self):
        dx = self.dest_pos.x - self.rect.centerx
        dy = self.dest_pos.y - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:
            dx /= distance
            dy /= distance
            speed = 2
            return Vector2(dx * speed, dy * speed)
        elif distance < 0.1 and len(self.path) > 0:
            temp_path = self.path.pop(0)
            self.current_map_pos = temp_path
            print("pobieram kolejną współrzędną {}".format(temp_path))
            self.get_pos_from_map(temp_path[0], temp_path[1])
        return Vector2(0,0)

    def move(self, row, coll):
        # określenie pozycji pod względem kolumny i wiersza z mapy 
        if board_map[row, coll] == 2:
            self.dest_map_pos = (row, coll)
            print("aktualna pozycja {}".format(self.current_map_pos))
            # wywołanie algorytmu do poszukiwania drogi
            # wywołanie algorytmu BFS
            self.path = self.bfs_algorithm(self.current_map_pos, self.dest_map_pos)
            # wywołanie algorytmu A*
            # self.path = self.graph.a_star(self.current_map_pos, self.dest_map_pos)
            print("obliczona ścieżka")
            print(self.path)
        else:
            print("nie dozowlone miejsce")

    def get_pos_from_map(self, row, coll):
        print("wskazuje kolejną pozycję do przejścia")
        self.dest_pos.x = coll * 30 + 15
        self.dest_pos.y = row * 30 + 15
        self.dest_pos += self.global_offset

    # algorytmy do poszukiwania drogi 
    # dla obydwu algorytmów zakładam że działąm na tablei i do player-a dodaje dwie
    # dodatkowe zmienne:
    # current_map_pos - określa aktualną pozucję gracza na mapie
    # dest_map_pos - określa miejsce docelowe gracza 
    
    # algorytm BFS

    def bfs_algorithm(self, start, end):
        map_size = board_map.shape
        direction = [ (-1,0), (1,0), (0,-1), (0,1) ] #wskazanie kierunków do poszukiwania drogi
        queue = deque([start])  # Kolejka wierzchołków do odwiedzenia, wraz z ich ścieżką
        visited = set()
        visited.add(start)
        parent = {start: None}

        while queue:
            current = queue.popleft()

            if current == end:  # Jeśli znaleziono wierzchołek końcowy
                break 
            for direct in direction:
                neighbor = (current[0] + direct[0], current[1] + direct[1])
                if (0<= current[0] < map_size[0] and 0<= current[1] < map_size[1] and
                    board_map[current[0], current[1]] == 2 and neighbor not in visited) :
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
                
        path = []
        step = end
        while step is not None:
            path.append(step)
            step = parent[step]
        path.reverse()
        return path

    # algorytm A*
    # szczegóły implementacji znajdują się w pliku graph.py

