# settings.py: ортақ баптаулар және суретті, дыбысты, қаріпті жүктейтін функциялар
import os

import pygame

WIDTH, HEIGHT = 480, 560
SIZE = 8          # алаң 8x8
MINES = 10        # мина саны
CELL = 56         # бір ұяшықтың қадамы (сурет 2 пиксель кіші: ұяшықтар арасында саңылау бар)
LEFT = 16         # алаңның сол жақ шеті
TOP = 96          # жоғарғы жолақтың биіктігі

POINTS = 10       # әр қауіпсіз ұяшық үшін ұпай
WIN_BONUS = 200   # жеңіс үшін қосымша ұпай
END_DELAY = 90    # жеңістен/жеңілістен кейін алаңды көрсету кадрлары (1,5 секунд)

BG_COLOR = (15, 15, 35)
ASSETS = os.path.join(os.path.dirname(__file__), "assets")


def load_image(name, size):
    path = os.path.join(ASSETS, name)
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, size)


def load_sound(name):
    path = os.path.join(ASSETS, name)
    return pygame.mixer.Sound(path)


def load_font(name, size):
    path = os.path.join(ASSETS, name)
    return pygame.font.Font(path, size)
