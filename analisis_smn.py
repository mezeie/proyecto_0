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
    observaciones, lineas_invalidas = leer_observaciones(ruta_archivo)
    mostrar_resumen(observaciones, lineas_invalidas)


if __name__ == "__main__":
    main()