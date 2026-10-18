from datetime import datetime
import os
import json

CAMPOS_ESPERADOS = [
    "ciudad", "fecha", "hora", "condicion del cielo", "visibilidad",
    "temperatura (c)", "sensacion termica (c)", "humedad", "viento", "presion (hPa)"
]

MESES = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}


def leer_lineas(ruta: str) -> tuple:
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.readlines(), "UTF-8"
    except UnicodeDecodeError:
        with open(ruta, "r", encoding="latin-1") as archivo:
            return archivo.readlines(), "Latin-1"


def separar_viento(campo: str) -> tuple:
    palabras = campo.strip().split()

    if len(palabras) >= 2 and palabras[-1].isdigit():
        return " ".join(palabras[:-1]), int(palabras[-1])
    
    return campo.strip(), None


def parsear_fecha_hora(fecha, hora):
    dia, mes, anio = fecha.split("-")
    h, m = hora.split(":")
    return datetime(int(anio), MESES[mes.lower()], int(dia), int(h), int(m))


def horarios_reportados(observaciones: dict) -> list:
    horarios = []

    for datos in observaciones.values():
        f_h = datos.get("fecha_hora")
        if f_h is not None:
            try:
                hora = f_h.strftime("%H:%M")
            except AttributeError:
                hora = f_h.split("T")[1]

            if hora not in horarios:
                horarios.append(hora)

    horarios.sort()
    return horarios


def leer_observaciones(ruta: str) -> tuple:
    observaciones = {}
    lineas_invalidas = 0
    faltantes = {}

    lineas, codificacion = leer_lineas(ruta)

    for linea in lineas:
        if not linea.strip():
            continue

        campos = linea.strip().replace("/", "").split(";")

        if len(campos) != len(CAMPOS_ESPERADOS):
            lineas_invalidas += 1
            continue

        direccion, velocidad = separar_viento(campos[8])

        try:
            fecha_hora = parsear_fecha_hora(campos[1].strip(), campos[2].strip())
        except (ValueError, KeyError):
            fecha_hora = None

        try:
            temperatura = float(campos[5])
        except ValueError:
            temperatura = None

        try:
            sensacion_termica = (None if campos[6].strip().lower() == "no se calcula" else float(campos[6]))
        except ValueError:
            sensacion_termica = None

        try:
            humedad = float(campos[7].strip())
        except ValueError:
            humedad = None

        try:
            presion = float(campos[9].strip().split()[0])
        except ValueError:
            presion = None

        datos = {
            "condicion": campos[3].strip(),
            "visibilidad": campos[4].strip(),
            "temperatura": temperatura,
            "sensacion_termica": sensacion_termica,
            "humedad": humedad,
            "direccion_viento": direccion,
            "velocidad_viento": velocidad,
            "presion": presion,
            "fecha_hora": fecha_hora
        }

        ciudad = campos[0].strip()
        observaciones[ciudad] = datos

        for campo, valor in datos.items():
            if valor is None:
                if campo not in faltantes:
                    faltantes[campo] = []
                faltantes[campo].append(ciudad)

    return observaciones, lineas_invalidas, faltantes


def cantidad_ciudades(observaciones: dict) -> int:
    return len(observaciones)


def cantidad_ciudades_completas(observaciones: dict) -> int:
    return sum(None not in datos.values() for datos in observaciones.values())


def contar_ciudades_informadas(observaciones: dict) -> int:
    informadas = 0
    for datos in observaciones.values():
        if datos.get("temperatura") is not None:
            informadas += 1
    return informadas


def top_n_ciudades(observaciones: dict, campo: str, n: int, descendente: bool = True) -> list:
    pares = list(filter(lambda item: item[1].get(campo) is not None, observaciones.items()))
    pares.sort(key=lambda item: item[1][campo], reverse=descendente)
    return [ciudad for ciudad, datos in pares[:n]]


