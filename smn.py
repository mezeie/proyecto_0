import sys
import os
from funciones_smn import (
    leer_observaciones,
    guardar_json,
    leer_json,
    mostrar_cantidades,
    mostrar_resumen,
    contar_archivos
)

def main():
    # Punto 12 y 13: Validación de cantidad de parámetros
    if len(sys.argv) < 2:
        print("Aviso: No se pasó ningún archivo por parámetro.")
        cant_txt = contar_archivos("datos", ".txt")
        cant_json = contar_archivos("obs_json", ".json")
        print(f"Archivos .txt en datos/: {cant_txt}")
        print(f"Archivos .json en obs_json/: {cant_json}")
        return
    elif len(sys.argv) > 2:
        print("Aviso: Se pasó más de un parámetro. Terminando sin hacer nada.")
        return

    ruta_archivo = sys.argv[1]
    
    try:
        extension = os.path.splitext(ruta_archivo)[1].lower()
    except Exception:
        print("Error: El nombre del archivo proporcionado no es válido.")
        return

    if extension == ".txt":
        print("Archivo del SMN, convirtiendo a json...")
        try:
            observaciones, lineas_invalidas, faltantes = leer_observaciones(ruta_archivo)
            print("Lectura completada.")

            carpeta_json = "obs_json"
            try:
                if not os.path.isdir(carpeta_json):
                    print(f"El directorio {carpeta_json} no existe, creándolo...")
                    os.makedirs(carpeta_json, exist_ok=True)
                    print("Directorio creado correctamente.")
            except Exception as e:
                print(f"Advertencia al crear el directorio de JSON: {e}")

            nombre_base = os.path.splitext(os.path.basename(ruta_archivo))[0]
            ruta_json = os.path.join(carpeta_json, f"{nombre_base}.json")

            print("Guardando archivo JSON...")
            guardar_json(observaciones, ruta_json)
            print("Conversión y guardado completados.")

            mostrar_cantidades(observaciones)
            print("\n")
            mostrar_resumen(observaciones, lineas_invalidas, faltantes)
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error al procesar el archivo del SMN: {e}")

    elif extension == ".json":
        print("Archivo JSON, leyendo...")
        try:
            if not os.path.exists(ruta_archivo):
                print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
                return

            observaciones = leer_json(ruta_archivo)
            # Al leer un .json, solo muestra las cantidades en a lo sumo 2 líneas (Punto 10)
            mostrar_cantidades(observaciones)
        except Exception as e:
            print(f"Error al procesar el archivo JSON: {e}")

    else:
        print(f"Formato de archivo no soportado: {extension}")

if __name__ == "__main__":
    main()