# cell.py: ұяшық. GameObject-тің еншілес класы, SafeCell мен MineCell-дің ата-анасы
from game_object import GameObject
from settings import CELL, load_image


class Cell(GameObject):
    def __init__(self, row, col):
        self.closed_image = load_image("closed.png", (CELL - 2, CELL - 2))
        self.flag_image = load_image("flag.png", (CELL - 2, CELL - 2))
        super().__init__(self.closed_image, row, col)
        self.is_open = False
        self.flagged = False

    def reveal(self, game):
        # ұяшықты ашады; еншілес кластар қайта анықтайды
        self.is_open = True

    def toggle_flag(self, game):
        # жалауды қояды немесе алады
        self.flagged = not self.flagged
        if self.flagged:
            self.image = self.flag_image
            game.flags = game.flags + 1
        else:
            self.image = self.closed_image
            game.flags = game.flags - 1
        game.flag_sound.play()

    def on_game_over(self):
        # ойын біткенде шақырылады; MineCell қайта анықтайды
        pass
