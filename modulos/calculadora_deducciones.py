class CalculadoraDeducciones:
    """Módulo base para otras deducciones (ej. préstamos, alimentación)"""

    def calcular_otras_deducciones(self, empleado):
        prestamos = empleado.get('prestamos', 0.0)
        alimentacion = empleado.get('alimentacion', 0.0)
        return float(prestamos) + float(alimentacion)
