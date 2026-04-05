import pygame
import random
import time
import os
import sys

from utils.metrics import calcular_tiempo_promedio
from utils.json_export import guardar_json

WIDTH, HEIGHT = 800, 600

def draw_circle(screen, color, pos, radius):
    pygame.draw.circle(screen, color, pos, radius)


def pausa(screen):
    font = pygame.font.Font(None, 50)
    boton_rect = pygame.Rect(250, 250, 300, 100)

    pygame.event.clear()  # Limpia eventos previos

    while True:
        screen.fill((30, 30, 30))  # Fondo gris oscuro para el menú

        texto = font.render("JUEGO EN PAUSA", True, (255, 255, 255))
        screen.blit(texto, (250, 150))

        pygame.draw.rect(screen, (0, 200, 0), boton_rect)
        texto_btn = font.render("CONTINUAR", True, (255, 255, 255))
        screen.blit(texto_btn, (300, 285))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(event.pos):
                    return "continuar"

def run_test_1(screen, nombre_paciente):
    nivel = 1
    max_nivel = 10
    tiempos = []
    resultados = []

    # Rectángulo para detectar el clic de pausa (esquina superior derecha)
    pause_rect = pygame.Rect(740, 10, 50, 50)

    for intento in range(10):
        screen.fill((0, 0, 0))

        # Mostrar objetivo (pantalla de referencia)
        objetivo_color = (0, 0, 255)
        objetivo_pos = (random.randint(50, 750), random.randint(50, 550))

        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 40)
        text = font.render("Buscá este objetivo", True, (255, 255, 255))
        screen.blit(text, (260, 50))

        draw_circle(screen, objetivo_color, (WIDTH // 2, HEIGHT // 2), 25)

        pygame.display.flip()
        pygame.time.delay(1800)

        # Generar distractores
        distractores = nivel * 3
        objetos = []
        #print("Cantidad de objetos:", len(objetos))

        for _ in range(distractores):
            pos = (random.randint(50, 750), random.randint(50, 550))

            if nivel < 5:
                color = (0, 255, 0)
                radius = 20
            else:
                color = (0, 100, 255)
                radius = random.randint(15, 25)

            objetos.append((pos, color, False, radius))
        #print("Después de cargar:", len(objetos))
        # Agregar objetivo
        objetos.append((objetivo_pos, objetivo_color, True, 20))

        random.shuffle(objetos)

        def dibujar_todo():
            screen.fill((0, 0, 0))
            for obj in objetos:
                draw_circle(screen, obj[1], obj[0], obj[3])
            # Dibujar botón de pausa (dos barritas blancas)
            pygame.draw.rect(screen, (255, 255, 255), (750, 15, 10, 35))
            pygame.draw.rect(screen, (255, 255, 255), (770, 15, 10, 35))
            pygame.display.flip()

        dibujar_todo()

        start = time.time()
        clicked = False

        while not clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Datos de emergencia si cierra con la X
                    data_aux = {
                        "id_paciente": nombre_paciente,
                        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "test": "complejidad_gradual",
                        "estado": "incompleto: Interrumpido por el usuario",
                        "intentos": len(resultados),
                        "nivel_final": nivel
                    }
                    guardar_json(data_aux, f"complejidad_gradual_{nombre_paciente}")
                    pygame.quit()
                    import sys
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # SI TOCA EL BOTÓN DE PAUSA
                    if pause_rect.collidepoint(event.pos):
                        p_inicio = time.time()
                        res = pausa(screen)

                        if res == "salir":
                            # Datos de emergencia si cierra desde el menú de pausa
                            data_pausa = {
                                "id_paciente": nombre_paciente,
                                "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                                "test": "complejidad_gradual",
                                "estado": "interrumpido_en_pausa",
                                "intentos": len(resultados),
                                "nivel_final": nivel
                            }
                            guardar_json(data_pausa, f"complejidad_gradual_{nombre_paciente}")
                            pygame.quit()
                            import sys
                            sys.exit()

                        # Al volver: corregir tiempo y redibujar
                        p_fin = time.time()
                        start += (p_fin - p_inicio)
                        dibujar_todo()
                        continue

                    end = time.time()
                    tiempo = (end - start) * 1000
                    tiempos.append(tiempo)

                    x, y = event.pos

                    for obj in objetos:
                        ox, oy = obj[0]
                        radio_obj = obj[3]
                        if (x - ox)**2 + (y - oy)**2 < radio_obj**2:

                            if obj[2]:  # acierto
                                resultados.append(True)

                                # Feedback visual VERDE
                                screen.fill((0, 0, 0))
                                font = pygame.font.Font(None, 60)
                                text = font.render("✔ Correcto", True, (0, 255, 0))
                                screen.blit(text, (300, 250))
                                pygame.display.flip()
                                pygame.time.delay(800)

                                if tiempo < 1500:
                                    nivel += 1

                            else:
                                resultados.append(False)

                                # Feedback visual ROJO
                                screen.fill((0, 0, 0))
                                font = pygame.font.Font(None, 60)
                                text = font.render("✖ Incorrecto", True, (255, 0, 0))
                                screen.blit(text, (280, 250))
                                pygame.display.flip()
                                pygame.time.delay(800)

                                nivel -= 1

                            nivel = max(1, min(max_nivel, nivel))
                            clicked = True
                            break

    data = {
        "id_paciente": nombre_paciente,
        "fecha": time.strftime("%Y-%m-%d"),
        "tests": "complejidad_gradual",
        "Estado": "Completado exitosamente",
        "metrica_principal": nivel,
        "unidad": "nivel",
        "intentos": len(tiempos),
        "tiempo_promedio_ms": calcular_tiempo_promedio(tiempos),
        "errores": resultados.count(False)
    }

    guardar_json(data, f"complejidad_gradual_{nombre_paciente}")
    if event.type == pygame.QUIT:
        guardar_json(data, f"complejidad_gradual_{nombre_paciente}")
        pygame.quit()
        return