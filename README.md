# 🧠 OpenRehab - Test Figura Fondo y complejidad gradual

Aplicación desarrollada en Python utilizando Pygame para la evaluación cognitiva, basada en tareas de discriminación figura-fondo  y complejidad gradual .

---

## 🎯 Objetivo Clínico
Evaluar la **atención selectiva** y la **discriminación visual** mediante tareas de búsqueda, cancelación y segmentación. El sistema permite determinar umbrales de saturación y sensibilidad al contraste en pacientes con compromiso neurológico (**Neglect, DVC, ACV**).

---

## 🧪 Módulos y Métricas

| Test | Descripción | Variable Clínica / Modo |
| :--- | :--- | :--- |
| **Buscando a Wally** | Búsqueda de un objetivo único entre distractores. | **Densidad:** Capacidad de filtrado y rastreo visual. |
| **Figura-Fondo V2** | Identificación de estímulos con camuflaje. | **Umbral de Contraste:** Incluye modo **Gris (Psicofísica)** y **Color (Funcional)**. |
| **Complejidad Gradual**| Tarea de cancelación con carga progresiva. | **Saturación:** Resistencia a la interferencia y fatiga. |
> **Nota Técnica:** Todos los módulos registran el **Tiempo de Reacción (TR) Neto**, descontando automáticamente los periodos de pausa para garantizar la validez de la velocidad de procesamiento medida.
---
### 🛡️ Robustez y Seguridad de Datos
El sistema incluye mecanismos de protección de información:

- **Guardado de Emergencia:** Si el test se cierra inesperadamente (botón X), se genera un reporte JSON automático con los datos parciales.

- **Estado del Test:** Los resultados indican si la sesión fue completada exitosamente o interrumpida.

---
## 🛠️ Tecnologías utilizadas

- Python 3
- Pygame
- JSON (para exportación de resultados)

---

## 💻 Requisitos

Antes de ejecutar el programa, asegurarse de tener instalado:

- Python 3.12 o anterior (https://www.python.org/)
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
pip install -r requirements.txt
```

3. Para ejecutar el juego abrir en terminal o aplicacion (Visual Studio / PyCharm)

```bash
python main.py
```

---

## 📁 Estructura del proyecto
- `tests/` → Contiene los juegos (figura-fondo y complejidad gradual)
- `results/` → Guarda los resultados en formato JSON
- `assets/` → Sonidos (.wav)
- `utils/` → Métricas y exportación de resultados
- `generate_sounds.py` → Script para generar sonidos
- `main.py` → Codigo principal del programa

---
## 📊 Salida de Datos (Reporte JSON)

El sistema genera un archivo detallado por cada sesión para su posterior análisis estadístico o integración en historias clínicas. Los campos exportados incluyen:

* **Metadatos:** ID del paciente, Fecha/Hora exacta, Test realizado y Modo (gris/color).
* **Estado Clínico:** `Completado` o `Interrumpido` (permite evaluar fatiga o tolerancia a la frustración).
* **Desempeño Cuantitativo:**
    * **Tasa de Aciertos:** Precisión perceptual expresada en porcentaje.
    * **TR Neto:** Tiempo de Reacción promedio en milisegundos (excluye tiempos de pausa).
    * **Métrica Específica:** Umbral de contraste (Delta RGB) o Nivel de saturación alcanzado.
* **Registro de Errores:** Conteo total de fallas de discriminación visual.

---
## 👥 Población y Utilidad Clínica

El software provee herramientas cuantitativas para la evaluación y estimulación de procesos visuales complejos, siendo especialmente efectivo en:

* **Heminegligencia Unilateral (Neglect):** Análisis de la exploración espacial y tiempos de respuesta en los campos visuales afectados mediante tareas de cancelación.
* **Deterioro Visual Cortical/Cerebral (DVC):** Determinación del **Umbral de Saturación**. El sistema identifica la cantidad exacta de estímulos que el paciente procesa antes de perder eficiencia visual.
* **Baja Visión y Sensibilidad al Contraste:** Evaluación psicofísica mediante el **Delta RGB** (Figura-Fondo V2), midiendo la capacidad de segmentación en condiciones de camuflaje.
* **Secuelas de ACV o TCE:** Medición de la **Velocidad de Procesamiento (TR)** y la resistencia a la interferencia visual ante distractores densos.
---

## 👨‍💻 Autores

Bagnato Ignacio, Ferreira Agustin , Garcia Irlanda y Rivero Ariel