def mostrar_resumen(observaciones: dict, lineas_invalidas: int, faltantes: dict) -> None:
    if not observaciones:
        print("No hay datos para mostrar.")
        return
    
    print("=== RESUMEN METEOROLÓGICO ===")
    print("Total ciudades:", cantidad_ciudades(observaciones))  
    print("Ciudades completas:", cantidad_ciudades_completas(observaciones))
    print("Líneas inválidas:", lineas_invalidas)
    horarios = horarios_reportados(observaciones)
    print(f"Horarios de reporte: {', '.join(horarios)}")

    print("\n--- Datos Faltantes ---")

    if not faltantes:
        print("Sin datos faltantes.")
    else:
        for campo, ciudades in faltantes.items():
            ejemplos = ", ".join(ciudades[:5])
            print("-", campo, ":", len(ciudades), "| ejemplos:", ejemplos)

    calidas = top_n_ciudades(observaciones, "temperatura", 5)
    frias = top_n_ciudades(observaciones, "temperatura", 5, False)
    viento_max = top_n_ciudades(observaciones, "velocidad_viento", 5)
    viento_min = top_n_ciudades(observaciones, "velocidad_viento", 5, False)

    print("\n--- Extremos ---")
    if calidas:
        ciudad = calidas[0]
        print("Máxima:", ciudad, "-", observaciones[ciudad]["temperatura"], "°C")

    if frias:
        ciudad = frias[0]
        print("Mínima:", ciudad, "-", observaciones[ciudad]["temperatura"], "°C")

    if viento_max:
        ciudad = viento_max[0]
        print("Viento máx:", ciudad, "-", observaciones[ciudad]["direccion_viento"], "-", observaciones[ciudad]["velocidad_viento"], "km/h")

    if viento_min:
        ciudad = viento_min[0]
        print("Viento mín:", ciudad, "-", observaciones[ciudad]["direccion_viento"], "-", observaciones[ciudad]["velocidad_viento"], "km/h")

    print("\n--- Top 5 Cálidas ---")
    for ciudad in calidas:
        print(ciudad, ":", observaciones[ciudad]["temperatura"], "°C")

    print("\n--- Top 5 Frías ---")
    for ciudad in frias:
        print(ciudad, ":", observaciones[ciudad]["temperatura"], "°C")

    print("\n--- Top 5 Más Viento ---")
    for ciudad in viento_max:
        print(ciudad, ":", "Viento", observaciones[ciudad]["direccion_viento"], "a", observaciones[ciudad]["velocidad_viento"], "km/h")

    print("\n--- Top 5 Menos Viento ---")
    for ciudad in viento_min:
        print(ciudad, ":", "Viento", observaciones[ciudad]["direccion_viento"], "a", observaciones[ciudad]["velocidad_viento"], "km/h")


def contar_archivos(carpeta: str, extension: str) -> int:
    if not os.path.isdir(carpeta):
        return 0

    cantidad = 0

    for nombre in os.listdir(carpeta):
        ruta = os.path.join(carpeta, nombre)
        nombre_archivo, extension_archivo = os.path.splitext(nombre)

        if extension_archivo.lower() == extension.lower():
            if os.path.isfile(ruta):
                cantidad += 1

    return cantidad


def guardar_json(observaciones: dict, ruta: str) -> None:
    datos_json = {}

    for ciudad, datos in observaciones.items():
        datos_json[ciudad] = datos.copy()

        f_h = datos_json[ciudad].get("fecha_hora")
        if f_h is not None:
            try:
                datos_json[ciudad]["fecha_hora"] = f_h.isoformat(timespec="minutes")
            except AttributeError:
                pass

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(
            datos_json,
            archivo,
            ensure_ascii=False,
            indent=4
        )


def leer_json(ruta: str) -> dict:
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def mostrar_cantidades(observaciones: dict) -> None:
    total = cantidad_ciudades(observaciones)
    informadas = contar_ciudades_informadas(observaciones)
    print(f"Ciudades que contiene el archivo: {total}")
    print(f"Ciudades informadas: {informadas}")