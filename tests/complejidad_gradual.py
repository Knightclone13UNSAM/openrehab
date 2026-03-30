import pygame
import random
import time
from utils.metrics import calcular_tiempo_promedio
from utils.json_export import guardar_json

WIDTH, HEIGHT = 800, 600

def draw_circle(screen, color, pos, radius):
    pygame.draw.circle(screen, color, pos, radius)

def run_test_1(screen):
    nivel = 1
    max_nivel = 10
    tiempos = []
    resultados = []

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

        # Mostrar escena
        screen.fill((0, 0, 0))
        for obj in objetos:
            draw_circle(screen, obj[1], obj[0], obj[3])

        pygame.display.flip()

        start = time.time()
        clicked = False

        while not clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    end = time.time()
                    tiempo = (end - start) * 1000
                    tiempos.append(tiempo)

                    x, y = event.pos

                    for obj in objetos:
                        ox, oy = obj[0]
                        if (x - ox)**2 + (y - oy)**2 < 20**2:

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

    data = {
        "id_paciente": "001",
        "fecha": time.strftime("%Y-%m-%d"),
        "tests": "complejidad_gradual",
        "metrica_principal": nivel,
        "unidad": "nivel",
        "intentos": len(tiempos),
        "tiempo_promedio_ms": calcular_tiempo_promedio(tiempos),
        "errores": resultados.count(False)
    }

    guardar_json(data, "complejidad_gradual")