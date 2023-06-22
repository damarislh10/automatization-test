import pandas as pd
from conexionDB import ConexionDB
import os

class FileMajority():
    def __init__(self):
        super().__init__()        

        # Instanciar base de datos
        self.base_datos = ConexionDB()

        # Directorio donde se encuentran los archivos CSV
        # self.directorio2 = 'C:/Users/ASUS/Documents/EmpresaAsiste/leadmayority'
        self.directorio2 = 'C:/Users/corte/OneDrive/Documentos/EmpresaAsiste/semanaMajority/filesLeads'
        self.archivos_csv = [archivo for archivo in os.listdir(self.directorio2) if archivo.endswith('.csv')]

    def leer_csv(self,archivo_csv):
            try:
                df = pd.read_csv(archivo_csv, sep=';')
           
                return df
            except pd.errors.EmptyDataError:
                print(f"El archivo CSV '{archivo_csv}' está vacío")
                return None
            except FileNotFoundError:
                print(f"El archivo CSV '{archivo_csv}' no existe")
                return None
        

    def procesar_datos(self):
            for archivo_csv in self.archivos_csv:
                ruta_archivo = os.path.join(self.directorio2, archivo_csv)
                df= self.leer_csv(ruta_archivo)
                
                if df is not None:
                    df = df.dropna()
                    registros = df.to_records(index=False)
                    valores = [(int(row['celular']), str(row['cedula'])) for row in registros]
                    print(valores)
                    self.base_datos.registerLeads(valores)

               

# Crear instancia de la clase FileMajority
file_majority = FileMajority()

# Ejecutar el procesamiento de los datos
file_majority.procesar_datos()


     
           

            