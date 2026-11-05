# board.py
import random
from settings import SIZE, MINES
from cell import Cell
from mine import Mine


class Board:
    """Поле: клетки и мины."""

    def __init__(self):
        self.cells = []
        for r in range(SIZE):
            line = []
            for c in range(SIZE):
                line.append(Cell(r, c))
            self.cells.append(line)
        self.mines = []
        self.place_mines()
        self.count_neighbours()

    def place_mines(self):
        while len(self.mines) < MINES:
            r = random.randint(0, SIZE - 1)
            c = random.randint(0, SIZE - 1)
            if not self.cells[r][c].has_mine:
                self.cells[r][c].has_mine = True
                self.mines.append(Mine(r, c))

    def count_neighbours(self):
        for r in range(SIZE):
            for c in range(SIZE):
                total = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == 0 and dc == 0:
                            continue
                        nr = r + dr
                        nc = c + dc
                        # проверяем, что не вышли за края поля
                        if nr >= 0 and nr < SIZE and nc >= 0 and nc < SIZE:
                            if self.cells[nr][nc].has_mine:
                                total += 1
                self.cells[r][c].count = total

    def show(self, show_mines):
        print()
        header = "   "
        for c in range(SIZE):
            header = header + str(c + 1) + " "
        print(header)
        for r in range(SIZE):
            line = str(r + 1) + "  "
            for c in range(SIZE):
                line = line + self.cells[r][c].symbol(show_mines) + " "
            print(line)
        print()
