# pruebas/test_pension.py
import sys 
sys.path.append("src")
import unittest
from unittest.mock import patch
from controlador.pension_controlador import *
from modelo.pension_modelo import *


class TestPension(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para cada prueba
        self.controlador = PensionControlador()
        self.id_pension = 1
    
    def tearDown(self):
        self.controlador.cerrar_conexion()

    def test_creacion_tabla(self):
        with patch('builtins.input', side_effect=["1"]):
            self.controlador.crear_tabla()

    def test_insercion_pension(self):
        # Datos de entrada
        edad = 56
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1150
        ahorro_actual = 250000000
        rentabilidad_fondo = 7
        tasa_administracion = 1
        datos_pension = (edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        with patch('builtins.input', side_effect=["2"]), patch('builtins.input', side_effect=datos_pension):
            self.controlador.insertar_pension(datos_pension)

    def test_eliminacion_pension(self):
        id_pension = 1
        with patch('builtins.input', side_effect=["4", id_pension]):
            self.controlador.eliminar_pension(id_pension)

    def test_consulta_pension_existente(self):
        id_pension = 1
        with patch('builtins.input', side_effect=["5", id_pension]):
            self.controlador.obtener_pension(id_pension)

    def test_consulta_pension_no_existente(self):
        id_pension = 999  # ID que no existe
        with patch('builtins.input', side_effect=["5", id_pension]):
            self.controlador.obtener_pension(id_pension)

    def test_calculo_pension_para_id(self):
        # Insertar datos de pensión válidos
        edad = 56
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1150
        ahorro_actual = 250000000
        rentabilidad_fondo = 7
        tasa_administracion = 1
        datos_pension = (edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        self.controlador.insertar_pension(datos_pension)
        # Calcular la pensión para el ID correspondiente
        self.controlador.calcular_pension_para_id(1)
        # No hay una verificación específica aquí, simplemente se verifica que no se produzca un error durante el cálculo
    
    def test_excepcion_al_actualizar_pension_inexistente(self):
        # Datos de entrada
        edad = 56
        sexo = "mujer"
        salario_actual = 0
        semanas_laboradas = 1150
        ahorro_actual = 250000000
        rentabilidad_fondo = 7
        tasa_administracion = 1
        datos_pension = (edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        with self.assertRaises(ValueError):  # Reemplaza ValueError con la excepción específica que lanza tu método
            self.controlador.actualizar_pension(999, datos_pension)
    
    def test_validacion_datos_pension(self):
        # Datos de entrada inválidos
        edad = 56
        sexo = "alien"  # Sexo inválido
        salario_actual = -50000  # Salario inválido
        semanas_laboradas = 1150
        ahorro_actual = 250000000
        rentabilidad_fondo = 7
        tasa_administracion = 1
        datos_invalidos = (edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
        with self.assertRaises(ValueError):
            self.controlador.validar_datos_pension(datos_invalidos)
            
    def test_rendimiento_insercion_masiva(self):
        for _ in range(100):
            # Datos de entrada
            edad = 56
            sexo = "mujer"
            salario_actual = 0
            semanas_laboradas = 1150
            ahorro_actual = 250000000
            rentabilidad_fondo = 7
            tasa_administracion = 1
            datos_pension = (edad, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
            self.controlador.insertar_pension(datos_pension)
        # Aquí podrías medir el tiempo de inserción y verificar que se mantenga dentro de un rango aceptable
    
    def test_conexion_base_datos(self):
        modelo = PensionModelo()
        conexion_exitosa = modelo.verificar_conexion()
        modelo.cerrar_conexion()
        self.assertTrue(conexion_exitosa, "La conexión con la base de datos debería ser exitosa")

if __name__ == '__main__':
    unittest.main()
