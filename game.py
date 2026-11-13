# game.py: ортақ класс, үш экранды (start, play, end) басқарады
import pygame

from board import Board
from cursor import Cursor
from settings import SIZE, MINES, WIDTH, HEIGHT, WIN_BONUS, END_DELAY
from timer import Timer


class Game:
    def __init__(self):
        self.board = Board()
        self.cells = self.board.cells
        self.cursor = Cursor()
        self.objects = []  # түрлі класс объектілері бір тізімде
        for cell in self.cells:
            self.objects.append(cell)
        self.objects.append(self.cursor)
        self.timer = Timer()
        self.state = "start"  # start, play, end
        self.opened = 0
        self.score = 0
        self.over = False
        self.won = False
        self.pause = 0

    def lose(self):
        self.over = True
        self.won = False
        for cell in self.cells:
            cell.on_game_over()

    def open_cell(self):
        for cell in self.cells:
            if self.cursor.is_on(cell) and not cell.is_open:
                cell.reveal(self)

    def handle_key(self, key):
        if self.state == "start":
            if key == pygame.K_RETURN:
                self.state = "play"
        elif self.state == "play":
            if not self.over:
                self.cursor.move(key)
                if key == pygame.K_SPACE:
                    self.open_cell()

    def update(self):
        if self.state == "play":
            if not self.over:
                self.timer.update()
                for obj in self.objects:
                    obj.update()
                if self.opened == SIZE * SIZE - MINES:
                    self.over = True
                    self.won = True
                    self.score = self.score + WIN_BONUS
            else:
                self.pause = self.pause + 1
                if self.pause >= END_DELAY:
                    self.state = "end"

    def draw_start(self, screen, font, big_font):
        title = big_font.render("САПЁР", True, (255, 210, 60))
        screen.blit(title, (WIDTH // 2 - 100, 70))
        lines = ["Стрелкалар: ұяшықты таңдау", "Space: ұяшықты ашу", "R: қайта бастау",
                 "8×8 алаң, 10 мина"]
        y = 190
        for line in lines:
            text = font.render(line, True, (230, 232, 244))
            screen.blit(text, (30, y))
            y = y + 44
        start = font.render("Бастау: Enter", True, (120, 255, 120))
        screen.blit(start, (30, y + 30))

    def draw_play(self, screen, font):
        time_text = font.render(f"Уақыт: {self.timer.seconds()}", True, (255, 255, 255))
        screen.blit(time_text, (10, 8))
        score_text = font.render(f"Ұпай: {self.score}", True, (255, 210, 60))
        screen.blit(score_text, (WIDTH - 140, 8))
        mines_text = font.render(f"Мина: {MINES}", True, (255, 120, 120))
        screen.blit(mines_text, (10, 38))
        for obj in self.objects:
            obj.draw(screen, font)

    def draw_end(self, screen, font, big_font):
        if self.won:
            title = big_font.render("Жеңдіңіз!", True, (120, 255, 120))
        else:
            title = big_font.render("Жеңілдіңіз!", True, (255, 120, 120))
        screen.blit(title, (30, 70))
        score_text = font.render(f"Қорытынды ұпай: {self.score}", True, (255, 210, 60))
        screen.blit(score_text, (30, 190))
        time_text = font.render(f"Уақыт: {self.timer.seconds()} с", True, (230, 232, 244))
        screen.blit(time_text, (30, 234))
        again = font.render("Қайта бастау: R", True, (120, 255, 120))
        screen.blit(again, (30, 310))

    def draw(self, screen, font, big_font):
        screen.fill((15, 15, 35))
        if self.state == "start":
            self.draw_start(screen, font, big_font)
        elif self.state == "play":
            self.draw_play(screen, font)
        else:
            self.draw_end(screen, font, big_font)
