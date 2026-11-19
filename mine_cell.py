# mine_cell.py: миналы ұяшық
import pygame

from cell import Cell
from settings import CELL, load_image


class MineCell(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.exploded = False  # ойыншы дәл осы минаны басты ма
        self.frames = []
        for i in range(4):
            self.frames.append(load_image(f"mine_{i}.png", (CELL - 2, CELL - 2)))
        self.boom_image = load_image("mine_boom.png", (CELL - 2, CELL - 2))
        self.frame = 0
        self.last_switch = pygame.time.get_ticks()

    def reveal(self, game):
        super().reveal(game)
        self.exploded = True
        self.image = self.boom_image
        game.lose(self)

    def on_game_over(self):
        self.is_open = True  # ойын біткенде барлық мина көрінеді

    def update(self):
        # ашылған мина анимацияланады: төрт кадр кезекпен ауысады
        if self.is_open and not self.exploded:
            now = pygame.time.get_ticks()
            if now - self.last_switch > 150:
                self.frame = (self.frame + 1) % len(self.frames)
                self.image = self.frames[self.frame]
                self.last_switch = now
