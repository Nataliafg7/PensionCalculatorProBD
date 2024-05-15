import psycopg2

class PensionModelo:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='ep-red-sun-a20g8yxw.eu-central-1.aws.neon.tech',
            database='Pension',
            user='calcukara_owner',
            password='1lRELx0vMSgI'
        )
        self.cursor = self.conn.cursor()

    def crear_tabla(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS pension (
                id SERIAL PRIMARY KEY,
                edad_actual INTEGER NOT NULL,
                sexo VARCHAR(10) NOT NULL,
                salario_actual FLOAT NOT NULL,
                semanas_laboradas INTEGER NOT NULL,
                ahorro_actual FLOAT NOT NULL,
                rentabilidad_fondo FLOAT NOT NULL,
                tasa_administracion FLOAT NOT NULL
            );
        '''
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insertar_pension(self, datos_pension):
        insert_query = '''
            INSERT INTO pension (edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        '''
        self.cursor.execute(insert_query, datos_pension)
        self.conn.commit()

    def actualizar_pension(self, id_pension, datos_pension):
        update_query = '''
            UPDATE pension
            SET edad_actual=%s, sexo=%s, salario_actual=%s, semanas_laboradas=%s, ahorro_actual=%s, rentabilidad_fondo=%s, tasa_administracion=%s
            WHERE id=%s;
        '''
        datos_actualizar = datos_pension + (id_pension,)
        self.cursor.execute(update_query, datos_actualizar)
        self.conn.commit()

    def eliminar_pension(self, id_pension):
        delete_query = '''
            DELETE FROM pension
            WHERE id=%s;
        '''
        self.cursor.execute(delete_query, (id_pension,))
        self.conn.commit()

    def obtener_pension(self, id_pension):
        select_query = '''
            SELECT * FROM pension
            WHERE id=%s;
        '''
        self.cursor.execute(select_query, (id_pension,))
        return self.cursor.fetchone()
    
    def consultar_por_edad(self, edad_actual):
        select_query = '''
            SELECT * FROM pension
            WHERE edad_actual=%s;
        '''
        self.cursor.execute(select_query, (edad_actual,))
        return self.cursor.fetchall()

    def consultar_por_sexo(self, sexo):
        select_query = '''
            SELECT * FROM pension
            WHERE sexo=%s;
        '''
        self.cursor.execute(select_query, (sexo,))
        return self.cursor.fetchall()

    def consultar_por_salario(self, salario_actual):
        select_query = '''
            SELECT * FROM pension
            WHERE salario_actual=%s;
        '''
        self.cursor.execute(select_query, (salario_actual,))
        return self.cursor.fetchall()

    def consultar_por_semanas_laboradas(self, semanas_laboradas):
        select_query = '''
            SELECT * FROM pension
            WHERE semanas_laboradas=%s;
        '''
        self.cursor.execute(select_query, (semanas_laboradas,))
        return self.cursor.fetchall()

    def consultar_por_ahorro_actual(self, ahorro_actual):
        select_query = '''
            SELECT * FROM pension
            WHERE ahorro_actual=%s;
        '''
        self.cursor.execute(select_query, (ahorro_actual,))
        return self.cursor.fetchall()

    def consultar_por_rentabilidad_fondo(self, rentabilidad_fondo):
        select_query = '''
            SELECT * FROM pension
            WHERE rentabilidad_fondo=%s;
        '''
        self.cursor.execute(select_query, (rentabilidad_fondo,))
        return self.cursor.fetchall()

    def consultar_por_tasa_administracion(self, tasa_administracion):
        select_query = '''
            SELECT * FROM pension
            WHERE tasa_administracion=%s;
        '''
        self.cursor.execute(select_query, (tasa_administracion,))
        return self.cursor.fetchall()


    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()


    def verificar_existencia_registro(self, tabla, datos_registro):
        select_query = f"SELECT * FROM {tabla} WHERE id=%s;"  # Asumiendo que el primer valor de datos_registro es el ID
        self.cursor.execute(select_query, (datos_registro[0],))  # Suponiendo que el ID está en la primera posición
        return self.cursor.fetchone() is not None


    def verificar_conexion(self):
        return self.conn is not None
