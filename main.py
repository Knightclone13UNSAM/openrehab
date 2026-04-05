import pygame
import sys
from tests.complejidad_gradual import run_test_1
from tests.figura_fondo import run_test_2
from tests.figura_fondoV2 import run_test_3
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OpenRehab - Evaluación Visual")

font = pygame.font.SysFont(None, 40)

def pedir_nombre(screen):
    font = pygame.font.Font(None, 50)
    nombre = ""

    while True:
        screen.fill((200, 200, 200))

        texto = font.render("Ingrese su nombre:", True, (0, 0, 0))
        screen.blit(texto, (200, 200))

        nombre_render = font.render(nombre, True, (0, 0, 150))
        screen.blit(nombre_render, (200, 260))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return nombre if nombre != "" else "anonimo"
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += event.unicode

def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

def menu(nombre_paciente):
    while True:
        screen.fill((0, 0, 0))
        draw_text("OpenRehab - Evaluación Visual", 150, 100)
        draw_text("1 - Complejidad Gradual", 200, 200)
        draw_text("2 - Figura-Fondo (Buscando a Wally)", 200, 250)
        draw_text("3 - Figura-Fondo Tradicional", 200, 300)
        draw_text("Click para seleccionar", 200, 400)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 200 < y < 230:
                    run_test_1(screen, nombre_paciente)
                elif 250 < y < 280:
                    run_test_2(screen, nombre_paciente)
                elif 300 < y < 330:
                    run_test_3(screen, nombre_paciente)

nombre_paciente = pedir_nombre(screen)
menu(nombre_paciente)