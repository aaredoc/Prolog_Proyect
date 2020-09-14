import psycopg2

class CastDB:
    def __init__(self, dni, nombres, apellidos, fecha, puntos_test):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha = fecha
        self.puntos_test = puntos_test
        self.conexion = psycopg2.connect(user='postgres',
                                         password='admin',
                                         host='localhost',
                                         port='5432',
                                         database='castsoftDB')
        self.cursor = self.conexion.cursor()

    def addBD(self):
        command = 'INSERT INTO paciente (dni, nombres, apellidos, fecha, puntos_test)'\
            'VALUES(%s, %s, %s, %s, %s)'
        values = (self.dni, self.nombres, self.apellidos, self.fecha, self.puntos_test)
        self.cursor.execute(command, values)
        self.conexion.commit()
    
    def updateDB(self):
        pass

    def getBD(self):
        command = 'SELECT * FROM paciente'
        self.cursor.execute(command)
        registros = self.cursor.fetchall()
        return registros

    
    def closeConexion(self):
        self.cursor.close()
        self.conexion.close()