import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from utilits.logger import Logger


class CheckoutPage(Base):
    """Страница оплаты товара"""

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    block_header = "//div[@class='block_header']"

    # Getters
    def get_block_header(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.block_header)))

    # Methods
    def finish_checkout(self, test):
        """Метод содержащий финальные проверки товара при оплате"""
        with allure.step("Finish checkout"):
            Logger.add_start_step(method="finish_checkout")
            self.get_current_url()
            self.assert_current_element(self.get_block_header(), "СПОСОБЫ ОПЛАТЫ")
            self.get_screenshot(test)
            Logger.add_end_step(url=self.driver.current_url, method="finish_checkout")
