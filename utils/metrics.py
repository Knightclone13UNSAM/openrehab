def calcular_tiempo_promedio(tiempos):
    return sum(tiempos) / len(tiempos) if tiempos else 0

def calcular_tasa_aciertos(resultados):
    """
    Recibe la lista de booleanos [True, False, True...]
    y devuelve el porcentaje de aciertos.
    """
    if not resultados:
        return 0
    aciertos = resultados.count(True)
    return round((aciertos / len(resultados)) * 100, 2)