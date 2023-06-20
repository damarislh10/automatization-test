import os
import csv
import pandas as pd
# Directorio donde se encuentran los archivos CSV
# directorio = 'C:/Users/corte/OneDrive/Documentos/EmpresaAsiste/semanaMajority/automatization/e.csv'
#directorio = pd.read_csv('C:/Users/corte/OneDrive/Documentos/EmpresaAsiste/semanaMajority/automatization/e.csv', sep=",")
directorio2 = pd.read_csv('C:/Users/corte/OneDrive/Documentos/data.csv', sep=",")

dfcsv = pd.DataFrame(directorio2)
dfcsv = dfcsv.dropna()
print(dfcsv)


for i in range(len(dfcsv)): 

    print(i)

# Obtener la lista de archivos en el directorio
""" archivos_csv = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.csv')]

# Iterar sobre los archivos CSV
for archivo_csv in archivos_csv:
    ruta_archivo = os.path.join(directorio, archivo_csv)

    # Abrir el archivo CSV
    with open(ruta_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)

        # Leer cada fila del archivo CSV
        for fila in lector_csv:
            # Procesar la fila como desees
            # Por ejemplo, imprimir los valores de cada columna
            for columna in fila:
                print(columna)

            # Agregar aquí la lógica adicional que necesites para procesar cada fila

            # Fin del procesamiento de la fila

        # Fin del procesamiento del archivo CSV

    # Cerrar el archivo CSV

# Fin del p """