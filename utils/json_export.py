import json
from datetime import datetime
import os

def guardar_json(data, nombre_test):
    # Obtener ruta base del proyecto
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Ir a la carpeta raíz (salir de utils)
    ruta_results = os.path.join(BASE_DIR, "..", "results")
    ruta_results = os.path.normpath(ruta_results)

    # Crear carpeta si no existe
    if not os.path.exists(ruta_results):
        os.makedirs(ruta_results)

    # Nombre del archivo
    nombre_archivo = f"{nombre_test}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    archivo = os.path.join(ruta_results, nombre_archivo)

    # Guardar JSON
    with open(archivo, "w") as f:
        json.dump(data, f, indent=4)