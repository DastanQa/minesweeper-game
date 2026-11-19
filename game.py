# game.py: командаға ортақ класс. Алаңды, үш экранды (start, play, over) және ойын ережесін басқарады
import random

import pygame

from cursor import Cursor
from mine_cell import MineCell
from particle import Particle
from safe_cell import SafeCell
from settings import (WIDTH, HEIGHT, SIZE, MINES, WIN_BONUS, END_DELAY, BG_COLOR,
                      load_image, load_sound)


class Game:
    def __init__(self):
        self.cursor = Cursor()
        self.cells = pygame.sprite.Group()    # тек ұяшықтар: курсормен соқтығысуды тексеру үшін
        self.objects = pygame.sprite.Group()  # ұяшықтар мен курсор: түрлі класс бір топта
        self.effects = pygame.sprite.Group()  # бөлшектер
        self.cell_list = []                   # ұяшықтар қатар-қатарымен
        self.mine_spots = []                  # миналар тұрған орындар (қатар, баған)
        self.waiting = []                     # айналасын ашу керек бос ұяшықтар
        self.open_sound = load_sound("open.wav")
        self.flag_sound = load_sound("flag.wav")
        self.boom_sound = load_sound("boom.wav")
        self.win_sound = load_sound("win.wav")
        self.lose_sound = load_sound("lose.wav")
        self.menu_image = load_image("mine_big.png", (96, 96))
        self.canvas = pygame.Surface((WIDTH, HEIGHT))
        self.state = "start"  # start, play, over
        self.quit = False
        self.new_round()

    # ---------- алаңды дайындау ----------
    def new_round(self):
        self.cursor.set_place(0, 0)
        self.mine_spots = []
        while len(self.mine_spots) < MINES:
            spot = (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))
            used = spot in self.mine_spots
            if not used:
                self.mine_spots.append(spot)
        self.build_cells()
        self.effects.empty()
        self.waiting = []
        self.score = 0
        self.opened = 0
        self.flags = 0
        self.seconds = 0
        self.start_ticks = 0
        self.first_move = True
        self.result = ""  # "" - ойын жүріп жатыр, "win" немесе "lose"
        self.end_timer = 0
        self.shake = 0

    def build_cells(self):
        self.cells.empty()
        self.objects.empty()
        self.cell_list = []
        for row in range(SIZE):
            for col in range(SIZE):
                if (row, col) in self.mine_spots:
                    cell = MineCell(row, col)
                else:
                    cell = SafeCell(row, col, self.count_around(row, col))
                self.cell_list.append(cell)
                self.cells.add(cell)
                self.objects.add(cell)
        self.objects.add(self.cursor)  # курсор соңынан қосылады: ұяшықтардың үстінен салынады

    def count_around(self, row, col):
        count = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if (row + dr, col + dc) in self.mine_spots:
                    count = count + 1
        return count

    def neighbours(self, cell):
        result = []
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                r = cell.row + dr
                c = cell.col + dc
                inside = r >= 0 and r < SIZE and c >= 0 and c < SIZE
                if inside and (dr != 0 or dc != 0):
                    result.append(self.cell_list[r * SIZE + c])
        return result

    def move_mine_away(self, row, col):
        # бірінші басылған ұяшықта мина болса, миананы басқа орынға көшіреміз
        self.mine_spots.remove((row, col))
        placed = False
        while not placed:
            spot = (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))
            used = spot in self.mine_spots
            if not used and spot != (row, col):
                self.mine_spots.append(spot)
                placed = True
        self.build_cells()

    # ---------- ойын ережесі ----------
    def open_cell(self):
        cell = self.cursor.find_cell(self.cells)
        if cell.is_open or cell.flagged:
            return
        if self.first_move:
            self.first_move = False
            self.start_ticks = pygame.time.get_ticks()
            if (cell.row, cell.col) in self.mine_spots:
                self.move_mine_away(cell.row, cell.col)
                cell = self.cursor.find_cell(self.cells)
        cell.reveal(self)
        self.spread()
        self.check_win()

    def spread(self):
        # бос ұяшықтың айналасын ашады; жаңа бос ұяшықтар тізімге түсе береді
        while len(self.waiting) > 0:
            cell = self.waiting[0]
            self.waiting.remove(cell)
            for near in self.neighbours(cell):
                if not near.is_open and not near.flagged:
                    near.reveal(self)

    def toggle_flag(self):
        if self.first_move:
            return
        cell = self.cursor.find_cell(self.cells)
        if not cell.is_open:
            cell.toggle_flag(self)

    def lose(self, cell):
        self.result = "lose"
        self.boom_sound.play()
        self.shake = 25
        for i in range(40):
            self.effects.add(Particle(cell.rect.center, (255, 150, 30)))
        for obj in self.cells:
            obj.on_game_over()

    def check_win(self):
        if self.result == "" and self.opened == SIZE * SIZE - MINES:
            self.result = "win"
            self.score = self.score + WIN_BONUS
            self.win_sound.play()
            for obj in self.cells:
                obj.on_game_over()

    # ---------- перне және жаңарту ----------
    def handle_key(self, key):
        if key == pygame.K_r and self.state != "start":
            self.new_round()
            self.state = "play"
        elif self.state == "start":
            if key == pygame.K_RETURN:
                self.state = "play"
            if key == pygame.K_ESCAPE:
                self.quit = True
        elif self.state == "play":
            if self.result == "":
                self.cursor.move(key)
                if key == pygame.K_SPACE:
                    self.open_cell()
                if key == pygame.K_f:
                    self.toggle_flag()
            if key == pygame.K_ESCAPE:
                self.new_round()
                self.state = "start"
        else:
            if key == pygame.K_ESCAPE:
                self.quit = True

    def update(self):
        if self.state != "play":
            return
        self.objects.update()
        self.effects.update()
        if self.shake > 0:
            self.shake = self.shake - 1
        if self.result == "":
            if not self.first_move:
                self.seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        else:
            self.end_timer = self.end_timer + 1
            if self.end_timer >= END_DELAY:
                self.state = "over"
                if self.result == "lose":
                    self.lose_sound.play()

    # ---------- экрандар ----------
    def draw_text(self, screen, font, text, y, color):
        image = font.render(text, True, color)
        screen.blit(image, image.get_rect(center=(WIDTH // 2, y)))

    def draw_start(self, screen, font, big_font):
        screen.blit(self.menu_image, self.menu_image.get_rect(center=(WIDTH // 2, 100)))
        self.draw_text(screen, big_font, "САПЁР", 190, (255, 210, 60))
        lines = ["Жебелер: ұяшықты таңдау", "Space: ұяшықты ашу", "F: жалау қою / алу",
                 "R: қайта бастау", "8×8 алаң, 10 мина"]
        y = 262
        for line in lines:
            self.draw_text(screen, font, line, y, (230, 232, 244))
            y = y + 34
        self.draw_text(screen, font, "Бастау: Enter", 460, (120, 255, 120))
        self.draw_text(screen, font, "Шығу: Esc", 500, (160, 160, 180))

    def draw_play(self, screen, font):
        self.canvas.fill(BG_COLOR)
        time_text = font.render(f"Уақыт: {self.seconds}", True, (255, 255, 255))
        self.canvas.blit(time_text, (16, 14))
        score_text = font.render(f"Ұпай: {self.score}", True, (255, 210, 60))
        self.canvas.blit(score_text, score_text.get_rect(topright=(WIDTH - 16, 14)))
        mines_text = font.render(f"Мина: {MINES - self.flags}", True, (255, 130, 130))
        self.canvas.blit(mines_text, (16, 52))
        self.objects.draw(self.canvas)
        self.effects.draw(self.canvas)
        dx = 0
        dy = 0
        if self.shake > 0:
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
        screen.blit(self.canvas, (dx, dy))

    def draw_end(self, screen, font, big_font):
        if self.result == "win":
            self.draw_text(screen, big_font, "Жеңдіңіз!", 130, (120, 255, 120))
        else:
            self.draw_text(screen, big_font, "Жеңілдіңіз!", 130, (255, 120, 120))
        self.draw_text(screen, font, f"Қорытынды ұпай: {self.score}", 250, (255, 210, 60))
        self.draw_text(screen, font, f"Уақыт: {self.seconds} с", 295, (230, 232, 244))
        self.draw_text(screen, font, "Қайта бастау: R", 390, (120, 255, 120))
        self.draw_text(screen, font, "Шығу: Esc", 430, (160, 160, 180))

    def draw(self, screen, font, big_font):
        screen.fill(BG_COLOR)
        if self.state == "start":
            self.draw_start(screen, font, big_font)
        elif self.state == "play":
            self.draw_play(screen, font)
        else:
            self.draw_end(screen, font, big_font)
