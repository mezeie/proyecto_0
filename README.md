# Trabajo Práctico 1 — Proyecto 0 y 0.1
**Estudiante:** Esteban Mezei  
**Materia:** Programación 1 — Comisión 2  
**Proyecto:** Procesamiento de Observaciones Meteorológicas del SMN 🇦🇷

---

## Descripción del Proyecto
Programa modular en Python desarrollado para interactuar con los datos en vivo del **Servicio Meteorológico Nacional (SMN)**. Permite leer, parsear registros meteorológicos, convertir y serializar datos a formato **JSON** (con codificación UTF-8 y fechas en estándar ISO 8601), y mostrar estadísticas y resúmenes completos del clima en la consola.

---

## Estructura del Proyecto

```text
proyecto_0/
 ┣ datos/
 ┃ ┗ estado_tiempo20260910.txt
 ┣ obs_json/                  # (Se genera automáticamente)
 ┃ ┗ estado_tiempo20260910.json
 ┣ analisis_smn.py            # Ejecutable Proyecto 0 (Análisis directo de .txt)
 ┣ smn.py                     # Ejecutable Proyecto 0.1 (Gestión .txt / .json)
 ┣ funciones_smn.py           # Librería central con la lógica y parseo
 ┗ README.md

Cómo Utilizarlo
1- Preparación de los datos

   1. Ingresar a la descarga de datos del SMN y obtené las observaciones actuales en formato "Estado del tiempo".

    2. Colocar el archivo .txt resultante dentro de la carpeta datos/ (ej: datos/estado_tiempo20260910.txt).

2- Ejecución de Scripts en la Terminal

    Opción A — Análisis directo de archivo TXT (Proyecto 0):

    python3 analisis_smn.py datos/estado_tiempo20260910.txt

    Opción B — Conversión de TXT a JSON y resumen (Proyecto 0.1):

    python3 smn.py datos/estado_tiempo20260910.txt

    (Este comando crea la carpeta obs_json/ automáticamente si no existe).

    Opción C — Lectura directa de un archivo JSON (Proyecto 0.1):

    python3 smn.py obs_json/estado_tiempo20260910.json

    (Muestra en consola las cantidades de ciudades de forma compacta)

    Opción D — Validación de parámetros vacíos o excesivos:

    python3 smn.py

Ejemplos de Salida en Consola
1. Salida al procesar un archivo TXT (analisis_smn.py o conversión completa):

=== RESUMEN METEOROLÓGICO ===
Ciudades que contiene el archivo: 121
Ciudades informadas: 121


=== RESUMEN METEOROLÓGICO ===
Total ciudades: 121
Ciudades completas: 24
Líneas inválidas: 0
Horarios de reporte: 09:00, 10:00, 11:00, 12:00, 13:00, 15:00

--- Datos Faltantes ---
- sensacion_termica : 96 | ejemplos: Azul, Bahía Blanca, Benito Juárez, Bolívar, Campo de Mayo
- velocidad_viento : 11 | ejemplos: Bolívar, Mar del Plata, Olavarría, Pigué, Villa María Del Río Seco

--- Extremos ---
Máxima: Rivadavia - 28.0 °C
Mínima: Base Belgrano II - -28.6 °C
Viento máx: Mount Pleasant Airport (Islas Malvinas) - Sur - 42 km/h
Viento mín: Benito Juárez - Norte - 3 km/h

--- Top 5 Cálidas ---
Rivadavia : 28.0 °C
Orán : 27.4 °C
Pcia. Roque Saenz Peña : 26.7 °C
Tartagal : 26.4 °C
Resistencia : 26.3 °C

--- Top 5 Frías ---
Base Belgrano II : -28.6 °C
Base San Martín : -24.8 °C
Base Orcadas : -24.3 °C
Base Marambio : -15.5 °C
Base Esperanza : -9.5 °C

--- Top 5 Más Viento ---
Mount Pleasant Airport (Islas Malvinas) : Viento Sur a 42 km/h
Perito Moreno : Viento Este a 38 km/h
Río Gallegos : Viento Sudoeste a 37 km/h
San Julián : Viento Sudoeste a 37 km/h
Comodoro Rivadavia : Viento Sur a 33 km/h

--- Top 5 Menos Viento ---
Benito Juárez : Viento Norte a 3 km/h
Campo de Mayo : Viento Norte a 3 km/h
Las Flores : Viento Sur a 3 km/h
Mariano Moreno : Viento Norte a 3 km/h
Laboulaye : Viento Sur a 3 km/h


2. Salida al leer directamente un archivo JSON (smn.py):

Archivo JSON, leyendo...
Ciudades que contiene el archivo: 121
Ciudades informadas: 121