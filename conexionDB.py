import mysql.connector

modeDev = True
if modeDev:
    host = 'localhost'
else:
    host = '10.255.254.25'

class ConexionDB():
    def __init__(self):
        self.usuario = ''
        self.contraseña = ''
        self.host = host
        self.base_datos = ''
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

    def registerLeads(self, valores):
        
        # Conectar a la base de datos si aún no está conectado
        if not self.conexion:
            resultado_conexion = self.conectar()
            if not resultado_conexion["conexion"]:
                print("hola",resultado_conexion["msg"])
                return

        sql = '''INSERT INTO `api2` (celular, cedula) VALUES (%s, %s)'''
        sql_select = '''SELECT celular, cedula FROM `api2` WHERE celular = %s AND cedula =%s'''
       
        # Intentar consulta a base de datos
        try:
            cursor = self.conexion.cursor()

            for valor in valores: 
                cursor.execute(sql_select,valor)
                resultado = cursor.fetchone()

                if resultado is None:
                    cursor.execute(sql,valor)

            self.conexion.commit()
            cursor.close()
            print("Inserción en la base de datos completada")
        except Exception as e:
            return print("Error al insertar en la base de datos:", str(e))
