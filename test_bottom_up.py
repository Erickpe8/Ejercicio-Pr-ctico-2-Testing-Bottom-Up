import pytest
from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_bonos import CalculadoraBonos
from drivers.test_driver import TestDriver
from nomina_sistema import NominaSistema

class TestNivelBase:
    """Nivel 1: Prueba módulos atómicos"""

    def setup_method(self):
        self.calc = CalculadoraImpuestos()
        self.driver = TestDriver(self.calc)

    def test_isr_salario_bajo(self):
        salario = 8000
        resultado = self.calc.calcular_isr(salario)
        assert resultado == 400  # 5%

    def test_isr_salario_medio(self):
        assert self.calc.calcular_isr(15000) == 1500  # 10%

    def test_isr_salario_alto(self):
        assert self.calc.calcular_isr(30000) == 4500  # 15%

    def test_seguro_social(self):
        assert self.calc.calcular_seguro_social(10000) == 625  # 6.25%

    def test_driver_sobre_modulo_base(self):
        msg = self.driver.ejecutar_prueba_unitaria('calcular_isr', (10000,), 500)
        assert 'OK' in msg


class TestIntegracion:
    """Nivel 2: Integración de módulos ya probados"""

    def test_nomina_neta_con_bono_alto(self):
        sistema = NominaSistema()
        empleado = {'salario_base': 20000, 'rendimiento': 92, 'prestamos': 0, 'alimentacion': 0}
        neta = sistema.calcular_nomina_neta(empleado)
        # salario 20000 + bono 10% (2000) - isr 10% (2000) - seguro 6.25% (1250) = 18750
        assert abs(neta - 18750) < 0.01

    def test_nomina_neta_con_bono_medio_y_deducciones(self):
        sistema = NominaSistema()
        empleado = {'salario_base': 12000, 'rendimiento': 80, 'prestamos': 300, 'alimentacion': 200}
        neta = sistema.calcular_nomina_neta(empleado)
        # salario 12000 + bono 5% (600) - isr 10% (1200) - seguro 6.25% (750) - otras (500) = 10150
        assert abs(neta - 10150) < 0.01

    def test_nomina_neta_sin_bonos_con_deducciones(self):
        sistema = NominaSistema()
        empleado = {'salario_base': 9000, 'rendimiento': 60, 'prestamos': 100, 'alimentacion': 50}
        neta = sistema.calcular_nomina_neta(empleado)
        # salario 9000 + 0 - isr 5% (450) - seguro 6.25% (562.5) - otras (150) = 7837.5
        assert abs(neta - 7837.5) < 0.01
