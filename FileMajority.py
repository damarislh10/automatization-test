import pandas as pd
from connectionDB import ConnectionDB
import os

class FileMajority():
    def __init__(self):
        super().__init__()        

        # To instantiate a database
        self.data_base = ConnectionDB()

        # The directory where the CSV files are located
        # self.directorio2 = 'C:/Users/ASUS/Documents/EmpresaAsiste/leadmayority'
        self.directory2 = 'C:/Users/corte/OneDrive/Documentos/EmpresaAsiste/semanaMajority/filesLeads'
        self.files_csv = [file for file in os.listdir(self.directory2) if file.endswith('.csv')]

    def validate_csv(self,files_csv):
            try:
                df = pd.read_csv(files_csv, sep=';')
           
                return df
            except pd.errors.EmptyDataError:
                print(f"The CSV '{files_csv}' is empty")
                return None
            except FileNotFoundError:
                print(f"The CSV '{files_csv}' does not exist")
                return None
        

    def process_data(self):
            for file_csv in self.files_csv:
                file_path = os.path.join(self.directory2, file_csv)
                df= self.validate_csv(file_path)

                if df is not None:
                    df = df.dropna()
                    records = df.to_records(index=False)
                    values = [(int(row['celular']), str(row['cedula'])) for row in records]
                    self.data_base.registerLeads(values)

               

# Crear instancia de la clase FileMajority
file_majority = FileMajority()

# Ejecutar el procesamiento de los datos
file_majority.process_data()


     
           

            