# Ejercicio Práctico 2: Testing Bottom Up – Sistema de Nómina

## Requisitos
- Python 3.8+
- pytest, pytest-cov (opcional para cobertura)

## Estructura
proyecto_nomina/
├── modulos/
│   ├── calculadora_impuestos.py
│   ├── calculadora_bonos.py
│   └── calculadora_deducciones.py
├── drivers/
│   └── test_driver.py
├── nomina_sistema.py
└── test_bottom_up.py

## Ejecutar pruebas
python -m pytest -v --tb=short

## Cobertura (si está disponible pytest-cov)
python -m pytest --cov=modulos --cov-report=html
