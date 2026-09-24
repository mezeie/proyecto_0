# modulo principal
import sys
from lector import leer_observaciones
from estadisticas import (
    cantidad_ciudades,
    cantidad_ciudades_completas,
    datos_faltantes_por_campo,
    top_n_ciudades,
)

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Falta indicar la ruta del archivo de datos.")
        print("Uso correcto: python3 analisis_smn.py datos/estado_tiempo20260910.txt")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    observaciones, lineas_invalidas = leer_observaciones(ruta_archivo)
    mostrar_resumen(observaciones, lineas_invalidas)