# Ejercicio Práctico 2: Testing Bottom Up – Sistema de Nómina

## Descripción
Este proyecto implementa un **Sistema de Cálculo de Nómina**, probado con enfoque **Bottom Up**.  
Se parte de módulos base (cálculo de impuestos, bonos y deducciones) y, mediante **drivers de prueba**, se validan de forma unitaria.  
Posteriormente, se integran progresivamente en el sistema de nómina para comprobar el cálculo de la **nómina neta**.
<img width="1318" height="348" alt="image" src="https://github.com/user-attachments/assets/29ceddef-b991-45ed-91d1-038079b1f2c1" />


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
<img width="1808" height="398" alt="image" src="https://github.com/user-attachments/assets/ebedb5a8-670e-4678-ba0f-57be2e02cbce" />

<img width="918" height="509" alt="image" src="https://github.com/user-attachments/assets/e6da1c78-3ab9-4945-a4f6-cacc631b11d3" />
<img width="1500" height="503" alt="image" src="https://github.com/user-attachments/assets/fec78f20-f755-4ea0-bb56-a042e04dbbd7" />
<img width="1292" height="439" alt="image" src="https://github.com/user-attachments/assets/7cd461c0-88cd-4d21-bcc6-290930f33045" />





---

## Autor
- Erick Sebastián Pérez Carvajal  
Ingeniería de Software – FESC, 2025
