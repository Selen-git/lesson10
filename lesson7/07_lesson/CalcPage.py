import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.spinner = (By.ID, "spinner")
 
    @allure.step("Открываем страницу калькулятора")
    def open(self, url):
        self.driver.get(url)
 
    @allure.step("Устанавливаем задержку {seconds} секунд")
    def set_delay(self, seconds):
        el = self.driver.find_element(*self.delay_input)
        el.clear()
        el.send_keys(str(seconds))
 
    @allure.step("Нажимаем кнопку '{key}'")
    def press(self, key):
        buttons = self.driver.find_elements(By.XPATH, f"//span[normalize-space(text())='{key}']")
        assert buttons, f"Кнопка '{key}' не найдена"
        buttons[0].click()
 
    @allure.step("Получаем результат")
    def get_result(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.spinner)
        )
        return self.driver.find_element(*self.screen).text
 
    @allure.step("Выполняем операцию {expr}")
    def calculate(self, expr, delay=1):
        self.set_delay(delay)
        for char in expr:
            self.press(char)
        self.press("=")
        return self.get_result()