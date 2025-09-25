class CalculadoraBonos:
    """Módulo base para cálculo de bonos"""

    def calcular_bonos(self, empleado):
        rendimiento = empleado.get('rendimiento', 0)
        salario = empleado.get('salario_base', 0)
        if rendimiento >= 90:
            return salario * 0.10
        elif rendimiento >= 75:
            return salario * 0.05
        return 0.0
