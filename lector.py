from datetime import datetime

MESES = {m: i + 1 for i, m in enumerate([
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
])}

def a_numero(val: str):
    """Convierte un string a float o devuelve None si no es numérico o no se calcula."""
    try:
        return float(val)
    except ValueError:
        return None
    
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


def leer_observaciones(ruta: str) -> tuple:
    """Lee el archivo de observaciones del SMN y devuelve una tupla con:
    - El diccionario {ciudad: datos}
    - La cantidad de líneas inválidas encontradas."""

    observaciones = {}
    lineas_invalidas = 0

    try:
        with open(ruta, "r", encoding="latin-1") as archivo:
            for linea in archivo:
                linea = linea.strip().rstrip("/")
                if not linea:
                    continue

                campos = [c.strip() for c in linea.split(";")]
                if len(campos) != 10:
                    lineas_invalidas += 1
                    continue

                # Parseo de fecha simple
                p_fecha = campos[1].split("-")
                fecha = None
                if len(p_fecha) == 3:
                    try:
                        fecha = datetime(int(p_fecha[2]), MESES.get(p_fecha[1].lower(), 1), int(p_fecha[0])).date()
                    except ValueError:
                        pass

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
                    "presion": campos[9],
                }
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
        return {}, 0

    return observaciones, lineas_invalidas