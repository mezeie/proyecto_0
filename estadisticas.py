#modulo de estadisticas, datos faltantes y rankings
def cantidad_ciudades(observaciones: dict) -> int:
    """Devuelve la cantidad total de ciudades leídas."""
    return len(observaciones)

def cantidad_ciudades_completas(observaciones: dict) -> int:
    """Devuelve la cantidad de ciudades sin ningún dato faltante."""

    total = len(observaciones)
    completas = 0

    for datos in observaciones.values():
        # comprueba si temperatura o sensación térmica quedaron en None
        if (
            datos["temperatura"] is not None
            and datos["sensacion_termica"] is not None
        ):
            completas += 1

    return (total, completas)

def top_n_ciudades(observaciones: dict, campo: str, n: int, descendente: bool = True) -> list:
    """Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor
    (o al revés si descendente=False), en una lista. Reutilizable tanto para temperatura
    como para viento."""
