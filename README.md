# 🧠 OpenRehab - Test Figura Fondo y complejidad gradual

Aplicación desarrollada en Python utilizando Pygame para la evaluación cognitiva, basada en tareas de discriminación figura-fondo (similar a "¿Dónde está Wally?") y complejidad gradual (seleccionar figura correcta).

---

## 🎯 Objetivo

Evaluar:
- Atención selectiva
- Discriminación visual
- Velocidad de respuesta

El usuario debe identificar un objeto objetivo entre múltiples distractores con características similares.

---
## 🧪 Tests incluidos

### Figura-Fondo
El usuario debe identificar un objeto objetivo entre múltiples distractores con características similares.

### Complejidad Gradual
El usuario debe seleccionar la figura correcta mientras la dificultad aumenta progresivamente.

---
## 🛠️ Tecnologías utilizadas

- Python 3
- Pygame
- JSON (para exportación de resultados)

---

## 💻 Requisitos

Antes de ejecutar el programa, asegurarse de tener instalado:

- Python 3 (https://www.python.org/)
- pip (gestor de paquetes de Python)

---

## ▶️ Instalación y ejecución

1. Clonar el repositorio:
Abrir terminal de comandos en la carpeta deseada

```bash
git clone https://github.com/Knightclone13UNSAM/openrehab.git
cd openrehab
```

2. Instalar dependencias (PyGame)

```bash
pip install pygame
```

3. Para ejecutar el juego abrir en terminal o aplicacion (Visual Studio / PyCharm)

```bash
python main.py
```

---

##📁 Estructura del proyecto
- `.idea/` → Archivos de configuración de PyCharm (opcional)
- `tests/` → Contiene los juegos (figura-fondo y complejidad gradual)
- `results/` → Guarda los resultados en formato JSON
- `assets/` → Sonidos (.wav)
- `utils/` → Métricas y exportación de resultados
- `generate_sounds.py` → Script para generar sonidos
- `main.py` → Codigo principal del programa

---
##🔊 Funcionalidades
Generación dinámica de estímulos
Variación de tamaño, forma y color
Evita superposición de objetos
Feedback:
✔ Correcto (sonido + mensaje)
✖ Incorrecto (sonido + mensaje)
Registro de métricas:
Tiempo de respuesta
Errores
Nivel alcanzado

---
##📊 Salida de datos
Los resultados se exportan en formato JSON:
ID del paciente
Fecha
Test realizado
Nivel alcanzado
Tiempo promedio
Cantidad de errores

---
##🧪 Contexto académico
Proyecto orientado al desarrollo de herramientas de evaluación cognitiva en rehabilitación, enfocado en procesos perceptuales y atencionales.
---

##👨‍💻 Autor
Ignacio Bagnato