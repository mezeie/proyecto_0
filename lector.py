from datetime import datetime


def separar_viento(campo_viento: str) -> tuple:
    """Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
    Contempla el caso 'Calma' (sin velocidad numérica)."""
    campo_viento = campo_viento.strip()

    if campo_viento == "" or campo_viento.lower() == "no se calcula":
        return (None, None)

    if campo_viento.lower() == "calma":
        return ("Calma", 0)

    palabras = campo_viento.split()

    if palabras and palabras[-1].isdigit():
        velocidad = int(palabras[-1])
        direccion = " ".join(palabras[:-1])
        return (direccion, velocidad)

    return (campo_viento, None)


def leer_observaciones(ruta: str) -> tuple:
    """Lee el archivo de observaciones del SMN y devuelve una tupla con:
    - El diccionario {ciudad: datos}
    - La cantidad de líneas inválidas encontradas."""

    observaciones = {}
    lineas_invalidas = 0

    MESES = {
        "enero": 1, "febrero": 2, "marzo": 3,
        "abril": 4, "mayo": 5, "junio": 6, "julio": 7,
        "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11,
        "diciembre": 12,
    }

    try:
        with open(ruta, "r", encoding="latin-1") as archivo:
            for linea in archivo:
                linea = linea.strip()

                if not linea:
                    continue

                if linea[-1] == "/":
                    linea = linea[:-1].strip()

                campos = linea.split(";")

                # asegurar de que la línea tenga exactamente 10 campos
                if len(campos) != 10:
                    lineas_invalidas += 1
                    continue

                ciudad = campos[0].strip()

                # parseo de fecha con datetie
                fecha_texto = campos[1].strip()
                partes_fecha = fecha_texto.split("-")
                if len(partes_fecha) == 3:
                    try:
                        dia = int(partes_fecha[0])
                        mes = MESES.get(partes_fecha[1].lower(), 1)
                        anio = int(partes_fecha[2])
                        fecha_parseada = datetime(anio, mes, dia).date()
                    except ValueError:
                        fecha_parseada = None
                else:
                    fecha_parseada = None

                # temperatura a número (o None si no se calcula)
                temp_texto = campos[5].strip()
                if temp_texto.lower() == "no se calcula":
                    temp = None
                else:
                    try:
                        temp = float(temp_texto)
                    except ValueError:
                        temp = None

                # sensación térmica a número (o None si no se calcula)
                st_texto = campos[6].strip()
                if st_texto.lower() == "no se calcula":
                    sensacion = None
                else:
                    try:
                        sensacion = float(st_texto)
                    except ValueError:
                        sensacion = None

                # separar la dirección y velocidad del viento
                dir_viento, vel_viento = separar_viento(campos[8])

                # Guardado de info en diccionario
                observaciones[ciudad] = {
                    "fecha": fecha_parseada,
                    "hora": campos[2].strip(),
                    "condicion": campos[3].strip(),
                    "visibilidad": campos[4].strip(),
                    "temperatura": temp,
                    "sensacion_termica": sensacion,
                    "humedad": campos[7].strip(),
                    "direccion_viento": dir_viento,
                    "velocidad_viento": vel_viento,
                    "presion": campos[9].strip(),
                }

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
        return {}, 0

    return observaciones, lineas_invalidas