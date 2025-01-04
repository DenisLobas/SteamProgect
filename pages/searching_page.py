import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from base.base_class import Base
from utilits.logger import Logger


class SearchingPage(Base):
    """Страница поиска товара"""

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    product = "//span[@class='title']"

    # Getters
    def get_product(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.product)))

    # Actions
    def click_product(self):
        self.get_product().click()
        print("Click product")

    # Methods
    def select_needed_element(self):
        """Метод для выбора нужного товара на странице поиска"""
        with allure.step("Select needed element"):
            Logger.add_start_step(method="select_needed_element")
            self.click_product()
            Logger.add_end_step(url=self.driver.current_url, method="select_needed_element")
