# game.py
from board import Board
from player import Player
from timer import Timer
from settings import SIZE, MINES


class Game:
    """Игра: связывает все объекты и решает, выиграл игрок или проиграл."""

    def __init__(self):
        self.board = Board()
        self.player = Player()
        self.timer = Timer()
        self.finished = False
        self.won = False

    def play(self):
        print("САПЁР", SIZE, "x", SIZE, ", мин:", MINES)
        self.timer.start()
        while not self.finished:
            self.board.show(False)
            print("Время:", self.timer.elapsed(), "сек")
            row, col = self.player.ask_move()
            cell = self.board.cells[row][col]
            if cell.is_open:
                print("Эта клетка уже открыта.")
                continue
            cell.open()
            if cell.has_mine:
                self.finished = True
                self.won = False
            else:
                self.player.opened += 1
                if self.player.opened == SIZE * SIZE - MINES:
                    self.finished = True
                    self.won = True
        self.end()

    def end(self):
        self.board.show(True)
        if self.won:
            print("Вы выиграли!")
        else:
            print("Вы наступили на мину. Игра окончена.")
        print("Время:", self.timer.elapsed(), "сек")
