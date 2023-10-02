from selenium.webdriver.common.by import By

from pages.checkout_page import CheckoutPage


class FormPage:
    """
        POM:
        -- El driver lo pasamos al momento de crear un objeto de esta clase. Ese driver proviene de la Fixture que utiliza
            la BaseClass
        -- Los elementos de la pagina los mapeamos como atributos de la clase y los guardamos como tuplas
        -- Creamos los metodos por cada accion que necesitemos hacer en la pagina
        -- Estos metodos devolveran el web element entontrado para que en los test se puedan realizar las acciones de
            selenium

    """
    def __init__(self, driver):
        self.driver = driver

    name_input = (By.NAME, "name")
    email_input = (By.NAME, "email")
    pass_input = (By.ID, "exampleInputPassword1")
    gender_select = (By.ID, "exampleFormControlSelect1")
    message_banner = (By.CLASS_NAME, "alert-success")
    submit_button = (By.CLASS_NAME, "btn-success")


    def get_name(self):
        # El * se utiliza para desempaquetar la tupla y pasar lo valores como llave, valor
        # Se llaman desde HomePage porque es un atributo de la clase
        return self.driver.find_element(*FormPage.name_input)

    def get_email(self):
        return self.driver.find_element(*FormPage.email_input)

    def get_pass(self):
        return self.driver.find_element(*FormPage.pass_input)

    def get_gender(self):
        return self.driver.find_element(*FormPage.gender_select)

    def submit_form(self):
        return self.driver.find_element(*FormPage.submit_button)
    def get_confirmation_text(self):
        return self.driver.find_element(*FormPage.message_banner)

    def proceed_to_checkout(self):
        self.driver.find_element(*FormPage.submit_button).click()
        # cuando un elemento nos lleva a otra pagina podremos realizar la accion y instanciar la clase de la pag. siguiente para devolverla al llamar el metodo
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
