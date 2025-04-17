from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        self.first_name = (By.NAME, "first-name")
        self.first_name_id = (By.ID, "first-name")
        self.last_name = (By.NAME, "last-name")
        self.last_name_id = (By.ID, "last-name")
        self.address = (By.NAME, "address")
        self.address_id = (By.ID, "address")
        self.email = (By.NAME, "e-mail")
        self.email_id = (By.ID, "e-mail")
        self.phone = (By.NAME, "phone")
        self.phone_id = (By.ID, "phone")
        self.zip_code = (By.NAME, "zip-code")
        self.zip_code_id = (By.ID, "zip-code")
        self.city = (By.NAME, "city")
        self.city_id = (By.ID, "city")
        self.country = (By.NAME, "country")
        self.country_id = (By.ID, "country")
        self.job_position = (By.NAME, "job-position")
        self.job_position_id = (By.ID, "job-position")
        self.company = (By.NAME, "company")
        self.company_id = (By.ID, "company")
        self.submit_button = (By.XPATH, "//button[@type='submit']")

        self.field_error = (By.CLASS_NAME, "error")
    
    @allure.step
    def open_page(self):
        self.driver.get(self.url)
    
    @allure.step
    def fill_form(self, first_name, last_name, address, email, phone, city, country, job_position, company):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.address).send_keys(address)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.phone).send_keys(phone)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.country).send_keys(country)
        self.driver.find_element(*self.job_position).send_keys(job_position)
        self.driver.find_element(*self.company).send_keys(company)

    @allure.step
    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()
    
    @allure.step
    def check_field_highlighted_red(self, field_name):
        element = self.driver.find_element(*field_name)
        return "danger" in element.get_attribute("class")

    @allure.step
    def check_field_highlighted_green(self, field_name):
        element = self.driver.find_element(*field_name)
        return "success" in element.get_attribute("class")
    