import pygame
import sys
from tests.complejidad_gradual import run_test_1
from tests.figura_fondo import run_test_2

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OpenRehab - Evaluación Visual")

font = pygame.font.SysFont(None, 40)

def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

def menu():
    while True:
        screen.fill((0, 0, 0))
        draw_text("OpenRehab - Evaluación Visual", 150, 100)
        draw_text("1 - Complejidad Gradual", 200, 250)
        draw_text("2 - Figura-Fondo", 200, 300)
        draw_text("Click para seleccionar", 200, 400)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 250 < y < 280:
                    run_test_1(screen)
                elif 300 < y < 330:
                    run_test_2(screen)

menu()