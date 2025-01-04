import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

from utilits.logger import Logger


class ProductPage(Base):
    """Страница товара"""

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    product_name = "//div[@class='apphub_AppName']"
    cart_button = "//a[@class='btn_green_steamui btn_medium']"
    continue_pay_button = "/html/body/div[3]/dialog/div/div[2]/div/div[3]/div/div[3]/button[2]"
    continue_product_name = "//div[@class='EflKs0JjldhDSxbUBaiOp']"
    final_price = "//div[@class='pk-LoKoNmmPK4GBiC9DR8']"
    value_final_price = None

    # Getters
    def get_product_element(self):
        return WebDriverWait(self.driver, 30).until(
            es.visibility_of_element_located((By.XPATH, self.product_name)))

    def get_final_price(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.final_price)))

    def get_continue_pay_button(self):
        return WebDriverWait(self.driver, 30).until(
            es.visibility_of_element_located((By.XPATH, self.continue_pay_button)))

    def get_continue_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            es.visibility_of_element_located((By.XPATH, self.continue_product_name)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions
    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    def click_continue_pay_button(self):
        self.get_continue_pay_button().click()
        print("Click continue pay button")

    def check_price(self):
        self.value_final_price = self.get_final_price().text
        print(f"Product price: {self.value_final_price}")

    # Methods
    def select_product_with_search(self, result):
        """Метод для выбора товара при использовании быстрога поиска"""
        with allure.step("Select product with search"):
            Logger.add_start_step(method="select_product_with_search")
            self.get_current_url()
            self.assert_current_element(self.get_product_element(), result)
            self.scroll_to_coordinates(0, 1000)
            self.click_cart_button()
            self.assert_current_element(self.get_continue_product_name(), result)
            self.check_price()
            self.click_continue_pay_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_with_search")

    def select_product_with_filter(self, result):
        """Метод для выбора товара при использовании фильтра """
        with allure.step("Select product with filter"):
            Logger.add_start_step(method="select_product_with_filter")
            self.assert_current_element(self.get_continue_product_name(), result)
            self.value_final_price = self.get_final_price().text
            self.check_price()
            self.click_continue_pay_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_with_filter")
