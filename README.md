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

Estructura del proyecto

################
Carpeta principal

Archivo .gitignore
Archivo README.md
Archivo analisis_smn.py
Archivo archivodeprueba.ipynb
ARchivo estadisticas.py
ARchivo lector.py

#################
Carpeta datos
Archivo datos/estado_tiempo20260910.txt


Ejemplo de salida en consola

############################################

================ RESUMEN METEOROLOGICO ================
Total de ciudades leidas: 121
Ciudades con datos completos: 25
Lineas mal formadas o invalidas: 0

DATOS FALTANTES POR CAMPO
- sensacion_termica: 96 faltante(s) en Azul, Bahía Blanca, Benito Juárez, Bolívar, Campo de Mayo, Coronel Suarez, Dolores, El Palomar, Ezeiza, Junín, La Plata, Las Flores, Mar del Plata, Mariano Moreno, Merlo, Morón, Nueve de Julio, Olavarría, Pehuajó, Pigué, Punta Indio B.A., San Fernando, Tandil, Trenque Lauquen, Tres Arroyos, Villa Gesell, Aeroparque Buenos Aires, Buenos Aires, Catamarca, Tinogasta, Puerto Madryn, Trelew, Córdoba, Córdoba Observatorio, Esc. Aviación Militar, Laboulaye, Marcos Juárez, Pilar Obs., Río Cuarto, Villa Dolores, Villa María Del Río Seco, Corrientes, Ituzaingó, Mercedes, Monte Caseros, Paso De Los Libres, Concordia, Gualeguaychú, Paraná, Formosa, La Quiaca, Jujuy, Jujuy Universidad Nacional, General Pico, Victorica, Santa Rosa, Chamical, Chepes, Chilecito, La Rioja, Malargue, Mendoza, Mendoza Observatorio, San Martín (Mza), San Rafael, Uspallata, Bernardo De Irigoyen, Iguazú, Oberá, Posadas, Neuquén, Cipolletti, El Bolsón, Maquinchao, Río Colorado, Viedma, Metán, Salta, Jachal, San Juan, San Luis, Santa Rosa del Conlara, Villa Reynolds, Gobernador Gregores, Ceres, Rafaela, Reconquista, Rosario, Santa Fe, Sunchales, Venado Tuerto, Termas de Rio Hondo, Santiago del Estero, Tucumán, Base Esperanza, Base Carlini

VALORES EXTREMOS
Temperatura mas alta: Rivadavia con 28.0 °C
Temperatura mas baja: Base Belgrano II con -28.6 °C
Viento mas fuerte: Mount Pleasant Airport (Islas Malvinas) a 42 km/h
Viento mas suave: Base Carlini a 0 km/h

CIUDADES MAS CALIDAS
  Rivadavia: 28.0 °C
  Orán: 27.4 °C
  Pcia. Roque Saenz Peña: 26.7 °C
  Tartagal: 26.4 °C
  Resistencia: 26.3 °C

CIUDADES MAS FRIAS
  Base Belgrano II: -28.6 °C
  Base San Martín: -24.8 °C
  Base Orcadas: -24.3 °C
  Base Marambio: -15.5 °C
  Base Esperanza: -9.5 °C

CIUDADES CON MAS VIENTO
  Mount Pleasant Airport (Islas Malvinas): 42 km/h
  Perito Moreno: 38 km/h
  San Julián: 37 km/h
  Río Gallegos: 37 km/h
  Comodoro Rivadavia: 33 km/h

CIUDADES CON MENOS VIENTO
  Base Carlini: 0 km/h
  Bolívar: 0 km/h
  Cipolletti: 0 km/h
  Gobernador Gregores: 0 km/h
  Mar del Plata: 0 km/h
=======================================================

