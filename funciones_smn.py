from datetime import datetime

MESES = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

def separar_viento(campo: str) -> tuple:
    """Convierte un campo de viento en dirección y velocidad."""
    palabras = campo.strip().split()

    if len(palabras) >= 2 and palabras[-1].isdigit():
        return " ".join(palabras[:-1]), int(palabras[-1])
    
    return campo.strip(), 0

def parsear_fecha_hora(fecha, hora):
    """Convierte una fecha y hora del SMN en un datetime."""
    dia, mes, anio = fecha.split("-")
    h, m = hora.split(":")
    return datetime(int(anio), MESES[mes.lower()], int(dia), int(h), int(m))

def horarios_reportados(observaciones: dict) -> list:
    """Devuelve los horarios sin repetir y ordenados."""
    horarios = []

    for datos in observaciones.values():
        hora = datos["fecha_hora"].strftime("%H:%M")
        if hora not in horarios:
            horarios.append(hora)

    horarios.sort()
    return horarios

def leer_observaciones(ruta: str) -> dict:
    """Lee el archivo de observaciones del SMN y devuelve un diccionario
    {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    ya separado en dirección y velocidad."""
    observaciones = {}
    lineas_invalidas = 0

    with open(ruta, "r", encoding="latin-1") as archivo:
        for linea in archivo:
            campos = linea.strip().replace("/", "").split(";")

            if len(campos) != 10:
                lineas_invalidas += 1
                continue

            direccion, velocidad = separar_viento(campos[8])
            observaciones[campos[0].strip()] = {
                "fecha_hora": parsear_fecha_hora(campos[1].strip(), campos[2].strip()),
                "condicion": campos[3].strip(),
                "visibilidad": campos[4].strip(),
                "temperatura": float(campos[5]),
                "sensacion_termica": None if campos[6].lower() == "no se calcula" else float(campos[6]),
                "humedad": float(campos[7]),
                "direccion_viento": direccion,
                "velocidad_viento": velocidad,
                "presion": float(campos[9])
            }
    return observaciones, lineas_invalidas

def cantidad_ciudades(observaciones: dict) -> int:
    """Devuelve la cantidad total de ciudades leídas."""
    return len(observaciones)

def cantidad_ciudades_completas(observaciones: dict) -> int:
    """Devuelve la cantidad de ciudades sin ningún dato faltante."""
    return sum(None not in datos.values() for datos in observaciones.values())

def top_n_ciudades(observaciones: dict, campo: str, n: int, descendente: bool = True) -> list:
    """Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor
    (o al revés si descendente=False), en una lista. Reutilizable tanto para temperatura
    como para viento."""
    valores = []
    for ciudad, datos in observaciones.items():
        if datos[campo] is not None:
            valores.append((datos[campo], ciudad))

    valores.sort(reverse=descendente)
    return [(ciudad, valor) for valor, ciudad in valores[:n]]

def mostrar_resumen(observaciones: dict, lineas_invalidas: int) -> None:
    """Imprime por pantalla el resumen con todas las características calculadas. Usar n=5"""
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

    faltantes = {}

    for ciudad, datos in observaciones.items():
        for campo, valor in datos.items():
            if valor is None:
                if campo not in faltantes:
                    faltantes[campo] = []
                faltantes[campo].append(ciudad)

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
        print("Máxima:", calidas[0][0], "-", calidas[0][1], "°C")

    if frias:
        print("Mínima:", frias[0][0], "-", frias[0][1], "°C")

    if viento_max:
        print("Viento máx:", viento_max[0][0], "-", viento_max[0][1], "km/h")

    if viento_min:
        print("Viento mín:", viento_min[0][0], "-", viento_min[0][1], "km/h")

    print("\n--- Top 5 Cálidas ---")
    for ciudad, valor in calidas:
        print(ciudad, ":", valor, "°C")

    print("\n--- Top 5 Frías ---")
    for ciudad, valor in frias:
        print(ciudad, ":", valor, "°C")

    print("\n--- Top 5 Más Viento ---")
    for ciudad, valor in viento_max:
        print(ciudad, ":", valor, "km/h")

    print("\n--- Top 5 Menos Viento ---")
    for ciudad, valor in viento_min:
        print(ciudad, ":", valor, "km/h")