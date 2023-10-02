import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

driver = None  # con None indicamos que la variable no lleva ningun valor. esta es una variable global

# Metodo especial de pytest que nos permite pasar parametros desde consola al momento de ejecutar
# Aqui lo usaremos para pasar el navegador en el que queremos ejecutar la prueba
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )
    parser.addoption(
        "--url", action="store", default="https://rahulshettyacademy.com/angularpractice/",
    )


@pytest.fixture(scope="function")
def setup(request):
    global driver  # Indicamos que estamos utilizando la variable global 'driver' y no creando una nueva dentro de la funcion
    browser_name = request.config.getoption("browser_name")
    url = request.config.getoption("url")

    """
        Elegir Navegador
    """
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service())
    elif browser_name == "edge":
        driver = webdriver.Edge(service=Service())

    """
        Elegir Ambiente
    """

    if url == "qa":
        driver.get("https://rahulshettyacademy.com/angularpractice/qa")
    elif url == "prd":
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    else:
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    """
            Conf Inicial
    """

    driver.implicitly_wait(3)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


# Funcion que nos permite tomar un screenshot si se genera algun error
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
