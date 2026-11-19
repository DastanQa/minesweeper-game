# main.py: ойын циклі. Ойынды import арқылы жинайды
import pygame

from game import Game
from settings import WIDTH, HEIGHT, load_font


def main(max_frames=None):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Сапёр")
    font = load_font("font.ttf", 24)
    big_font = load_font("font_bold.ttf", 56)
    clock = pygame.time.Clock()
    game = Game()
    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game.handle_key(event.key)
        if game.quit:
            running = False
        game.update()
        game.draw(screen, font, big_font)
        pygame.display.flip()
        clock.tick(60)
        frame = frame + 1
        if max_frames and frame >= max_frames:
            running = False
    pygame.quit()
    return game


if __name__ == "__main__":
    main()
