import time
import pytest
import allure
from CalcPage import CalculatorPage
from selenium import webdriver

 
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # Можно убрать, если нужен реальный браузер
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.title("Проверка расчёта 7 + 8 с задержкой 45 секунд")
def test_addition_with_delay(driver):
    page = CalculatorPage(driver)
 
    # Шаг 1: открыть страницу калькулятора
    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  # Заменить на реальный адрес
 
    # Шаг 2: установить задержку 45
    page.set_delay(5)
 
    # Шаг 3: нажать 7 + 8 =
    page.press("7")
    page.press("+")
    page.press("8")
    page.press("=")

    time.sleep(10)
 
    # Шаг 4: дождаться результата и проверить его
    result = page.get_result()
    assert result == "15", f"Ожидалось 15, но получили {result}"