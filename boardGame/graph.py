import heapq
import numpy as np
import pygame

class Graph:
    def __init__(self, width, height, matrix):
        self.width = width
        self.height = height
        self.matrix = matrix

    def update_graph_matrix(self, changes):
        for change in changes:
            row, col, value = change
            self.matrix[row][col] = value    

    def get_neighbors(self, pos, visited):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            new_x, new_y = pos[0] + dx, pos[1] + dy
            if (0 <= new_x  and 0 <= new_y and 
                    self.matrix[new_x][new_y] == 2 and (new_x, new_y) not in visited):
                neighbors.append((new_x, new_y))
        return neighbors

    def a_star(self, start, end):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {(x, y): float("inf") for x in range(self.height) for y in range(self.width)}  # Inicjalizacja g_score dla wszystkich węzłów
        g_score[start] = 0
        f_score = {(x, y): float("inf") for x in range(self.height) for y in range(self.width)}
        f_score[start] = heuristic(start, end)

        while open_set:
            current = heapq.heappop(open_set)[1]
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for neighbor in self.get_neighbors(current, set()):  # Przekazanie pustego zbioru jako argument 'visited'
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score.get(neighbor, float("inf")):  # Sprawdzanie, czy neighbor istnieje w g_score
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])