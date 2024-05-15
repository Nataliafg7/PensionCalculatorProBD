# pruebas/test_pension.py
import unittest
from unittest.mock import patch
from src.controlador.pension_controlador import *
from src.modelo.pension_modelo import *


class TestPension(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para cada prueba
        self.controlador = PensionControlador()
        self.id_pension = 1
        self.datos_pension = (30, 'hombre', 50000, 500, 10000, 5, 1)
    
    def tearDown(self):
        self.controlador.cerrar_conexion()

    def test_creacion_tabla(self):
        with patch('builtins.input', side_effect=["1"]):
            self.controlador.crear_tabla()

    def test_insercion_pension(self):
        datos_pension = (30, 'hombre', 50000, 500, 10000, 5, 1)
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
        datos_pension = (30, 'mujer', 50000.0, 800, 10000.0, 5.0, 1.0)
        self.controlador.insertar_pension(datos_pension)
        # Calcular la pensión para el ID correspondiente
        self.controlador.calcular_pension_para_id(1)
        # No hay una verificación específica aquí, simplemente se verifica que no se produzca un error durante el cálculo
    
    def test_excepcion_al_actualizar_pension_inexistente(self):
        datos_pension = (30, 'hombre', 50000, 500, 10000, 5, 1)
        with self.assertRaises(ValueError):  # Reemplaza ValueError con la excepción específica que lanza tu método
            self.controlador.actualizar_pension(999, datos_pension)
    
    def test_validacion_datos_pension(self):
        datos_invalidos = (30, 'alien', -50000, 500, 10000, 5, 1)
        with self.assertRaises(ValueError):
            self.controlador.validar_datos_pension(datos_invalidos)
            
    def test_rendimiento_insercion_masiva(self):
        for _ in range(100):
            datos_pension = (30, 'hombre', 50000, 500, 10000, 5, 1)
            self.controlador.insertar_pension(datos_pension)
        # Aquí podrías medir el tiempo de inserción y verificar que se mantenga dentro de un rango aceptable
    def test_conexion_base_datos(self):
        modelo = PensionModelo()
        conexion_exitosa = modelo.verificar_conexion()
        modelo.cerrar_conexion()
        self.assertTrue(conexion_exitosa, "La conexión con la base de datos debería ser exitosa")

if __name__ == '__main__':
    unittest.main()
