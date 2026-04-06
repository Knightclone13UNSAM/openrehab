import pygame
import random
import time
import sys
import os

from utils.metrics import calcular_tasa_aciertos, calcular_tiempo_promedio
# --- CONFIGURACIÓN DE PANTALLA ---
WIDTH, HEIGHT = 800, 600


def obtener_ruta(carpeta, archivo):
    """Busca archivos en la carpeta raíz del proyecto (Portable)."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, carpeta, archivo)


def dibujar_ruido_color(screen, color_base):
    """Crea el fondo con el color del nivel y puntitos de camuflaje."""
    screen.fill(color_base)
    for _ in range(600):
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        v = random.randint(-15, 15)
        r = max(0, min(255, color_base[0] + v))
        g = max(0, min(255, color_base[1] + v))
        b = max(0, min(255, color_base[2] + v))
        pygame.draw.circle(screen, (r, g, b), (x, y), random.randint(1, 2))


def pausa(screen):
    """Menú de pausa accesible con mouse."""
    font = pygame.font.Font(None, 60)
    boton = pygame.Rect(200, 250, 400, 120)
    pygame.event.clear()
    while True:
        screen.fill((20, 20, 20))
        screen.blit(font.render("PAUSA", True, (255, 255, 255)), (330, 150))
        pygame.draw.rect(screen, (0, 180, 0), boton, border_radius=15)
        screen.blit(font.render("CONTINUAR", True, (255, 255, 255)), (265, 285))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "salir"
            if event.type == pygame.MOUSEBUTTONDOWN and boton.collidepoint(event.pos): return "continuar"


def run_test_3(screen, nombre_paciente):
    from utils.metrics import calcular_tiempo_promedio
    from utils.json_export import guardar_json

    nivel, tiempos, resultados = 1, [], []
    contrastes_logrados= []

    # Cargar sonidos relativos
    try:
        snd_ok = pygame.mixer.Sound(obtener_ruta("assets", "acierto.wav"))
        snd_err = pygame.mixer.Sound(obtener_ruta("assets", "error.wav"))
    except:
        snd_ok = snd_err = None

    for intento in range(10):
        # Color aleatorio para que cada nivel sea distinto y no lúgubre
        color_bg = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
        # Dificultad por contraste (Epsilon)
        epsilon = max(5, 45 - (nivel * 4))
        color_obj = (min(255, color_bg[0] + epsilon), min(255, color_bg[1] + epsilon), min(255, color_bg[2] + epsilon))
        pos_obj, radio = (random.randint(150, 650), random.randint(150, 450)), 28

        # Pantalla de preparación
        screen.fill((0, 0, 0))
        f = pygame.font.Font(None, 45)
        screen.blit(f.render(f"Nivel {nivel}: Buscá el círculo", True, (255, 255, 255)), (230, 200))
        pygame.draw.rect(screen, color_bg, (350, 280, 100, 100))
        pygame.draw.circle(screen, color_obj, (400, 330), radio)
        pygame.display.flip()
        pygame.time.delay(1500)

        def refrescar():
            dibujar_ruido_color(screen, color_bg)
            pygame.draw.circle(screen, color_obj, pos_obj, radio)
            pygame.draw.rect(screen, (60, 60, 60), (740, 20, 15, 40))  # Botón Pausa
            pygame.draw.rect(screen, (60, 60, 60), (765, 20, 15, 40))
            pygame.display.flip()

        refrescar()
        start_t, clicked = time.time(), False
        while not clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # ROBUSTEZ: Guardar antes de cerrar
                    data_emergencia = {"paciente": nombre_paciente,
                        "test": "Figura-Fondo V2",
                        "estado": "INTERRUMPIDO_POR_USUARIO",
                        "nivel_alcanzado": nivel,
                        "aciertos_parciales": resultados.count(True),
                        "tr_promedio_ms": round(calcular_tiempo_promedio(tiempos), 2),
                        "ultimo_contraste_intentado": epsilon,
                        "fecha": time.strftime("%d/%m/%Y %H:%M:%S")
                    }
                    guardar_json(data_emergencia, f"figura_fondo_{nombre_paciente}")
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Detectar click en pausa
                    if pygame.Rect(730, 10, 70, 70).collidepoint(event.pos):
                        p_ini = time.time()
                        if pausa(screen) == "salir":
                            data = {"id": nombre_paciente, "estado": "salida_pausa"}
                            guardar_json(data, f"figura_fondo_{nombre_paciente}")
                            pygame.quit()
                            sys.exit()
                        start_t += (time.time() - p_ini)
                        refrescar()
                        continue

                    reaccion = (time.time() - start_t) * 1000
                    dist = ((event.pos[0] - pos_obj[0]) ** 2 + (event.pos[1] - pos_obj[1]) ** 2) ** 0.5

                    if dist < radio:
                        if snd_ok: snd_ok.play()
                        resultados.append(True)
                        tiempos.append(reaccion)
                        contrastes_logrados.append(epsilon)
                        screen.fill((30, 120, 30))
                        nivel = min(10, nivel + 1)
                    else:
                        if snd_err: snd_err.play()
                        resultados.append(False)
                        screen.fill((120, 30, 30))
                        nivel = max(1, nivel - 1)

                    pygame.display.flip()
                    pygame.time.delay(600)
                    clicked = True

    #Calculos clínicos
    tasa = calcular_tasa_aciertos(resultados)
    # El umbral es el epsilon más bajo (más difícil) donde acertó
    umbral_minimo = min(contrastes_logrados) if contrastes_logrados else "No alcanzado"

    # --- GUARDADO FINAL ---
    data_final = {
        "paciente": nombre_paciente,
        "test": "Figura Fondo V2 (Sensibilidad al Contraste)",
        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
        "Estado": "Completado Exitosamente",

        #Umbral de Contraste
        "umbral_contraste_delta_rgb": umbral_minimo,

        #Desempeño
        "nivel_alcanzado": nivel,
        "tiempo_aciertos_precision": f"{tasa}%",
        "aciertos": resultados.count(True),
        "errores": resultados.count(False),

        #Velocidad de Procesamiento
        "tiempo_promedio_ms": round(calcular_tiempo_promedio(tiempos),2)
    }
    guardar_json(data_final, f"figura_fondo_V2_{nombre_paciente}")