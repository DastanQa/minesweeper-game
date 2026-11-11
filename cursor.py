# cursor.py: таңдалған ұяшықты стрелкалармен жылжытады
import pygame

from settings import SIZE


class Cursor:
    def __init__(self):
        self.row = 0
        self.col = 0

    def move(self, key):
        if key == pygame.K_UP and self.row > 0:
            self.row = self.row - 1
        if key == pygame.K_DOWN and self.row < SIZE - 1:
            self.row = self.row + 1
        if key == pygame.K_LEFT and self.col > 0:
            self.col = self.col - 1
        if key == pygame.K_RIGHT and self.col < SIZE - 1:
            self.col = self.col + 1

    def is_on(self, cell):
        return cell.row == self.row and cell.col == self.col
