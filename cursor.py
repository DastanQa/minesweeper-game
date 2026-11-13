# cursor.py: таңдалған ұяшықты көрсететін жақтау
import pygame

from game_object import GameObject
from settings import SIZE, CELL


class Cursor(GameObject):
    def __init__(self):
        super().__init__(0, 0)

    def move(self, key):
        if key == pygame.K_UP and self.row > 0:
            self.set_place(self.row - 1, self.col)
        if key == pygame.K_DOWN and self.row < SIZE - 1:
            self.set_place(self.row + 1, self.col)
        if key == pygame.K_LEFT and self.col > 0:
            self.set_place(self.row, self.col - 1)
        if key == pygame.K_RIGHT and self.col < SIZE - 1:
            self.set_place(self.row, self.col + 1)

    def is_on(self, cell):
        return cell.row == self.row and cell.col == self.col

    def draw(self, screen, font):
        color = (255, 210, 60)
        x = self.rect.x
        y = self.rect.y
        size = CELL - 2
        pygame.draw.rect(screen, color, pygame.Rect(x, y, size, 4))
        pygame.draw.rect(screen, color, pygame.Rect(x, y + size - 4, size, 4))
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 4, size))
        pygame.draw.rect(screen, color, pygame.Rect(x + size - 4, y, 4, size))
