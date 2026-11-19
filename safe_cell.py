# safe_cell.py: қауіпсіз ұяшық
from cell import Cell
from particle import Particle
from settings import CELL, POINTS, load_image


class SafeCell(Cell):
    def __init__(self, row, col, count):
        super().__init__(row, col)
        self.count = count  # айналасында қанша мина бар
        self.open_image = load_image(f"open_{count}.png", (CELL - 2, CELL - 2))

    def reveal(self, game):
        super().reveal(game)
        self.image = self.open_image
        game.opened = game.opened + 1
        game.score = game.score + POINTS
        game.open_sound.play()
        for i in range(3):
            game.effects.add(Particle(self.rect.center, (150, 190, 255)))
        if self.is_empty():
            game.waiting.append(self)  # айналасын Game ашады

    def is_empty(self):
        # айналасында мина жоқ ұяшық па
        return self.count == 0
