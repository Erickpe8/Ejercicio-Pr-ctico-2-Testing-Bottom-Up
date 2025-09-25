class TestDriver:
    __test__ = False  # Lo marque asi para que pytest no me lo pase como prueba, adjunto imagen en el reporte
    def __init__(self, modulo):
        self.modulo = modulo
        self.resultados = []

    def ejecutar_prueba_unitaria(self, metodo, parametros, esperado):
        resultado = getattr(self.modulo, metodo)(*parametros)
        exito = abs(resultado - esperado) < 0.01
        self.resultados.append({
            'metodo': metodo,
            'exito': exito,
            'resultado': resultado,
            'esperado': esperado
        })
        assert exito, f"Fallo: {resultado} != {esperado}"
        return f"✓ {metodo}: OK"
