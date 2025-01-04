import time
import allure
from selenium.webdriver.support import expected_conditions as es
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from utilits.logger import Logger


class MainPage(Base):
    """Главная страница"""

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    search_area = "//input[@id='store_nav_search_term']"
    search_link = "//a[@id='store_search_link']"
    hidden_genre_element = "//*[@id='genre_flyout']/div/div[2]/div[7]/a[7]"
    genre_tap = "//div[@id='genre_tab']"
    genre_filter = "//div[@class='Qa8BXBnhFcu7QgSy5RqD']"
    all_genre = "//div[@class='_12piyDV8d50GcK-wlEd3fy']"
    game_element_cart = "//div[contains(@class, 'yoe6d_43t3I6-mjbZGkLs')]"
    product_element = "//div[@class='apphub_AppName']"
    my_profile_button = "//button[@id='account_pulldown']"
    logaut_button = "//*[@id='account_dropdown']/div/a[4]"
    delete_product = "//div[text()='Удалить все товары']"
    dialog_slider = "//div[@class='DialogSlider_Grabber']"

    # Getters
    def get_search_area(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.search_area)))

    def get_dialog_slider(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.dialog_slider)))

    def get_game_element_cart(self, index):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, f"({self.game_element_cart})[{index}]")))

    def get_hidden_genre_element(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.hidden_genre_element)))

    def get_delete_product(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.delete_product)))

    def get_genre_tap(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.genre_tap)))

    def get_logaut_button(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.logaut_button)))

    def get_my_profile_button(self):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, self.my_profile_button)))

    def get_search_link(self):
        return WebDriverWait(self.driver, 30).until(
            es.visibility_of_element_located((By.XPATH, self.search_link)))

    def get_all_genre(self, index):
        return WebDriverWait(self.driver, 30).until(
            es.visibility_of_element_located((By.XPATH, f"({self.all_genre})[{index}]")))

    def get_genre_filter(self, index):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, f"({self.genre_filter})[{index}]")))

    def click_dialog_slider(self, x, y):
        action = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, self.dialog_slider)
        time.sleep(2)
        action.click_and_hold(slider).move_by_offset(x, y).release().perform()

    # Actions
    def click_search_link(self):
        element = self.get_search_link()
        self.driver.execute_script("arguments[0].click();", element)
        print("Click search link")

    def click_all_genre(self, index):
        self.get_all_genre(index).click()
        print("Click all genre")

    def click_hidden_genre_element(self):
        self.get_hidden_genre_element().click()
        print("Click hidden genre element")

    def click_genre_tap(self):
        self.get_genre_tap().click()
        print("Click genre tap")

    def click_delete_product(self):
        self.get_delete_product().click()
        print("Click delete product")

    def click_genre_filter(self, index):
        self.get_genre_filter(index).click()
        print("Click genre filter")

    def click_my_profile_button(self):
        self.get_my_profile_button().click()
        print("Click my profile button")

    def click_logaut_button(self):
        self.get_logaut_button().click()
        print("Click logaut button\n")

    def click_game_element_cart(self, index):
        self.get_game_element_cart(index).click()
        print(f"Click game element cart index: {index}")

    def input_search_area(self, value):
        self.get_search_area().send_keys(value)
        print("Input search area")

    # Methods
    def search_product(self, name_product):
        """Метод для поиска товара с помощью поисковой строки"""
        with allure.step("Search product"):
            Logger.add_start_step(method="search_product")
            self.get_current_url()
            self.input_search_area(name_product)
            self.click_search_link()
            Logger.add_end_step(url=self.driver.current_url, method="search_product")

    def logaut(self):
        """Метод для выхода с аккаунта"""
        with allure.step("Logaut"):
            Logger.add_start_step(method="logaut")
            self.click_my_profile_button()
            self.click_logaut_button()
            Logger.add_end_step(url=self.driver.current_url, method="logaut")

    def delete_all_product(self):
        """Метод для очистки корзины"""
        with allure.step("Delete all product"):
            Logger.add_start_step(method="delete_all_product")
            self.driver.back()
            time.sleep(3)
            self.click_delete_product()
            Logger.add_end_step(url=self.driver.current_url, method="delete_all_product")

    def search_product_with_filter(self):
        """Метод для поиска товара с помощью фильтров"""
        with allure.step("Search product with filter"):
            Logger.add_start_step(method="search_product_with_filter")
            self.get_current_url()
            self.click_genre_tap()
            self.click_hidden_genre_element()
            self.scroll_to_coordinates(0, 3300)
            self.click_genre_filter(2)
            time.sleep(3)
            self.click_all_genre(8)
            time.sleep(3)
            self.click_genre_filter(13)
            self.click_dialog_slider(-80, 0)
            self.scroll_to_coordinates(0, 3300)
            time.sleep(5)
            self.click_game_element_cart(2)
            time.sleep(3)
            self.click_game_element_cart(2)
            Logger.add_end_step(url=self.driver.current_url, method="search_product_with_filter")
