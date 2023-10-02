import logging
import time

import pytest
from selenium.common import NoSuchElementException

from pages.form_page import FormPage
from test_data.home_page_data import HomePageData
from utilities.base_class import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmit(self, get_data_for_excel_file):
        log = self.get_logger()
        log.info("usuario ingresa a llenar formulario con " +
                 "nombre: " + get_data_for_excel_file["name"]
                 )

        try:
            form_page = FormPage(self.driver)
            form_page.get_name().send_keys(get_data_for_excel_file["name"])
            form_page.get_email().send_keys(get_data_for_excel_file["mail"])
            form_page.get_pass().send_keys(get_data_for_excel_file["pass"])
            self.select_option_by_text(form_page.get_gender(), get_data_for_excel_file["genre"])
            form_page.submit_form().click()
            assert "Success" in form_page.get_confirmation_text().text
            time.sleep(5)
        except KeyError as ke:
            log.error(f'Llaves del data set no existentes:  {ke}')
        except NoSuchElementException as e:
            log.error(f'Excepcion NoSuchElementException generado con detalle: {e}')
            raise NoSuchElementException("Elemento no encontrado en pantalla")
        except AssertionError as ae:
            log.error(f'Excepcion AssertionError generado con detalle: {ae}')
            raise AssertionError(f'Se genera error en la asercion:  {ae}')

    """
        Al momento de ejecutar el test con varios casos, tenemos tres opciones para evitar que se 
        sobreescriba la informacion en los inputs
        1. Cambiando el scope del fixture para que se ejecute por metodo
        2. Colocando al final la funcion test el metodo de selenium "driver.refresh()"
        3. Antes de escribir en el campo, utilizar el metodo de selenium "element.clear()"
    """

    # Forma de pasar los datos directamente desde los descritos en la anotacion
    @pytest.fixture(params=[
        ("pepito", "pe@correo.com", "1234", "Male"),
        ("pancha", "pa@correo.com", "234567", "Female")])
    def get_data_for_annotation(self, request):
        return request.param

    # Forma de pasar los datos desde la anotacion pero usando un diccionario externo
    @pytest.fixture(params=HomePageData.home_page_data)
    def get_data_for_external_file(self, request):
        return request.param

    # Forma de pasar los datos mediante un excel
    @pytest.fixture(params=HomePageData.get_excel_data())
    def get_data_for_excel_file(self, request):
        return request.param