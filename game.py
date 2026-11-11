# game.py: ортақ класс, барлық объектіні біріктіреді
import pygame

from board import Board
from cursor import Cursor
from settings import SIZE, MINES, WIDTH
from timer import Timer


class Game:
    def __init__(self):
        self.board = Board()
        self.cells = self.board.cells  # екі түрлі класс объектілері бір тізімде
        self.cursor = Cursor()
        self.timer = Timer()
        self.opened = 0
        self.over = False
        self.won = False

    def lose(self):
        self.over = True
        self.won = False
        for obj in self.cells:
            obj.on_game_over()

    def open_cell(self):
        for obj in self.cells:
            if self.cursor.is_on(obj) and not obj.is_open:
                obj.reveal(self)

    def handle_key(self, key):
        if not self.over:
            self.cursor.move(key)
            if key == pygame.K_SPACE:
                self.open_cell()

    def update(self):
        if not self.over:
            self.timer.update()
            if self.opened == SIZE * SIZE - MINES:
                self.over = True
                self.won = True

    def draw(self, screen, font):
        screen.fill((15, 15, 35))
        time_text = font.render(f"Уақыт: {self.timer.seconds()}", True, (255, 255, 255))
        screen.blit(time_text, (10, 8))
        mines_text = font.render(f"Мина: {MINES}", True, (255, 120, 120))
        screen.blit(mines_text, (WIDTH - 110, 8))
        for obj in self.cells:
            obj.draw(screen, font, self.cursor.is_on(obj))
        if self.over:
            if self.won:
                message = font.render("Жеңдіңіз! Қайта бастау: R", True, (120, 255, 120))
            else:
                message = font.render("Жеңілдіңіз! Қайта бастау: R", True, (255, 120, 120))
            screen.blit(message, (10, 38))
