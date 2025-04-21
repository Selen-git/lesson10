import pytest
import allure
from selenium import webdriver
from ShopPage import ShopPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.title("Проверка работы корзины в магазине")
@allure.description('Тест на магазин')
@allure.severity('CRITICAL')
def test_shop_with_allure(driver):
    shop_page = ShopPage(driver)
    with allure.step("Открыть страницу магазина"):
        shop_page.open()
    shop_page.authorization()
    with allure.step("Добавляем товар в корзину"):
        shop_page.add_to_cart()
        shop_page.in_cart()
    shop_page.click_checkout()
    with allure.step("Заполняем форму"):
        shop_page.fill_form(
            first_name="Иван", last_name="Петров",
            postal_code="123456")
    with allure.step("Проверяем сумму"):
        shop_page.checking_total_amount()
        total = shop_page.checking_total_amount()
        assert total == "Total: $58.29", (
            f"Итоговая сумма не равна $58.29. " f"Фактическая сумма: {total}"
        )
