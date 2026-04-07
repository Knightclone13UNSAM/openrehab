import pygame
import random
import time
import os
from utils.metrics import calcular_tiempo_promedio, calcular_tasa_aciertos
from utils.json_export import guardar_json

WIDTH, HEIGHT = 800, 600

# Inicializar mixer si no está inicializado
if not pygame.mixer.get_init():
    pygame.mixer.init()

# BASE_DIR es .../openrehab/tests
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Subimos un nivel para llegar a la raíz (.../openrehab) y luego entramos a assets
ruta_assets = os.path.abspath(os.path.join(BASE_DIR, "..", "assets"))

path_correct = os.path.join(ruta_assets, "correct.wav")
path_wrong = os.path.join(ruta_assets, "wrong.wav")

# Verificación de depuración (esto imprimirá la ruta real en tu consola)
print(f"Buscando sonidos en: {ruta_assets}")

try:
    correct_sound = pygame.mixer.Sound(path_correct)
    wrong_sound = pygame.mixer.Sound(path_wrong)
except pygame.error as e:
    print(f"⚠️ No se pudo cargar el sonido: {e}")
    # Sonido silencioso para evitar que el programa se cierre
    correct_sound = pygame.mixer.Sound(buffer=bytes(0))
    wrong_sound = pygame.mixer.Sound(buffer=bytes(0))


def draw_shape(screen, color, pos, size, tipo):
    if tipo == "circle":
        pygame.draw.circle(screen, color, pos, size)
    elif tipo == "square":
        pygame.draw.rect(screen, color, (pos[0] - size, pos[1] - size, size * 2, size * 2))

def posicion_valida(nueva_pos, posiciones_existentes, min_dist):
    for pos in posiciones_existentes:
        dx = nueva_pos[0] - pos[0]
        dy = nueva_pos[1] - pos[1]
        if (dx*dx + dy*dy) < (min_dist * min_dist):
            return False
    return True


def pausa(screen):
    font = pygame.font.Font(None, 50)
    boton_rect = pygame.Rect(250, 250, 300, 100)

    # Limpiamos eventos viejos para que el clic de "entrar" a pausa
    # no se use para "salir" de la pausa.
    pygame.event.clear()

    while True:
        screen.fill((120, 120, 120))
        texto = font.render("PAUSA", True, (255, 255, 255))
        screen.blit(texto, (340, 150))

        pygame.draw.rect(screen, (0, 200, 0), boton_rect)
        texto_btn = font.render("CONTINUAR", True, (0, 0, 0))
        screen.blit(texto_btn, (290, 285))

        pygame.display.flip()

        # En lugar de wait(), usamos un for event normal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.MOUSEBUTTONDOWN:  # Usamos DOWN para ser consistentes
                if boton_rect.collidepoint(event.pos):
                    return "continuar"

