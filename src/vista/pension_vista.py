#vista/pensionvista.py
import sys 
sys.path.append("src")
from controlador.pension_controlador import PensionControlador

class PensionVista:
    def __init__(self):
        self.controlador = PensionControlador()

    def mostrar_menu_principal(self):
        print("\nMenu Principal:")
        print("1. Crear tabla 'pension'")
        print("2. Insertar datos de pensión")
        print("3. Actualizar datos de pensión")
        print("4. Eliminar datos de pensión")
        print("5. Consultar datos de pensión")
        print("6. Calcular pensión para ID")
        print("7. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Ingrese el número de la opción que desea realizar: ")
            if opcion == "1":
                self.controlador.crear_tabla()
            elif opcion == "2":
                self.insertar_datos_pension()
            elif opcion == "3":
                self.actualizar_datos_pension()
            elif opcion == "4":
                self.eliminar_datos_pension()
            elif opcion == "5":
                self.menu_consultar()
            elif opcion == "6":
                self.calcular_pension_para_id()
            elif opcion == "7":
                print("¡Gracias por usar calculadorapro!")
                self.controlador.cerrar_conexion()
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def insertar_datos_pension(self):
        edad_actual = input("Ingrese su edad actual: ")
        sexo = input("Ingrese su sexo (mujer/hombre): ")
        salario_actual = input("Ingrese su salario actual: ")
        semanas_laboradas = input("Ingrese el número de semanas laboradas: ")
        ahorro_actual = input("Ingrese su ahorro actual: ")
        rentabilidad_fondo = input("Ingrese la rentabilidad del fondo (%): ")
        tasa_administracion = input("Ingrese la tasa de administración del fondo (%): ")
        datos_pension = (edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo,
                         tasa_administracion)
        self.controlador.insertar_pension(datos_pension)

    def actualizar_datos_pension(self):
        id_pension = input("Ingrese el ID de la pensión que desea actualizar: ")
        edad_actual = input("Ingrese su nueva edad actual: ")
        sexo = input("Ingrese su nuevo sexo (mujer/hombre): ")
        salario_actual = input("Ingrese su nuevo salario actual: ")
        semanas_laboradas = input("Ingrese el nuevo número de semanas laboradas: ")
        ahorro_actual = input("Ingrese su nuevo ahorro actual: ")
        rentabilidad_fondo = input("Ingrese la nueva rentabilidad del fondo (%): ")
        tasa_administracion = input("Ingrese la nueva tasa de administración del fondo (%): ")
        datos_pension = (edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo,
                         tasa_administracion)
        self.controlador.actualizar_pension(id_pension, datos_pension)


    def eliminar_datos_pension(self):
        id_pension = input("Ingrese el ID de la pensión que desea eliminar: ")
        self.controlador.eliminar_pension(id_pension)

    def consultar_datos_pension(self):
        id_pension = input("Ingrese el ID de la pensión que desea consultar: ")
        self.controlador.obtener_pension(id_pension)

    def calcular_pension_para_id(self):
        id_pension = input("Ingrese el ID de la pensión para calcular la pensión: ")
        try:
            id_pension = int(id_pension)
            self.controlador.calcular_pension_para_id(id_pension)
        except ValueError:
            print("El ID de la pensión debe ser un número entero.")


    def menu_consultar(self):
        while True:
            self.mostrar_menu_consulta()
            opcion = input("Ingrese el número de la opción que desea realizar: ")
            if opcion == "1":
                self.consultar_por_id()
            elif opcion == "2":
                self.consultar_por_edad()
            elif opcion == "3":
                self.consultar_por_sexo()
            elif opcion == "4":
                self.consultar_por_salario()
            elif opcion == "5":
                self.consultar_por_semanas_laboradas()
            elif opcion == "6":
                self.consultar_por_ahorro_actual()
            elif opcion == "7":
                self.consultar_por_rentabilidad_fondo()
            elif opcion == "8":
                self.consultar_por_tasa_administracion()
            elif opcion == "9":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def mostrar_menu_consulta(self):
        print("\nMenu de Consulta:")
        print("1. Consultar datos de pensión por ID")
        print("2. Consultar datos de pensión por edad")
        print("3. Consultar datos de pensión por sexo")
        print("4. Consultar datos de pensión por salario actual")
        print("5. Consultar datos de pensión por número de semanas laboradas")
        print("6. Consultar datos de pensión por ahorro actual")
        print("7. Consultar datos de pensión por rentabilidad del fondo")
        print("8. Consultar datos de pensión por tasa de administración del fondo")
        print("9. Volver al Menú Principal")

    def consultar_por_id(self):
        id_pension = input("Ingrese el ID de la pensión que desea consultar: ")
        self.controlador.consultar_por_id(id_pension)

    def consultar_por_edad(self):
        edad_actual = input("Ingrese la edad actual para buscar: ")
        self.controlador.consultar_por_edad(edad_actual)

    def consultar_por_sexo(self):
        sexo = input("Ingrese el sexo para buscar (mujer/hombre): ")
        self.controlador.consultar_por_sexo(sexo)

    def consultar_por_salario(self):
        salario_actual = input("Ingrese el salario actual para buscar: ")
        self.controlador.consultar_por_salario(salario_actual)

    def consultar_por_semanas_laboradas(self):
        semanas_laboradas = input("Ingrese el número de semanas laboradas para buscar: ")
        self.controlador.consultar_por_semanas_laboradas(semanas_laboradas)

    def consultar_por_ahorro_actual(self):
        ahorro_actual = input("Ingrese el ahorro actual para buscar: ")
        self.controlador.consultar_por_ahorro_actual(ahorro_actual)

    def consultar_por_rentabilidad_fondo(self):
        rentabilidad_fondo = input("Ingrese la rentabilidad del fondo para buscar (%): ")
        self.controlador.consultar_por_rentabilidad_fondo(rentabilidad_fondo)

    def consultar_por_tasa_administracion(self):
        tasa_administracion = input("Ingrese la tasa de administración del fondo para buscar (%): ")
        self.controlador.consultar_por_tasa_administracion(tasa_administracion)

    def calcular_pension_para_id(self):
        id_pension = input("Ingrese el ID de la pensión para calcular: ")
        self.controlador.calcular_pension_para_id(id_pension)

if __name__ == '__main__':
    vista = PensionVista()
    vista.ejecutar()
