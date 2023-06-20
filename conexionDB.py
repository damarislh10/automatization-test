import mysql.connector

modeDev = True
if modeDev:
    host = 'localhost'
else:
    host = '10.255.254.25'

class ConexionDB():
    def __init__(self):
        self.usuario = 'baq'
        self.contraseña = 'Asiste.2021'
        self.host = host
        self.base_datos = 'majority'
        self.auth_plugin = 'mysql_native_password'
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                user=self.usuario,
                password=self.contraseña,
                host=self.host,
                database=self.base_datos,
                auth_plugin=self.auth_plugin
            )
            print("Conectado a la base de datos")
            return {
                "conexion": True,
                "msg": "Conectado a la base de datos"
            }
        except Exception as e:
            print("Error al conectarse a la base de datos:", str(e))
            return {
                "conexion": False,
                "msg": "Error al conectarse a la base de datos"
            }

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("Desconectado de la base de datos")

    def registerLeads(self, celular, cedula):
        # Conectar a la base de datos si aún no está conectado
        if not self.conexion:
            self.conectar()

        datos = (celular, cedula)

        sql = '''INSERT INTO `api2` (celular, cedula) VALUES (%s, %s)'''

        # Intentar consulta a base de datos
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, datos)
            self.conexion.commit()
            cursor.close()
        except Exception as e:
            print("Error al insertar en la base de datos:", str(e))
        finally:
            # Desconectar de la base de datos después de la operación
            self.desconectar()