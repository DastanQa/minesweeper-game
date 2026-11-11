# cell.py: ата-ана класы, барлық ұяшыққа ортақ бөлік
import pygame

from settings import CELL, TOP


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.rect = pygame.Rect(col * CELL, TOP + row * CELL, CELL - 2, CELL - 2)
        self.is_open = False

    def draw(self, screen, font, selected):
        color = (110, 110, 140)
        if selected:
            color = (165, 165, 205)
        pygame.draw.rect(screen, color, self.rect)

    def reveal(self, game):
        self.is_open = True

    def on_game_over(self):
        pass
