import pytest
from selenium import webdriver
from CalcPage import CalculatorPage as CalculatorActions

class TestCalculator():

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_calculator(self):
        calculator = CalculatorActions(self.driver)
        calculator.page.open_page("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calculator.perform_calculation('45')

        result = calculator.page.get_result()
        self.assertEqual(result, '15')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()
