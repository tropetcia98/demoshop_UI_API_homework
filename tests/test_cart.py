import requests
from utils.data import URL
import allure
from allure_commons.types import AttachmentType
from selene import browser, have
from tests.conftest import auth_with_api, clear_cart, add_product_to_cart


def test_add_jewelry_to_cart(browser_management):
    with allure.step('Авторизоваться через API.'):
        cookie = auth_with_api()

    with allure.step('Открыть страницу интернет-магазина Demo Web Shop.'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open('/')

    with allure.step('Добавить товар "Black & White Diamond Heart" в корзину через API.'):
        response = add_product_to_cart(product_url='/addproducttocart/catalog/14/1/1', cookie=cookie)
        assert response == 200

    with allure.step('Проверить, что добавленный товар содержится в корзине.'):
        browser.element('.ico-cart .cart-label').click()
        browser.element('.product-name').should(have.exact_text('Black & White Diamond Heart'))

    with allure.step('Очистить корзину.'):
        clear_cart()


def test_add_smartphone_to_cart(browser_management):
    with allure.step('Авторизоваться через API.'):
        cookie = auth_with_api()

    with allure.step('Открыть страницу интернет-магазина Demo Web Shop.'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open('/')

    with allure.step('Добавить товар "Smartphone" в корзину через API.'):
        response = add_product_to_cart(product_url='/addproducttocart/catalog/43/1/1', cookie=cookie)
        assert response == 200

    with allure.step('Проверить, что добавленный товар содержится в корзине.'):
        browser.element('.ico-cart .cart-label').click()
        browser.element('.product-name').should(have.exact_text('Smartphone'))

    with allure.step('Очистить корзину.'):
        clear_cart()
