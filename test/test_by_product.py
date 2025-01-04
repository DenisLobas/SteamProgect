from base.base_class import Base
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.searching_page import SearchingPage
import allure
from conftest import set_group
from conftest import set_up


@allure.description("test buy product")
def test_buy_product(set_group, set_up, driver):
    """ Тест на покупку товара через поиск"""

    # Открываем браузер
    b = Base(driver)
    b.open_browser()
    # Авторизируемся
    lp = LoginPage(driver)
    lp.authorization()
    # Через посиковик находим нужную игру
    mp = MainPage(driver)
    mp.search_product("Baldur's Gate 3")
    # Выбираем игру которую ищем
    fp = SearchingPage(driver)
    fp.select_needed_element()
    # Проверяем что выбрали нужную игру и переходим в карзину
    pp = ProductPage(driver)
    pp.select_product_with_search("Baldur's Gate 3")
    # Перезодим к оплате
    cp = CartPage(driver)
    cp.continue_pay("Baldur's Gate 3", pp.value_final_price)
    # Проверяем что находимся в окне оплаты тавара
    ctp = CheckoutPage(driver)
    ctp.finish_checkout("test_buy_product")
    mp.delete_all_product()
    mp.logaut()


@allure.description("Test filter of product")
def test_filter_of_product(set_up, driver):
    """Тест фильтра товаров"""

    # Открываем браузер
    b = Base(driver)
    b.open_browser()
    # Авторизируемся
    lp = LoginPage(driver)
    lp.authorization()
    # Выбираем игру используя фильтр
    mp = MainPage(driver)
    mp.search_product_with_filter()
    # Проверяем что выбрали нужную игру и переходим в карзину
    pp = ProductPage(driver)
    pp.select_product_with_filter("Divinity: Original Sin Enhanced Edition")
    # Перезодим к оплате товара
    cp = CartPage(driver)
    cp.continue_pay("Divinity: Original Sin Enhanced Edition", pp.value_final_price)
    # Проверяем что находимся в окне оплаты тавара
    ctp = CheckoutPage(driver)
    ctp.finish_checkout("test_filter_of_product")
    mp.delete_all_product()
    mp.logaut()
