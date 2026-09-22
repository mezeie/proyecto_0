Trabajo Practico 1
Estudiante: Esteban Mezei
Observaciones Meteorologicas SMN
Programacion 1 - Comision 2

Programa en Python para procesar los datos en vivo del Servicio Meteorologico Nacional, parsear cada registro y mostrar las estadisticas principales del clima.


Como usarlo

1 Descargar el archivo
Entrar a la pagina del SMN en https://www.smn.gob.ar/descarga-de-datos y bajar el comprimido de observaciones actuales. Descomprimirlo y guardar el archivo txt dentro de la carpeta datos con el nombre observaciones_smn.txt.

2 Ejecutar la herramienta
En la terminal correr el comando python analisis_smn.py datos/observaciones_smn.txt.


Ejemplo de salida en consola

############################################

RESUMEN METEOROLOGICO SMN

Estaciones leidas correctamente: 112
Estaciones con datos completos: 89
Lineas descartadas por error de formato: 1

Datos faltantes por campo:
Sensacion termica: 23 estaciones con el valor No se calcula

Valores extremos
Temperatura maxima: 28.4 C en Bernardo de Irigoyen
Temperatura minima: -2.1 C en Maquinchao
Viento mas fuerte: 48 km/h en Comodoro Rivadavia
Viento mas suave: 0 km/h en Formosa (Calma)

TOP 5 CIUDADES MAS CALIDAS
1 Bernardo de Irigoyen: 28.4 C
2 Puerto Iguazu: 27.8 C
3 Posadas: 27.1 C
4 Rivadavia: 26.5 C
5 Tartagal: 26.0 C

TOP 5 CIUDADES MAS FRIAS
1 Maquinchao: -2.1 C
2 Bariloche: -0.5 C
3 El Calafate: 0.2 C
4 Ushuaia: 1.0 C
5 Esquel: 1.8 C


Estructura del proyecto

Carpeta principal

Archivo .gitignore
Archivo README.md
Archivo analisis_smn.py
Archivo archivodeprueba.ipynb
ARchivo estadisticas.py
ARchivo lector.py

Carpeta datos
Archivo datos/estado_tiempo20260910.txt