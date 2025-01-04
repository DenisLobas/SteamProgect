import datetime


class Base:
    """Базовый класс"""

    base_url = "https://store.steampowered.com"

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод для проверки url"""
        get_url = self.driver.current_url
        print("\nCurrent url: " + get_url)

    def assert_current_element(self, word, result):
        """Метод для сравнения элемента"""
        value_ward = word.text
        assert value_ward == result
        print(f"Current element: {value_ward}")

    def assert_current_words(self, word, result):
        """Метод для проверки корректности элемента"""
        assert word == result
        print(f"Current element: {word}")

    def get_screenshot(self, test):
        """Метод для создания скриншотов"""
        new_data = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name_screenshot = f"{test} " + new_data + ".png"
        self.driver.save_screenshot(f"/Users/denis/Steam/screen/{name_screenshot}")
        print("Save screenshot")

    def open_browser(self):
        """Метод для открытия браузера"""
        self.driver.get(self.base_url)

    def scroll_to_coordinates(self, x, y):
        """Метод для скроллинга к указанным координатам (x, y)"""
        self.driver.execute_script(f"window.scrollTo({x}, {y});")
