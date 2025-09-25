from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_bonos import CalculadoraBonos
from modulos.calculadora_deducciones import CalculadoraDeducciones

class NominaSistema:
    """Sistema integrado usando módulos ya probados"""

    def __init__(self):
        self.calc_impuestos = CalculadoraImpuestos()
        self.calc_bonos = CalculadoraBonos()
        self.calc_deducciones = CalculadoraDeducciones()

    def calcular_nomina_neta(self, empleado):
        salario = empleado['salario_base']
        isr = self.calc_impuestos.calcular_isr(salario)
        seguro = self.calc_impuestos.calcular_seguro_social(salario)
        bonos = self.calc_bonos.calcular_bonos(empleado)
        otras = self.calc_deducciones.calcular_otras_deducciones(empleado)
        return salario + bonos - isr - seguro - otras
