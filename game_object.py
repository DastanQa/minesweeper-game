# game_object.py: ата-ана класы, ойындағы барлық объектіге ортақ
import pygame

from settings import CELL, TOP


class GameObject:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.rect = pygame.Rect(col * CELL, TOP + row * CELL, CELL - 2, CELL - 2)

    def set_place(self, row, col):
        self.row = row
        self.col = col
        self.rect = pygame.Rect(col * CELL, TOP + row * CELL, CELL - 2, CELL - 2)

    def draw(self, screen, font):
        pass

    def update(self):
        pass
