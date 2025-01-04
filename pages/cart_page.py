import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from base.base_class import Base
from utilits.logger import Logger


class CartPage(Base):
    """Страница корзины"""

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    finish_pay_button = "//*[@id='page_root']/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/button"
    cart_name_game = "//div[@class='EflKs0JjldhDSxbUBaiOp']"
    continue_product_name = "//div[@class='EflKs0JjldhDSxbUBaiOp']"
    all_final_price = "//*[@id='page_root']/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div[1]"

    # Getters
    def get_finish_pay_button(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.finish_pay_button)))

    def get_all_final_price(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.all_final_price)))

    def get_continue_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.continue_product_name)))

    # Actions
    def click_finish_pay_button(self):
        self.get_finish_pay_button().click()
        print("Click finish pay button")

    def only_price(self):
        """Получение цены товара"""
        text = self.get_all_final_price().text
        result = text.replace("Общая стоимость", "").strip()
        return result

    # Methods
    def continue_pay(self, result, price):
        """Метод для перехода к странице оплаты товара"""
        with allure.step("Continue pay"):
            Logger.add_start_step(method="continue_pay")
            self.assert_current_element(self.get_continue_product_name(), result)
            self.assert_current_words(self.only_price(), price)
            self.click_finish_pay_button()
            Logger.add_end_step(url=self.driver.current_url, method="continue_pay")
