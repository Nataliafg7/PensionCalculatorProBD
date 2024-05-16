# Pension Calculator

# Definición de excepciones
class EdadNegativa(Exception):
    """Excepción lanzada cuando la edad es negativa."""


class SaldoNegativo(Exception):
    """Excepción lanzada cuando el saldo es negativo."""


class RentabilidadNegativa(Exception):
    """Excepción lanzada cuando la rentabilidad es negativa."""


class AdministracionNegativa(Exception):
    """Excepción lanzada cuando la administración es negativa."""


class SemanasInsuficientes(Exception):
    """Excepción lanzada cuando las semanas laboradas son insuficientes."""


class EdadInsuficiente(Exception):
    """Excepción lanzada cuando la edad es insuficiente para jubilarse."""


class RentabilidadSuperiorCien(Exception):
    """Excepción lanzada cuando la rentabilidad supera el 100%."""


class SemanasNegativas(Exception):
    """Excepción lanzada cuando las semanas laboradas son negativas."""


class SexoInvalido(Exception):
    """Excepción lanzada cuando el sexo no es 'mujer' o 'hombre'."""

""" La clase `PensionEstimada` evalúa la pensión estimada de una persona basándose en su edad, género, historial laboral y parámetros financieros. Primero, valida los datos ingresados y luego realiza los cálculos necesarios para estimar la pensión. """
class PensionEstimada:
    def __init__(self, edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo,
                 tasa_administracion):
        """Inicializa los parámetros necesarios para calcular la pensión."""
        self.edad_actual = edad_actual
        self.sexo = sexo
        self.salario_actual = salario_actual
        self.semanas_laboradas = semanas_laboradas
        self.ahorro_actual = ahorro_actual
        self.rentabilidad_fondo = rentabilidad_fondo
        self.tasa_administracion = tasa_administracion

    def _validar_edad(self):
        """Valida que la edad sea mayor o igual a 18 años."""
        if self.edad_actual < 18:
            raise EdadNegativa(
                "La edad mínima para calcular la pensión es de 18 años")

    def _validar_semanas_laboradas(self):
        """Valida que las semanas laboradas sean positivas y suficientes."""
        if self.semanas_laboradas < 0:
            raise SemanasNegativas(
                "Las semanas laboradas no pueden ser negativas")
        if self.semanas_laboradas < 700:
            raise SemanasInsuficientes(
                "Las semanas laboradas son insuficientes")

    def _validar_ahorro_actual(self):
        """Valida que el saldo actual sea positivo."""
        if self.ahorro_actual < 0:
            raise SaldoNegativo("El saldo no puede ser negativo")

    def _validar_rentabilidad_fondo(self):
        """Valida que la rentabilidad del fondo sea válida."""
        if self.rentabilidad_fondo < 0:
            raise RentabilidadNegativa(
                "La rentabilidad del fondo no puede ser negativa")
        if self.rentabilidad_fondo > 100:
            raise RentabilidadSuperiorCien(
                "La rentabilidad del fondo no puede ser mayor al 100%")

    def _validar_tasa_administracion(self):
        """Valida que la tasa de administración sea válida."""
        if self.tasa_administracion < 0:
            raise AdministracionNegativa(
                "La tasa de administración del fondo no puede ser negativa")

    def _validar_edad_jubilacion(self):
        """Valida que la edad actual sea suficiente para jubilarse."""
        if self.edad_actual >= 57 and self.sexo == "mujer":
            raise EdadInsuficiente("La mujer ya debería haberse jubilado")
        if self.edad_actual > 62 and self.sexo == "hombre":
            raise EdadInsuficiente("El hombre ya debería haberse jubilado")
        if self.sexo not in {"mujer", "hombre"}:
            raise SexoInvalido("El sexo debe ser 'mujer' o 'hombre'")

    def calcular_pension(self):
        """Calcula la pensión esperada."""
        self._validar_edad()
        self._validar_semanas_laboradas()
        self._validar_ahorro_actual()
        self._validar_rentabilidad_fondo()
        self._validar_tasa_administracion()
        self._validar_edad_jubilacion()

        años_restantes = 57 - self.edad_actual if self.sexo == "mujer" else 62 - self.edad_actual
        valor_ahorro_pensional_esperado = self.ahorro_actual * \
            ((1 + self.rentabilidad_fondo / 100) ** años_restantes)
        valor_pension_anual = valor_ahorro_pensional_esperado * \
            ((self.rentabilidad_fondo - self.tasa_administracion) / 100)
        valor_pension_mensual = valor_pension_anual / 12

        return valor_ahorro_pensional_esperado, valor_pension_anual, valor_pension_mensual
