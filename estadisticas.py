#modulo de estadisticas, datos faltantes y rankings

def cantidad_ciudades(observaciones: dict) -> int:
    """retorna la cantidad total de ciudades leidas"""
    pass


def cantidad_ciudades_completas(observaciones: dict) -> int:
    """retorna la cantidad de ciudades sin datos faltantes"""
    pass


def top_n_ciudades(
    observaciones: dict, campo: str, n: int, descendente: bool = True
) -> list:
    """ordena las ciudades segun el campo indicado y devuelve las top n"""
    pass