import pytest
import allure
from selenium import webdriver
from ShopPage import AuthPage
from ShopPage import MainPage
from ShopPage import CartPage
from ShopPage import CheckoutPage

@allure.title("Заголовок")
@allure.description("Описание")
def test_complete_order():
    auth_page = AuthPage()
    auth_page.input_username("test_user")
    auth_page.input_password("test_password")
    auth_page.click_login_button()


    main_page = MainPage()
    main_page.add_to_cart(12345) 
    main_page.go_to_cart()

    cart_page = CartPage()
    cart_page.click_checkout_button()
    cart_page.check_cart_content()

    checkout_page = CheckoutPage()
    checkout_page.fill_form("John", "Doe", "12345")
    checkout_page.check_total_cost()
