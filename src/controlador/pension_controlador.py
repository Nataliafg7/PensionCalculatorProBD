#controlador/pension_controlador
from modelo.pension_modelo import PensionModelo
from modelo.pension_Estimada import PensionEstimada


class PensionControlador:
    def __init__(self):
        self.modelo = PensionModelo()

    def crear_tabla(self):
        self.modelo.crear_tabla()
        print("Tabla 'pension' creada correctamente.")

    def insertar_pension(self, datos_pension):
        self.modelo.insertar_pension(datos_pension)
        print("Datos de pensión insertados correctamente.")

    def actualizar_pension(self, id_pension, datos_pension):
        # Verificar si la pensión con el ID especificado existe
        if not self.verificar_existencia_pension(id_pension):
            raise ValueError(f"No se encontró una pensión con el ID {id_pension}")

    def eliminar_pension(self, id_pension):
        self.modelo.eliminar_pension(id_pension)
        print(f"Datos de pensión con ID {id_pension} eliminados correctamente.")

    def verificar_existencia_pension(self, id_pension):
        # Lógica para verificar la existencia de la pensión
        pass

    def consultar_por_id(self, id_pension):
        pension = self.modelo.obtener_pension(id_pension)
        if pension:
            print("Datos de pensión:")
            print(pension)
        else:
            print(f"No se encontró ninguna pensión con ID {id_pension}.")

    def consultar_por_edad(self, edad_actual):
        resultados = self.modelo.consultar_por_edad(edad_actual)
        if resultados:
            print("Resultados de la consulta por edad:")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"No se encontraron resultados para la edad {edad_actual}.")

    def consultar_por_sexo(self, sexo):
        resultados = self.modelo.consultar_por_sexo(sexo)
        if resultados:
            print("Resultados de la consulta por sexo:")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"No se encontraron resultados para el sexo {sexo}.")

    def consultar_por_salario(self, salario_actual):
        resultados = self.modelo.consultar_por_salario(salario_actual)
        if resultados:
            print("Resultados de la consulta por salario actual:")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"No se encontraron resultados para el salario actual {salario_actual}.")

    def consultar_por_semanas_laboradas(self, semanas_laboradas):
        resultados = self.modelo.consultar_por_semanas_laboradas(semanas_laboradas)
        if resultados:
            print("Resultados de la consulta por número de semanas laboradas:")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"No se encontraron resultados para el número de semanas laboradas {semanas_laboradas}.")

    def consultar_por_ahorro_actual(self, ahorro_actual):
        resultados = self.modelo.consultar_por_ahorro_actual(ahorro_actual)
        if resultados:
            print("Resultados de la consulta por ahorro actual:")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"No se encontraron resultados para el ahorro actual {ahorro_actual}.")

    def consultar_por_rentabilidad_fondo(self, rentabilidad_fondo):
        resultados = self.modelo.consultar_por_rentabilidad_fondo(rentabilidad_fondo)
        if resultados:
            print("Resultados de la consulta por rentabilidad del fondo:")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"No se encontraron resultados para la rentabilidad del fondo {rentabilidad_fondo}.")

    def consultar_por_tasa_administracion(self, tasa_administracion):
        resultados = self.modelo.consultar_por_tasa_administracion(tasa_administracion)
        if resultados:
            print("Resultados de la consulta por tasa de administración del fondo:")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"No se encontraron resultados para la tasa de administración del fondo {tasa_administracion}.")

    def consultar_por_genero(self, genero):
        resultados = self.modelo.consultar_por_sexo(genero)
        if resultados:
            print("Resultados de la consulta por género:")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"No se encontraron resultados para el género {genero}.")

    def obtener_pension(self, id_pension):
        pension = self.modelo.obtener_pension(id_pension)
        if pension:
            print("Datos de pensión:")
            print(pension)
        else:
            print(f"No se encontró ninguna pensión con ID {id_pension}.")

    def validar_datos_pension(self, datos_pension):
        edad, genero, salario, cotizaciones, ahorro, tasa, tipo = datos_pension
        if edad < 0 or salario < 0 or cotizaciones < 0 or ahorro < 0 or tasa < 0 or tipo < 0:
            raise ValueError("Los valores no pueden ser negativos")
        if genero not in ['hombre', 'mujer']:
            raise ValueError("El género debe ser 'hombre' o 'mujer'")
        
    def calcular_pension_para_id(self, id_pension):
        pension = self.modelo.obtener_pension(id_pension)
        if pension:
            try:
                # Crear una instancia de PensionEstimada con los datos de la pensión obtenidos de la tabla
                # Excluir el primer elemento (ID de la pensión) de la lista de datos de la pensión
                pension_estimada = PensionEstimada(*pension[1:])
                # Calcular la pensión estimada
                valor_ahorro_pensional_esperado, valor_pension_anual, valor_pension_mensual = pension_estimada.calcular_pension()
                print("Resultados del cálculo de pensión:")
                print(f"Valor del ahorro pensional esperado: {valor_ahorro_pensional_esperado}")
                print(f"Valor de la pensión anual: {valor_pension_anual}")
                print(f"Valor de la pensión mensual: {valor_pension_mensual}")
            except Exception as e:
                print(f"No se pudo calcular la pensión para la pensión con ID {id_pension}. Error: {str(e)}")
        else:
            print(f"No se encontró ninguna pensión con ID {id_pension}.")

    def verificar_conexion(self):
        try:
            # Intenta realizar una operación simple con la base de datos
            # Por ejemplo, una consulta que siempre debería funcionar
            self.ejecutar_consulta("SELECT 1")
            return True
        except Exception as e:
            # Maneja cualquier excepción que indique un fallo en la conexión
            print(f"Error al verificar la conexión: {e}")
            return False


    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()
