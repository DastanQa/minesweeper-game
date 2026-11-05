# player.py
from settings import SIZE


class Player:
    """Игрок: вводит ход и считает открытые клетки."""

    def __init__(self):
        self.opened = 0

    def ask_move(self):
        while True:
            text = input("Строка и столбец через пробел (например: 3 5): ")
            parts = text.split()
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                row = int(parts[0]) - 1
                col = int(parts[1]) - 1
                if row >= 0 and row < SIZE and col >= 0 and col < SIZE:
                    return row, col
            print("Неверный ввод, попробуйте ещё раз.")
