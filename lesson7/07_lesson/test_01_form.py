from selenium import webdriver
from FormPage import FormPage


def test_form():

    driver = webdriver.Chrome()
    form_page = FormPage(driver)
    form_page.open_page()
    form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    form_page.submit_form()

    zip_code_highlighted_red = form_page.check_field_highlighted_red(form_page.zip_code_id)
    assert zip_code_highlighted_red, "Zip code field is not highlighted red"

    other_fields_highlighted_green = all([form_page.check_field_highlighted_green(field) for field in [form_page.first_name_id, form_page.last_name_id, form_page.address_id, form_page.email_id, form_page.phone_id, form_page.city_id, form_page.country_id, form_page.job_position_id, form_page.company_id]])
    assert other_fields_highlighted_green, "One or more fields are not highlighted green"

    driver.quit()
