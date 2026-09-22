# modulo principal
import sys
from lector import leer_observaciones
from estadisticas import (
    cantidad_ciudades,
    cantidad_ciudades_completas,
    datos_faltantes_por_campo,
    top_n_ciudades,
)


def mostrar_resumen(observaciones: dict, lineas_invalidas: int) -> None:
    """Imprime por pantalla el reporte meteorologico."""
    if not observaciones:
        print("No hay observaciones cargadas.")
        return

    print("================ RESUMEN METEOROLOGICO ================")
    print(f"Total de ciudades leidas: {cantidad_ciudades(observaciones)}")
    print(f"Ciudades con datos completos: {cantidad_ciudades_completas(observaciones)}")
    print(f"Lineas mal formadas o invalidas: {lineas_invalidas}\n")

    # Datos faltantes
    faltantes = datos_faltantes_por_campo(observaciones)
    print("DATOS FALTANTES POR CAMPO")
    if not faltantes:
        print("No se registraron datos faltantes.")
    else:
        for campo, info in faltantes.items():
            estaciones_str = ", ".join(info["estaciones"])
            print(f"- {campo}: {info['cantidad']} faltante(s) en {estaciones_str}")
    print()

    # Extremos (N=1)
    temp_max = top_n_ciudades(observaciones, "temperatura", 1, descendente=True)
    temp_min = top_n_ciudades(observaciones, "temperatura", 1, descendente=False)
    viento_max = top_n_ciudades(observaciones, "velocidad_viento", 1, descendente=True)
    viento_min = top_n_ciudades(observaciones, "velocidad_viento", 1, descendente=False)

    print("VALORES EXTREMOS")
    if temp_max:
        print(f"Temperatura mas alta: {temp_max[0][0]} con {temp_max[0][1]} °C")
    if temp_min:
        print(f"Temperatura mas baja: {temp_min[0][0]} con {temp_min[0][1]} °C")
    if viento_max:
        print(f"Viento mas fuerte: {viento_max[0][0]} a {viento_max[0][1]} km/h")
    if viento_min:
        print(f"Viento mas suave: {viento_min[0][0]} a {viento_min[0][1]} km/h")
    print()

    # Rankings N=5
    print("CIUDADES MAS CALIDAS")
    for ciudad, temp in top_n_ciudades(observaciones, "temperatura", 5, descendente=True):
        print(f"  {ciudad}: {temp} °C")

    print("\nCIUDADES MAS FRIAS")
    for ciudad, temp in top_n_ciudades(observaciones, "temperatura", 5, descendente=False):
        print(f"  {ciudad}: {temp} °C")

    print("\nCIUDADES CON MAS VIENTO")
    for ciudad, vel in top_n_ciudades(observaciones, "velocidad_viento", 5, descendente=True):
        print(f"  {ciudad}: {vel} km/h")

    print("\nCIUDADES CON MENOS VIENTO")
    for ciudad, vel in top_n_ciudades(observaciones, "velocidad_viento", 5, descendente=False):
        print(f"  {ciudad}: {vel} km/h")

    print("=======================================================")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Falta indicar la ruta del archivo de datos.")
        print("Uso correcto: python3 analisis_smn.py datos/estado_tiempo20260910.txt")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    observaciones, lineas_invalidas = leer_observaciones(ruta_archivo)
    mostrar_resumen(observaciones, lineas_invalidas)