def run_test_2(screen, nombre_paciente):
    nivel = 1
    max_nivel = 10
    tiempos = []
    resultados = []

    # Boton de pausa
    pause_rect = pygame.Rect(740, 10, 50, 50)

    for intento in range(10):
        screen.fill((200, 200, 200))  # fondo gris

        # OBJETIVO
        objetivo_pos = (random.randint(50, 750), random.randint(120, 550))
        posiciones_usadas = [objetivo_pos]
        objetivo_color = (200, 50, 50)
        objetivo_tipo = "square"

        # Mostrar consigna
        screen.fill((200, 200, 200))

        font = pygame.font.Font(None, 40)
        text = font.render("Buscá este objeto", True, (0, 0, 0))
        screen.blit(text, (280, 50))

        draw_shape(screen, objetivo_color, (WIDTH // 2, HEIGHT // 2), 25, objetivo_tipo)

        pygame.display.flip()
        pygame.time.delay(2000)


        # DIFICULTAD
        distractores = nivel * 10
        objetos = []

        grid_size = 40
        posiciones = []

        for x in range(50, 750, grid_size):
            for y in range(120, 550, grid_size):
                posiciones.append((x, y))

        random.shuffle(posiciones)

        posiciones_usadas = []

        for _ in range(distractores):

            while True:
                pos = posiciones.pop()

                if posicion_valida(pos, posiciones_usadas, 45):
                    posiciones_usadas.append(pos)
                    break

            # Distractores muy parecidos
            while True:
                color = (random.randint(60, 120), random.randint(60, 120), random.randint(60, 120))
                tipo = random.choice(["circle", "square"])

                # Evitar mismo tipo que el objetivo
                if tipo != objetivo_tipo:
                    break

            size = random.randint(10, 30)
            objetos.append((pos, color, tipo, False, size))

        # Agregar objetivo
        objetos.append((objetivo_pos, objetivo_color, objetivo_tipo, True,20))

        random.shuffle(objetos)

        # DIBUJAR
        screen.fill((200, 200, 200))

        # Mostrar objetivo arriba (referencia)
        font = pygame.font.Font(None, 30)
        text = font.render("Objetivo:", True, (0, 0, 0))

        # Panel superior oscuro
        pygame.draw.rect(screen, (30, 30, 30), (0, 0, WIDTH, 80))

        # Línea divisoria
        pygame.draw.line(screen, (255, 255, 255), (0, 80), (WIDTH, 80), 2)

        # Texto
        font = pygame.font.Font(None, 30)
        text = font.render("Objetivo:", True, (255, 255, 255))
        screen.blit(text, (20, 25))

        # Marco blanco (tipo referencia clínica)
        pygame.draw.rect(screen, (255, 255, 255), (120, 10, 80, 60), 2)

        # Objeto de referencia MÁS GRANDE
        draw_shape(screen, objetivo_color, (160, 40), 20, objetivo_tipo)

        # Dibujar escena
        for obj in objetos:
            draw_shape(screen, obj[1], obj[0], obj[4], obj[2])

        # Boton pausa
        pygame.draw.rect(screen, (200, 200, 200), pause_rect)
        pygame.draw.rect(screen, (0, 0, 0), (750, 20, 8, 30))
        pygame.draw.rect(screen, (0, 0, 0), (770, 20, 8, 30))

        pygame.display.flip()

        start = time.time()
        clicked = False
        ignorar_click= False

        while not clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if len(tiempos) > 0:
                        tasa = calcular_tasa_aciertos(resultados)
                        data = {
                            "id_paciente": nombre_paciente,
                            "fecha": time.strftime("%Y-%m-%d"),
                            "tests": "figura_fondo_wally",
                            "estado_sesion": "Interrumpido",  # Agregamos el estado
                            "nivel_maxima_densidad": nivel,
                            "tasa_aciertos_precision": f"{tasa}%",
                            "intentos": len(tiempos),
                            "tiempo_reaccion_promedio_ms": round(calcular_tiempo_promedio(tiempos), 2),
                            "errores_totales": resultados.count(False)
                        }
                        guardar_json(data, f"figura_fondo_{nombre_paciente}")
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ignorar_click:
                        ignorar_click= False
                        continue

                    if pause_rect.collidepoint(event.pos):
                        pausa_inicio = time.time()
                        res = pausa(screen)
                        if res == "salir":
                            if len(tiempos) > 0:
                                tasa = calcular_tasa_aciertos(resultados)
                                data = {
                                    "id_paciente": nombre_paciente,
                                    "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                                    "tests": "figura_fondo_wally",
                                    "estado_sesion": "Interrumpido (desde Pausa)",
                                    "nivel_maxima_densidad": nivel,
                                    "tasa_aciertos_precision": f"{tasa}%",
                                    "intentos": len(tiempos),
                                    "tiempo_reaccion_promedio_ms": round(calcular_tiempo_promedio(tiempos), 2),
                                    "errores_totales": resultados.count(False)
                                }
                                guardar_json(data, f"figura_fondo_{nombre_paciente}")
                            return

                        pausa_fin = time.time()
                        start += (pausa_fin - pausa_inicio)  # CORRIGE EL TIEMPO

                        #Redibujamos menu
                        screen.fill((200, 200, 200))
                        pygame.draw.rect(screen, (30, 30, 30), (0, 0, WIDTH, 80))
                        pygame.draw.line(screen, (255, 255, 255), (0, 80), (WIDTH, 80), 2)
                        font = pygame.font.Font(None, 30)
                        text = font.render("Objetivo:", True, (255, 255, 255))
                        screen.blit(text, (20, 25))
                        pygame.draw.rect(screen, (255, 255, 255), (120, 10, 80, 60), 2)
                        draw_shape(screen, objetivo_color, (160, 40), 20, objetivo_tipo)

                        #Redibujamos boton pausa
                        pygame.draw.rect(screen, (200, 200, 200), pause_rect)
                        pygame.draw.rect(screen, (0, 0, 0), (750, 20, 8, 30))
                        pygame.draw.rect(screen, (0, 0, 0), (770, 20, 8, 30))


                        for obj in objetos:
                            draw_shape(screen, obj[1], obj[0], obj[4], obj[2])

                        pygame.display.flip()


                        continue

                    end = time.time()
                    tiempo = (end - start) * 1000
                    tiempos.append(tiempo)

                    x, y = event.pos

                    for obj in objetos:
                        ox, oy = obj[0]

                        size=obj[4]
                        if (x - ox)**2 + (y - oy)**2 < size**2:

                            if obj[3]:  # acierto
                                correct_sound.play()
                                resultados.append(True)

                                screen.fill((200, 200, 200))
                                font = pygame.font.Font(None, 60)
                                text = font.render("CORRECTO", True, (0, 150, 0))
                                screen.blit(text, (300, 250))
                                pygame.display.flip()
                                pygame.time.delay(800)

                                if tiempo < 2000:
                                    nivel += 1

                            else:
                                wrong_sound.play()
                                resultados.append(False)

                                screen.fill((200, 200, 200))
                                font = pygame.font.Font(None, 60)
                                text = font.render("INCORRECTO", True, (200, 0, 0))
                                screen.blit(text, (280, 250))
                                pygame.display.flip()
                                pygame.time.delay(800)

                                nivel -= 1

                            nivel = max(1, min(max_nivel, nivel))
                            clicked = True
    tasa= calcular_tasa_aciertos(resultados)
    data = {
        "id_paciente": nombre_paciente,
        "fecha": time.strftime("%Y-%m-%d"),
        "tests": "figura_fondo_wally",
        "estado": "Completado",
        "nivel_maxima_densidad": nivel,
        "tasa_aciertos_precision": f"{tasa}%",
        "intentos": len(tiempos),
        "tiempo_reaccion_promedio_ms": round(calcular_tiempo_promedio(tiempos),2),
        "errores_totales": resultados.count(False)
    }

    guardar_json(data, f"figura_fondo_{nombre_paciente}")

