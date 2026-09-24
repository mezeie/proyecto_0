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
    if not observaciones:
        print("No hay datos para mostrar.")
        return

    print("=== RESUMEN METEOROLOGICO ===")
    print(f"Total ciudades: {cantidad_ciudades(observaciones)}")
    print(f"Ciudades completas: {cantidad_ciudades_completas(observaciones)}")
    print(f"Líneas inválidas: {lineas_invalidas}\n")

    print("--- Datos Faltantes ---")
    faltantes = datos_faltantes_por_campo(observaciones)
    if not faltantes:
        print("Sin datos faltantes.")
    else:
        for campo, info in faltantes.items():
            print(f"• {campo}: {info['cantidad']} en {', '.join(info['estaciones'])}")

    # Obtenemos los rankings de 5 elementos
    calidas = top_n_ciudades(observaciones, "temperatura", 5, True)
    frias = top_n_ciudades(observaciones, "temperatura", 5, False)
    vmas = top_n_ciudades(observaciones, "velocidad_viento", 5, True)
    vmenos = top_n_ciudades(observaciones, "velocidad_viento", 5, False)

    print("\n--- Extremos ---")
    if calidas: print(f"Máxima: {calidas[0][0]} ({calidas[0][1]} °C)")
    if frias: print(f"Mínima: {frias[0][0]} ({frias[0][1]} °C)")
    if vmas: print(f"Viento máx: {vmas[0][0]} ({vmas[0][1]} km/h)")
    if vmenos: print(f"Viento mín: {vmenos[0][0]} ({vmenos[0][1]} km/h)")

    print("\n--- Top 5 Cálidas ---")
    for c, t in calidas: print(f"  {c}: {t} °C")

    print("\n--- Top 5 Frías ---")
    for c, t in frias: print(f"  {c}: {t} °C")

    print("\n--- Top 5 Más Viento ---")
    for c, v in vmas: print(f"  {c}: {v} km/h")

    print("\n--- Top 5 Menos Viento ---")
    for c, v in vmenos: print(f"  {c}: {v} km/h")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Falta indicar la ruta del archivo de datos.")
        print("Uso correcto: python3 analisis_smn.py datos/estado_tiempo20260910.txt")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    observaciones, lineas_invalidas = leer_observaciones(ruta_archivo)
    mostrar_resumen(observaciones, lineas_invalidas)