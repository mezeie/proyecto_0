# modulo principal
import sys
from funciones_smn import *


def main() -> None:
    """Funcion principal del programa."""
    if len(sys.argv) < 2:
        print("Error: Falta indicar la ruta del archivo de datos.")
        print("Uso correcto: python3 analisis_smn.py datos/estado_tiempo20260910.txt")
        sys.exit(1)

    ruta_archivo = sys.argv[1]

    try:
        observaciones, lineas_invalidas = leer_observaciones(ruta_archivo)
        mostrar_resumen(observaciones, lineas_invalidas)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta_archivo}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()