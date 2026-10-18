import sys
from funciones_smn import (
    leer_observaciones,
    mostrar_cantidades,
    mostrar_resumen
)

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 analisis_smn.py <archivo_txt>")
        return

    ruta_archivo = sys.argv[1]

    try:
        observaciones, lineas_invalidas, faltantes = leer_observaciones(ruta_archivo)
        mostrar_cantidades(observaciones)
        print("\n")
        mostrar_resumen(observaciones, lineas_invalidas, faltantes)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error al procesar el archivo del SMN: {e}")

if __name__ == "__main__":
    main()