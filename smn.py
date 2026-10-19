import sys
import os
from funciones_smn import (
    leer_observaciones,
    guardar_json,
    leer_json,
    mostrar_cantidades,
    contar_archivos
)

def main():
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

    if not os.path.exists(ruta_archivo):
        print(f"error: el archivo {ruta_archivo} no existe")
        return
    
    try:
        extension = os.path.splitext(ruta_archivo)[1].lower()
    except Exception:
        print("Error: El nombre del archivo proporcionado no es válido.")
        return

    if extension == ".txt":
        print("archivo del SMN, convirtiendo a json...")
        try:
            observaciones, lineas_invalidas, faltantes = leer_observaciones(ruta_archivo)

            carpeta_json = "obs_json"
            try:
                if not os.path.isdir(carpeta_json):
                    print(f"el directorio {carpeta_json} no existe, creándolo...")
                    os.makedirs(carpeta_json, exist_ok=True)
                    print("directorio creado.")
            except Exception as e:
                print(f"Advertencia al crear el directorio de JSON: {e}")

            nombre_base = os.path.splitext(os.path.basename(ruta_archivo))[0]
            ruta_json = os.path.join(carpeta_json, f"{nombre_base}.json")

            guardar_json(observaciones, ruta_json)
            
            mostrar_cantidades(observaciones)
            
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error al procesar el archivo del SMN: {e}")

    elif extension == ".json":
        print("archivo json, leyendo...")
        try:
            observaciones = leer_json(ruta_archivo)
            print("lectura completada")
            mostrar_cantidades(observaciones)
        except Exception as e:
            print(f"Error al procesar el archivo JSON: {e}")

    else:
        print(f"Formato de archivo no soportado: {extension}")

if __name__ == "__main__":
    main()