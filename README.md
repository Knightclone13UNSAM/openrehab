# 🧠 OpenRehab - Test Figura Fondo y complejidad gradual

Aplicación desarrollada en Python utilizando Pygame para la evaluación cognitiva, basada en tareas de discriminación figura-fondo  y complejidad gradual .

---

## 🎯 Objetivo

Evalúar la Atención selectiva y la Discriminación visual mediante tareas de búsqueda de estímulos y cancelación.


- **¿Que mide?:** Mide la capacidad de filtrado de distractores, resistencia a la interferencia visual, **velocidad de respuesta** y sensibilidad al contraste

---
## 🧪 Tests incluidos

### Figura-Fondo "Buscando a Wally"
El usuario debe identificar un objeto objetivo entre múltiples distractores con características similares.

### Figura-Fondo Clásico
El usuario debe identificar un objeto objetivo cuyos bordes y colores se asemejan al del fondo para evaluar sensibilidad al contraste y la agudeza visual en condiciones de camuflaje. 

### Complejidad Gradual
El usuario debe seleccionar la figura correcta mientras la dificultad aumenta progresivamente.

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
## 📊 Salida de datos

Los resultados se exportan en formato JSON:

- ID del paciente
- Fecha
- Test realizado
- Estado del test
- Nivel alcanzado
- Tiempo promedio
- Cantidad de errores

---
## 👥 Población dirigida y Utilidad Clínica

Este software ha sido desarrollado específicamente para la evaluación y estimulación de pacientes con alteraciones en el procesamiento visual y la atención, incluyendo:

* **Heminegligencia Unilateral (Neglect):** Los tests de búsqueda visual y cancelación permiten evaluar la capacidad del paciente para orientarse y responder a estímulos en el campo visual afectado.
* **Deterioro Visual Cortical o Cerebral (DVC):** El test de **Complejidad Gradual** está diseñado para determinar el umbral de saturación visual del paciente, permitiendo identificar cuántos elementos puede procesar antes de perder la eficiencia visual.
* **Secuelas de ACV o TCE:** Evaluación de la atención selectiva y la resistencia a la interferencia (distractores).
* **Baja Visión y Sensibilidad al Contraste:** El test **Figura-Fondo V2** permite trabajar específicamente con pacientes que presentan dificultades para segmentar objetos de su entorno debido a la similitud de color y contraste.

---

## 👨‍💻 Autor

Ignacio Bagnato