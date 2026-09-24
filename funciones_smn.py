from datetime import datetime

MESES = {m: i + 1 for i, m in enumerate([
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
])}
    
def separar_viento(campo: str) -> tuple:
    """Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
    Contempla el caso 'Calma' (sin velocidad numérica)."""
    campo = campo.strip()
    if not campo or campo.lower() == "no se calcula":
        return (None, None)
    if campo.lower() == "calma":
        return ("Calma", 0)

    palabras = campo.split()
    if palabras and palabras[-1].isdigit():
        return (" ".join(palabras[:-1]), int(palabras[-1]))
    return (campo, None)

def a_numero(val: str):
    """Convierte un string a float o devuelve None si no es numérico o no se calcula."""
    try:
        return float(val)
    except ValueError:
        return None
    
def leer_observaciones(ruta: str) -> tuple:
    """Lee el archivo de observaciones del SMN y devuelve una tupla con:
    - El diccionario {ciudad: datos}
    - La cantidad de líneas inválidas encontradas."""

    observaciones = {}
    lineas_invalidas = 0

    try:
        with open(ruta, "r", encoding="latin-1") as archivo:
            for linea in archivo:
                linea = linea.strip().replace("/", "")
                if not linea:
                    continue

                campos = [c.strip() for c in linea.split(";")]
                if len(campos) != 10:
                    lineas_invalidas += 1
                    continue

                # parseo de la fecha con datetime
                p_fecha = campos[1].split("-")
                fecha = None
                if len(p_fecha) == 3:
                    dia, mes_nombre, anio = p_fecha
                    mes = MESES.get(mes_nombre.lower())
                    if mes and dia.isdigit() and anio.isdigit():
                        fecha = datetime(int(anio), mes, int(dia)).date()

                dir_viento, vel_viento = separar_viento(campos[8])

                observaciones[campos[0]] = {
                    "fecha": fecha,
                    "hora": campos[2],
                    "condicion": campos[3],
                    "visibilidad": campos[4],
                    "temperatura": a_numero(campos[5]),
                    "sensacion_termica": a_numero(campos[6]),
                    "humedad": campos[7],
                    "direccion_viento": dir_viento,
                    "velocidad_viento": vel_viento,
                    "presion": a_numero(campos[9]),
                }
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
        return {}, 0

    return observaciones, lineas_invalidas

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

def mostrar_resumen(observaciones, lineas_invalidas):
    if len(observaciones) == 0:
        print("No hay datos para mostrar.")
        return

    print("=== RESUMEN METEOROLOGICO ===")
    print("Total ciudades:", cantidad_ciudades(observaciones))
    print("Ciudades completas:", cantidad_ciudades_completas(observaciones))
    print("Líneas inválidas:", lineas_invalidas)
    print()

    print("--- Datos Faltantes ---")
    faltantes = datos_faltantes_por_campo(observaciones)
    if len(faltantes) == 0:
        print("Sin datos faltantes.")
    else:
        for campo, info in faltantes.items():
            cant = info["cantidad"]
            estaciones = info["estaciones"]
            print("-", campo, ":", cant, "en", estaciones)

    # Obtenemos los rankings
    calidas = top_n_ciudades(observaciones, "temperatura", 5, True)
    frias = top_n_ciudades(observaciones, "temperatura", 5, False)
    vmas = top_n_ciudades(observaciones, "velocidad_viento", 5, True)
    vmenos = top_n_ciudades(observaciones, "velocidad_viento", 5, False)

    print("\n--- Extremos ---")
    if len(calidas) > 0:
        print("Máxima:", calidas[0][0], "-", calidas[0][1], "°C")
    if len(frias) > 0:
        print("Mínima:", frias[0][0], "-", frias[0][1], "°C")
    if len(vmas) > 0:
        print("Viento máx:", vmas[0][0], "-", vmas[0][1], "km/h")
    if len(vmenos) > 0:
        print("Viento mín:", vmenos[0][0], "-", vmenos[0][1], "km/h")

    print("\n--- Top 5 Cálidas ---")
    for ciudad, temp in calidas:
        print(" ", ciudad, ":", temp, "°C")

    print("\n--- Top 5 Frías ---")
    for ciudad, temp in frias:
        print(" ", ciudad, ":", temp, "°C")

    print("\n--- Top 5 Más Viento ---")
    for ciudad, vel in vmas:
        print(" ", ciudad, ":", vel, "km/h")

    print("\n--- Top 5 Menos Viento ---")
    for ciudad, vel in vmenos:
        print(" ", ciudad, ":", vel, "km/h")

