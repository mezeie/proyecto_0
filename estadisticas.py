#modulo de estadisticas, datos faltantes y rankings
#
def cantidad_ciudades(observaciones: dict) -> int:
    """Devuelve la cantidad total de ciudades leídas."""
    return len(observaciones)

def cantidad_ciudades_completas(observaciones: dict) -> int:
    """Devuelve la cantidad de ciudades sin ningún dato faltante."""
    return sum(1 for datos in observaciones.values() if None not in datos.values())

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
    ciudades_validas = []
    for ciudad, datos in observaciones.items():
        if datos.get(campo) is not None:
            ciudades_validas.append((datos[campo], ciudad))

    ciudades_validas.sort(reverse=descendente)

    seleccionadas = ciudades_validas[:n]
    # (ciudad, valor)
    return [(ciudad, valor) for valor, ciudad in seleccionadas]

