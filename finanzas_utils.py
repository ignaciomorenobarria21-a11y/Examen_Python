def calcular_retorno_diario(precio_actual, precio_anterior):
    """
    Calcula el porcentaje de cambio entre dos precios.
    """
    retorno = ((precio_actual - precio_anterior) / precio_anterior) * 100
    return retorno

def categorizar_volatilidad(desviacion_estandar):
    """
    Clasifica la volatilidad según el porcentaje de la desviación estándar.
    """
    if desviacion_estandar < 2:
        return "Baja"
    elif 2 <= desviacion_estandar <= 5:
        return "Media"
    else:
        return "Alta"