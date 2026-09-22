#modulo de estadisticas, datos faltantes y rankings
def cantidad_ciudades(observaciones: dict) -> int:
    """Devuelve la cantidad total de ciudades leídas."""
    return len(observaciones)

def cantidad_ciudades_completas(observaciones: dict) -> int:
    """Devuelve la cantidad de ciudades sin ningún dato faltante."""
    contador = 0
    for datos in observaciones.values():
        if None not in datos.values():
            contador += 1
    return contador

def datos_faltantes_por_campo(observaciones: dict) -> dict:
    """Calcula la cantidad de faltantes por campo y en qué estaciones ocurren."""
    faltantes = {}
    for ciudad, datos in observaciones.items():
        for campo, valor in datos.items():
            if valor is None:
                if campo not in faltantes:
                    faltantes[campo] = {"cantidad": 0, "estaciones": []}
                faltantes[campo]["cantidad"] += 1
                faltantes[campo]["estaciones"].append(ciudad)
    return faltantes


def top_n_ciudades(observaciones: dict, campo: str, n: int, descendente: bool = True) -> list:
    """Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor
    (o al revés si descendente=False), en una lista. Reutilizable tanto para temperatura
    como para viento."""

    # filtramos las ciudades que tienen None en ese
    #  campo para no romper el orden
    ciudades_validas = []
    
    # guardamos (valor, ciudad) para que .sort() ordene por el valor numero
    for ciudad, datos in observaciones.items():
        if datos.get(campo) is not None:
            ciudades_validas.append((datos[campo], ciudad))

    # odena de menor a mayor por defecto (por el primer elemento de la tupla)
    ciudades_validas.sort()

    # para que sea de mayor a menor
    if descendente:
        ciudades_validas = ciudades_validas[::-1]

    # tomamos los primeros n elementos
    seleccionadas = ciudades_validas[:n]

    # reestructuramos al formato original (ciudad, valor)
    resultado = []
    for valor, ciudad in seleccionadas:
        resultado.append((ciudad, valor))

    return resultado

