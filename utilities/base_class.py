import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# En la baseclass creamos la anotacion para correr el setup del conftest
# Importante para correr en consola:
# Debe estar creado los archivos __init__.py para que se reconozca como un modulo valido de Python
@pytest.mark.usefixtures("setup")
class BaseClass:
    """
        En esta clase se colocan todos aquellos metodos que requerimos reutilizar a lo largo de la ejecuccion
        En este caso reutilizaremos los wait

    """
    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("../reports/logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger

    #Reutiliacion select
    def select_option_by_text(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def verify_invisibility_of_element(self, xpath):
        element = WebDriverWait(self.driver, 6).until(
            EC.invisibility_of_element((By.XPATH, xpath)))

    def verify_presence_of_element(self, class_name):
        element = WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
