import pytest

from utils.data import URL, PASSWORD, LOGIN
import requests
import allure
from allure_commons.types import AttachmentType
from selene import browser


def auth_with_api():
    result = requests.post(
        url=URL + '/login',
        data={'Email': LOGIN, 'Password': PASSWORD, 'RememberMe': False},
        allow_redirects=False
    )

    allure.attach(body=result.text, name='Result', attachment_type=AttachmentType.TEXT, extension='txt')
    allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    cookie = result.cookies.get('NOPCOMMERCE.AUTH')

    return cookie


def add_product_to_cart(product_url, cookie):
    response = requests.post(
        url=URL + product_url,
        cookies={'NOPCOMMERCE.AUTH': cookie}
    )

    allure.attach(body=response.text, name='Response', attachment_type=AttachmentType.TEXT, extension='txt')

    return response.status_code


def clear_cart():
    browser.element('.qty-input').set_value('0').press_enter()


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = URL
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'

    yield

    browser.quit()
