Trabajo Practico 1
Estudiante: Esteban Mezei
Observaciones Meteorologicas SMN
Programacion 1 - Comision 2

Programa en Python para procesar los datos en vivo del Servicio Meteorologico Nacional, parsear cada registro y mostrar las estadisticas principales del clima.

################
Como usarlo

1 Descargar el archivo
Entrar a la pagina del SMN en https://www.smn.gob.ar/descarga-de-datos y bajar el comprimido de observaciones actuales en "Estado del tiempo".

Descomprimirlo y guardar el archivo txt dentro de la carpeta datos con el nombre observaciones_smn.txt.

2 Ejecutar la herramienta
En la terminal correr el comando python analisis_smn.py datos/observaciones_smn.txt.

################
Estructura del proyecto

#Carpeta principal

Archivo .gitignore
Archivo README.md
Archivo analisis_smn.py
Archivo archivodeprueba.ipynb
Archivo funciones_smn.py

#Carpeta datos
Archivo datos/estado_tiempo20260910.txt

################
Ejemplo de salida en consola:


=== RESUMEN METEOROLÓGICO ===
Total ciudades: 121
Ciudades completas: 25
Líneas inválidas: 0
Horarios de reporte: 09:00, 10:00, 11:00, 12:00, 13:00, 15:00

--- Datos Faltantes ---
- sensacion_termica : 96 | ejemplos: Azul, Bahía Blanca, Benito Juárez, Bolívar, Campo de Mayo

--- Extremos ---
Máxima: Rivadavia - 28.0 °C
Mínima: Base Belgrano II - -28.6 °C
Viento máx: Mount Pleasant Airport (Islas Malvinas) - 42 km/h
Viento mín: Base Carlini - 0 km/h

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
Mount Pleasant Airport (Islas Malvinas) : 42 km/h
Perito Moreno : 38 km/h
San Julián : 37 km/h
Río Gallegos : 37 km/h
Comodoro Rivadavia : 33 km/h

--- Top 5 Menos Viento ---
Base Carlini : 0 km/h
Bolívar : 0 km/h
Cipolletti : 0 km/h
Gobernador Gregores : 0 km/h
Mar del Plata : 0 km/h



