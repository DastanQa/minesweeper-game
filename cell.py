# cell.py: ұяшық (GameObject-тің еншілес класы, SafeCell мен MineCell-дің ата-анасы)
import pygame

from game_object import GameObject


class Cell(GameObject):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.is_open = False

    def draw(self, screen, font):
        pygame.draw.rect(screen, (110, 110, 140), self.rect)

    def reveal(self, game):
        self.is_open = True

    def on_game_over(self):
        pass
