import allure

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

from utilits.logger import Logger


class LoginPage(Base):
    """Странца авторизации"""

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    user_name = "DonDelas6"
    user_password = "DonDelas123"
    input_login = "//input[@type='text']"
    input_password = "//input[@type='password']"
    login_button = "//button[@class='DjSvCZoKKfoNSmarsEcTS']"
    global_action_link = "//a[@class='global_action_link']"

    # Getters
    def get_input_login(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.input_login)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_global_action_link(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.global_action_link)))

    # Actions
    def send_keys_login(self, value):
        self.get_input_login().send_keys(value)
        print("Input login")

    def send_keys_password(self, value):
        self.get_input_password().send_keys(value)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_global_action_link(self):
        self.get_global_action_link().click()
        print("Click global action link")

    # Methods
    def authorization(self):
        """ Метод для авторизации пользователя"""
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.get_current_url()
            self.click_global_action_link()
            self.get_current_url()
            self.send_keys_login(self.user_name)
            self.send_keys_password(self.user_password)
            self.click_login_button()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
