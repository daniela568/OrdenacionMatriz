def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante el período dado.

    :param temperaturas: Diccionario donde las claves son nombres de ciudades y los valores son listas de temperaturas semanales.
    :return: Diccionario con las ciudades y sus respectivas temperaturas promedio.
    """
    promedios = {}
    for ciudad, temp_semanal in temperaturas.items():
        promedio = sum(temp_semanal) / len(temp_semanal)
        promedios[ciudad] = round(promedio, 2)  # Redondeamos a 2 decimales

    return promedios

# Datos de temperaturas: 3 ciudades durante 4 semanas
temperaturas_ciudades = {
    "Ciudad A": [22, 24, 19, 23],
    "Ciudad B": [30, 32, 29, 31],
    "Ciudad C": [15, 18, 17, 16]
}

# Prueba de la función
resultados = calcular_temperatura_promedio(temperaturas_ciudades)
print("Temperaturas promedio por ciudad:", resultados)
