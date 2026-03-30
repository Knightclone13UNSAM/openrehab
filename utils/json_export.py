import json
from datetime import datetime
import os

def guardar_json(data, nombre_test):
    if not os.path.exists("results"):
        os.makedirs("results")

    archivo = f"results/{nombre_test}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(archivo, "w") as f:
        json.dump(data, f, indent=4)