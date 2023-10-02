<p align="center">
  <img src="https://camo.githubusercontent.com/a58601f5f61b883cff2da374ec3e1b1b14596a5083ffb4e2dcbd8c0fb8e4fca3/68747470733a2f2f73656c656e69756d2d707974686f6e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031372f31312f63726f707065642d6c6f676f2d6d696e692e706e67" alt="Logo del Proyecto">
</p>

# PYTHON + SELENIUM + PYTEST WITH POM

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Selenium Version](https://img.shields.io/badge/selenium-4.x-green.svg)](https://pypi.org/project/selenium/)
[![Pytest Version](https://img.shields.io/badge/pytest-7.x-red.svg)](https://docs.pytest.org/en/latest/)
[![Openpyxl Version](https://img.shields.io/badge/openpyxl-3.x-orange.svg)](https://openpyxl.readthedocs.io/en/stable/)

## Acerca de

Este proyecto es un marco de automatización de pruebas bajo la estructura Page Object Model (POM) construido con Python, Selenium, Pytest y las bibliotecas "openpyxl" para la lectura de archivos Excel y "logging" para el registro de eventos.

### Características Principales

- **Estructura POM:** Organización de las pruebas de manera eficiente y mantenible utilizando el Modelo de Objetos de Página.
- **Automatización de Pruebas:** Automatización construida bajo Selenium WebDriver.
- **Gestión de Pruebas:** Utilización de Pytest para crear y ejecutar casos de pruebas, setups y manejo data de manera eficiente.
- **Lectura de Datos:** Mapeo de datos directamente desde archivos Excel mediante la biblioteca "openpyxl".
- **Registro de Eventos:** Seguimiento de eventos importantes con la biblioteca "logging".

## Requisitos de Instalación

Asegúrate de tener Python 3.x instalado. Puedes descargarlo [aquí](https://www.python.org/downloads/release).

Instala las dependencias usando pip:

```bash
pip install selenium pytest openpyxl
```

## Ejecución de Pruebas desde la Consola

Puedes ejecutar las pruebas desde la consola utilizando el siguiente comando:

```bash
py.test --browser_name "chrome" --url "prd" --html=$WORKSPACE/reports/report.html
```

Asegúrate de reemplazar los valores "chrome" y "prd" con las opciones específicas que desees para el navegador y la URL de destino. 