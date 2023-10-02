<p align="center">
  <img src="https://tu-imagen-o-logo.png" alt="Logo del Proyecto">
</p>

# PYTHON + SELENIUM + PYTEST WITH POM

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/release)
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