# safe_cell.py: қауіпсіз ұяшық
import pygame

from cell import Cell
from settings import NUM_COLORS, POINTS


class SafeCell(Cell):
    def __init__(self, row, col, count):
        super().__init__(row, col)
        self.count = count  # айналасында қанша мина бар

    def draw(self, screen, font):
        if self.is_open:
            pygame.draw.rect(screen, (205, 205, 215), self.rect)
            if self.count > 0:
                text = font.render(f"{self.count}", True, NUM_COLORS[self.count])
                screen.blit(text, (self.rect.x + 17, self.rect.y + 8))
        else:
            super().draw(screen, font)

    def reveal(self, game):
        super().reveal(game)
        game.opened = game.opened + 1
        game.score = game.score + POINTS
