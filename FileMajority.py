import pandas as pd
from conexionDB import ConexionDB
# Directorio donde se encuentran los archivos CSV
# directorio = 'C:/Users/corte/OneDrive/Documentos/EmpresaAsiste/semanaMajority/automatization/e.csv'
#directorio = pd.read_csv('C:/Users/corte/OneDrive/Documentos/EmpresaAsiste/semanaMajority/automatization/e.csv', sep=",")

class FileMajority():
    def __init__(self):
        super().__init__()        # Instanciar base de datos
        self.base_datos = ConexionDB()
        # directorio2 = pd.read_csv('C:/Users/corte/OneDrive/Documentos/data.csv', sep=";")
        directorio2 = pd.read_csv('C:/Users/ASUS/Documents/data.csv', sep=";")
        
        dfcsv = pd.DataFrame(directorio2)
        dfcsv = dfcsv.dropna()
        
        lote_size = 1000  # Tamaño del lote de inserción
        total_filas = len(dfcsv)

        
        for i in range(0, total_filas ,lote_size): 
            fin = i + lote_size
            lote = dfcsv.iloc[i:fin]
            
            # Generar los valores de inserción
            valores = []
            for fila in lote.itertuples(index=False):
                valores.append(tuple(fila))

            self.base_datos.registerLeads(valores)
           

            