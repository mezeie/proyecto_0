# modulo encargado de la lectura parseo y validacion del archivo del SMN
def separar_viento(campo_viento: str) -> tuple:
    """Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
    Contempla el caso 'Calma' (sin velocidad numérica)."""

    # si dice "calma" la velocidad es cero
    if campo_viento.lower() == "calma":
        return ("Calma", 0)

    palabras = campo_viento.split()

    ultima_palabra = palabras[-1]

    # verifica si esa última palabra es un número
    if ultima_palabra.isdigit():
        velocidad = int(ultima_palabra)

        # Ttodas las anteriores forman la direccion
        palabras_direccion = palabras[:-1]
        direccion = " ".join(palabras_direccion)

        return (direccion, velocidad)

    return (campo_viento, None)

def leer_observaciones(ruta: str) -> dict:
    """Lee el archivo de observaciones del SMN y devuelve un diccionario
    {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    ya separado en dirección y velocidad."""

    observaciones = {}

    # latin 1 para evitar problemas con acentos y ñ
    with open(ruta, "r", encoding="latin-1") as archivo:

        for linea in archivo:
            linea = linea.strip()

            # si la línea está vacía la salta
            if not linea:
                continue

            # si el ultimo caracter es / se saca
            if linea[-1] == "/":
                linea = linea[:-1].strip()

            
            campos = linea.split(";")

            # asegurar de que la línea tenga exactamente los 10 datos
            if len(campos) == 10:

                ciudad = campos[0].strip()

                # temperatura a número (o None si no se calcula)
                temp_texto = campos[5].strip()
                if temp_texto.lower() == "no se calcula":
                    temp = None
                else:
                    temp = float(temp_texto)

                # sensación térmica a número (o None si no se calcula)
                st_texto = campos[6].strip()
                if st_texto.lower() == "no se calcula":
                    sensacion = None
                else:
                    sensacion = float(st_texto)

                # separo la dirección y velocidad del viento con la funcion que hice antes
                dir_viento, vel_viento = separar_viento(campos[8])

                # guardado de info en diccionario
                observaciones[ciudad] = {
                    "fecha": campos[1].strip(),
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

    return observaciones
