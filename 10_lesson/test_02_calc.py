import pytest
import allure
from selenium import webdriver
from CalcPage import CalculatorPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.title("Проверка расчёта 7 + 8 с задержкой 45 секунд")
@allure.description('Тест на калькулятор')
@allure.severity('CRITICAL')
def test_addition_with_delay(driver):
    page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    with allure.step("Установить задержку 45"):
        page.set_delay(5)

    with allure.step("нажать 7 + 8 ="):
        page.press("7")
        page.press("+")
        page.press("8")
        page.press("=")

    with allure.step("дождаться результата и проверить его"):
        result = page.get_result()
        assert result == "15", f"Ожидалось 15, но получили {result}"
