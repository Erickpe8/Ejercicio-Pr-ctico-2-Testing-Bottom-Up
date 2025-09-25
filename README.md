# Ejercicio Práctico 2: Testing Bottom Up – Sistema de Nómina

## Descripción
Este proyecto implementa un **Sistema de Cálculo de Nómina**, probado con enfoque **Bottom Up**.  
Se parte de módulos base (cálculo de impuestos, bonos y deducciones) y, mediante **drivers de prueba**, se validan de forma unitaria.  
Posteriormente, se integran progresivamente en el sistema de nómina para comprobar el cálculo de la **nómina neta**.

## Requisitos
- Python 3.8+
- pytest (`pip install pytest`)
- pytest-cov (`pip install pytest-cov`) *(opcional, para generar reportes de cobertura)*

## Estructura
```
proyecto_nomina/
├── modulos/
│   ├── calculadora_impuestos.py
│   ├── calculadora_bonos.py
│   └── calculadora_deducciones.py
├── drivers/
│   └── test_driver.py
├── nomina_sistema.py
└── test_bottom_up.py
```

## Ejecución de pruebas
Dentro de la carpeta del proyecto, ejecutar:

```bash
python -m pytest -v --tb=short
```

### Niveles de prueba
- **Nivel 1 (Bottom-Up):** probar módulos base  
  ```bash
  python -m pytest test_bottom_up.py::TestNivelBase -v
  ```
- **Nivel 2 (Integración):** probar sistema completo  
  ```bash
  python -m pytest test_bottom_up.py::TestIntegracion -v
  ```

## Cobertura
Si cuentas con `pytest-cov`, puedes generar el reporte de cobertura en HTML:

```bash
python -m pytest --cov=modulos --cov-report=html
```

El reporte quedará disponible en la carpeta `htmlcov/index.html`.

## Resultados esperados
Todas las pruebas deben pasar mostrando `PASSED`.  
El reporte de cobertura debe reflejar más del **80%** de cobertura en los módulos.

## Evidencia


---

## Autor
- Erick Sebastián Pérez Carvajal  
Ingeniería de Software – FESC, 2025
