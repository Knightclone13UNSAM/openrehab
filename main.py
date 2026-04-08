import pygame
import sys
from tests.complejidad_gradual import run_test_1
from tests.complejidad_visualV2 import run_test_2
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


def draw_text(text, x, y, color=(255, 255, 255)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


# --- NUEVO SUB-MENÚ PARA COMPLEJIDAD ---
def menu_complejidad(nombre_paciente):
    while True:
        screen.fill((30, 30, 30))  # Un gris oscuro para diferenciarlo del principal
        draw_text("Seleccione Nivel de Complejidad", 150, 100)

        draw_text("1 - Nivel Estándar (Gradual)", 200, 200)
        draw_text("2 - Nivel Difícil (Wally)", 200, 270)
        draw_text("3 - Volver al Menú Principal", 200, 340, (255, 100, 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 200 < y < 230:
                    run_test_1(screen, nombre_paciente)
                elif 270 < y < 300:
                    run_test_2(screen, nombre_paciente)
                elif 340 < y < 370:
                    return  # Vuelve al menu anterior


def menu(nombre_paciente):
    while True:
        screen.fill((0, 0, 0))
        draw_text(f"Paciente: {nombre_paciente}", 20, 20, (0, 255, 0))
        draw_text("OpenRehab - Evaluación Visual", 150, 100)

        # Menú Principal con solo 2 ramas
        draw_text("1 - Test de Complejidad Visual / Wally", 200, 200)
        draw_text("2 - Figura-Fondo Tradicional (V2)", 200, 300)

        draw_text("Esc para Salir", 200, 450, (150, 150, 150))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Si toca la opcion 1, va al sub-menú nuevo
                if 200 < y < 230:
                    menu_complejidad(nombre_paciente)
                # Si toca la opcion 2, va directo al V2
                elif 300 < y < 330:
                    run_test_3(screen, nombre_paciente)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


nombre_paciente = pedir_nombre(screen)
menu(nombre_paciente)