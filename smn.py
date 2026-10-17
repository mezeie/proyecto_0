import os
import sys

from funciones_smn import (
    leer_observaciones,
    guardar_json,
    leer_json,
    contar_archivos,
    mostrar_cantidades,
    mostrar_resumen,
)


def main() -> None:
    if len(sys.argv) > 2:
        print("Error: Se debe indicar un solo archivo.")
        return

    if len(sys.argv) == 1:
        print("No se indicó ningún archivo.")
        print("Archivos TXT en datos/:", contar_archivos("datos", ".txt"))
        print("Archivos JSON en obs_json/:", contar_archivos("obs_json", ".json"))
        return

    ruta_archivo = sys.argv[1]
    extension = os.path.splitext(ruta_archivo)[1].lower()

    if extension == ".txt":
        print("Archivo del SMN, convirtiendo a json...")

        try:
            observaciones, lineas_invalidas, faltantes = leer_observaciones(ruta_archivo)

            if not observaciones:
                print("No se pudo leer ninguna observación válida.")
                return

            print("Lectura completada.")

            directorio = "obs_json"
            if not os.path.isdir(directorio):
                print("El directorio obs_json no existe, creándolo...")
                os.makedirs(directorio, exist_ok=True)
                print("Directorio creado correctamente.")

            nombre = os.path.splitext(os.path.basename(ruta_archivo))[0]
            ruta_json = os.path.join(directorio, nombre + ".json")

            print("Guardando archivo JSON...")
            guardar_json(observaciones, ruta_json)
            print("Conversión y guardado completados.")

            mostrar_cantidades(observaciones)

            print("\n")
            mostrar_resumen(observaciones, lineas_invalidas, faltantes)

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{ruta_archivo}'.")

        except (ValueError, KeyError, IndexError) as error:
            print(f"Error al procesar el archivo del SMN: {error}")

        except OSError as error:
            print(f"Error de lectura o escritura: {error}")

    elif extension == ".json":
        print("Archivo JSON, leyendo...")

        try:
            observaciones = leer_json(ruta_archivo)
            print("Lectura del JSON completada.")
            mostrar_cantidades(observaciones)

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{ruta_archivo}'.")

        except (ValueError, OSError) as error:
            print(f"Error al leer el archivo JSON: {error}")

    else:
        print("Error: El archivo debe tener extensión .txt o .json.")


if __name__ == "__main__":
    main()