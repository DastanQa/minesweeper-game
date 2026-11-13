# mine_cell.py: миналы ұяшық
import pygame

from cell import Cell


class MineCell(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.exploded = False  # ойыншы дәл осы минаны басты ма

    def draw(self, screen, font):
        if self.is_open:
            color = (150, 70, 70)
            if self.exploded:
                color = (230, 50, 50)
            pygame.draw.rect(screen, color, self.rect)
            pygame.draw.circle(screen, (30, 30, 30), self.rect.center, 10)
        else:
            super().draw(screen, font)

    def reveal(self, game):
        super().reveal(game)
        self.exploded = True
        game.lose()

    def on_game_over(self):
        self.is_open = True
