import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def set_up():
    print("\nStart test")
    yield
    print("Finish test")


@pytest.fixture(scope="module")
def set_group():
    print("\nEnter system")
    yield
    print("Exit system")


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
