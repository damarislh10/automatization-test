import mysql.connector

modeDev = True
if modeDev:
    host = 'localhost'
else:
    host = '10.255.254.25'

class ConnectionDB():
    def __init__(self):
        self.user = 'baq'
        self.password = 'Asiste.2021'
        self.host = host
        self.data_base = 'majority'
        self.auth_plugin = 'mysql_native_password'
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.data_base,
                auth_plugin=self.auth_plugin
            )
            print("Connected to the database")
            return {
                "connection": True,
                "msg": "Connected to the database"
            }
        except Exception as e:
            print("Error connecting to the database:", str(e))
            return {
                "connection": False,
                "msg": "Error connecting to the database"
            }

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnecting to the database")

    def registerLeads(self, values):
          
        # To connect to the database if not already connected
        if not self.connection:
            connection_result = self.connect()
            if not connection_result["connection"]:
                print("Hello ",connection_result["msg"])
                return

        sql = '''INSERT INTO `api2` (celular, cedula) VALUES (%s, %s)'''
        sql_select = '''SELECT celular, cedula FROM `api2` WHERE celular = %s AND cedula =%s'''
       
        # Intentar consulta a base de datos
        try:
            cursor = self.connection.cursor()

            for value in values: 
                cursor.execute(sql_select,value)
                resultado = cursor.fetchone()

                if resultado is None:
                    cursor.execute(sql,value)

            self.connection.commit()
            cursor.close()
            print("Database insertion completed")
        except Exception as e:
            return print("Error inserting into the database:", str(e))
