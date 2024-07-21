from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
import logging
from allure_commons.types import AttachmentType

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import allure
from allure_commons.types import AttachmentType

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()



def wait_and_click(browser, xpath, timeout=30):
    element = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    browser.execute_script("arguments[0].click();", element)

def wait_and_send_keys(browser, xpath, keys, timeout=30):
    element = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element.send_keys(keys)

@pytest.fixture()
def step(browser):
    
    with allure.step("Открытие страницы каталога"):
            browser.get("https://artdevivre.ru/catalog")
            logger.info("Открыта страница каталога")

    with allure.step("Выбор первого ковра в каталоге"):
        item = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[4]/div[3]/div/div[1]/div[1]/div/a/div[2]/span/img')))
        browser.execute_script("arguments[0].click();", item)
        logger.info("Выбран первый ковер")

    with allure.step("Добавление в корзину"):
        wait_and_click(browser, '//button[text()="Добавить в корзину"]')
        logger.info("Ковер добавлен в корзину")

    with allure.step("Переход в корзину"):
        wait_and_click(browser, '//button[text()="Перейти в корзину"]')
        logger.info("Осуществлен переход в корзину")


@pytest.mark.skip('Bug 1')
@allure.feature('ADV Website')
@allure.story("Проверка функциональности 'Демонстрация ковров в вашем интерьере'")
def test_carpet_demonstration_home(browser, step):
    try:
    
        with allure.step("Выбор опции 'Демонстрация ковров в вашем интерьере'"):
            wait_and_click(browser, '//span[contains(text(), "Демонстрация ковров в вашем интерьере")]')
            logger.info("Выбрана опция 'Демонстрация ковров в вашем интерьере'")

        with allure.step("Заполнение формы"):
            wait_and_send_keys(browser, '//input[@id="name-cart-form"]', "auto-tests")
            wait_and_send_keys(browser, '//input[@id="phone-cart-form"]', "9999999999")
            wait_and_send_keys(browser, '//input[@id="email-cart-form"]', "auto@tests.tests")
            wait_and_send_keys(browser, '//input[@id="address-cart-form"]', "test 99-99-99")
            logger.info("Форма заполнена")

        with allure.step("Отправка формы"):
            item = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="отправить"]'))).click()
            logger.info("Форма отправлена")

        with allure.step("Возврат в каталог"):
            item = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Перейти в каталог"]')).click())
            logger.info("Осуществлен возврат в каталог")

        logger.info("Проверка функциональности 'Демонстрация ковров в вашем интерьере'. Заявка отправлена")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=AttachmentType.TEXT)
    
    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=AttachmentType.PNG)

@pytest.mark.skip('Bug 2')
@allure.feature('ADV Website')
@allure.story("Проверка функциональности 'Демонстрация ковров в салоне'")
def test_carpet_demonstration_store(browser, step):
    try:
        #with allure.step("Открытие страницы каталога"):
            #browser.get("https://artdevivre.ru/catalog")
            #assert "Каталог" in browser.title
            #allure.attach(browser.get_screenshot_as_png(), name="Catalog Page Screenshot", attachment_type=allure.attachment_type.PNG)

        #with allure.step("Выбор первого ковра в каталоге"):
            #item = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[4]/div[3]/div/div[1]/div[1]/div/a/div[2]/span/img')))
            #browser.execute_script("arguments[0].click();", item)

        #with allure.step("Добавление в корзину"):
            #wait_and_click(browser, '//button[text()="Добавить в корзину"]')

        #with allure.step("Переход в корзину"):
            #wait_and_click(browser, '//button[text()="Перейти в корзину"]')

        with allure.step("Выбор опции 'Демонстрация ковров в салоне'"):
            wait_and_click(browser, '//span[contains(text(), "Демонстрация ковров в салоне")]')

        with allure.step("Нажать кнопку 'Выбрать салон'"):
            wait_and_click(browser, '//button[text()="Выбрать салон"]')

        with allure.step("Выбрать первый салон из списка"):
            wait_and_click(browser, '//*[@id="drawer"]/div[1]/div/div/div/div[2]/div/ul/li[2]/div/svg')

        with allure.step("Нажать кнопку 'Выбрать салон'"):
            wait_and_click(browser, '//button[text()="Выбрать салон"]')

        with allure.step("Заполнение формы"):
            wait_and_send_keys(browser, '//input[@id="name-cart-form"]', "auto-tests")
            wait_and_send_keys(browser, '//input[@id="phone-cart-form"]', "9999999999")
            wait_and_send_keys(browser, '//input[@id="email-cart-form"]', "auto@tests.tests")

        with allure.step("Отправка формы"):
            wait_and_click(browser, '//button[text()="Отправить"]')

        with allure.step("Возврат в каталог"):
            wait_and_click(browser, '//a[text()="Перейти в каталог"]')

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=AttachmentType.TEXT)

    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=AttachmentType.PNG)


@allure.feature('ADV Website')
@allure.story("Проверка функциональности 'Оформить заказ на доставку'")
def test_adv_delivery_order(browser, step):
    try:

        with allure.step("Выбор опции 'Оформить заказ на доставку'"):
            wait_and_click(browser, '//span[contains(text(), "Оформить заказ на доставку")]')
            logger.info("Нажали Оформить заказ на доставку")

        with allure.step("Заполнение формы"):
            wait_and_send_keys(browser, '//input[@id="name-cart-form"]', "auto-tests")
            wait_and_send_keys(browser, '//input[@id="phone-cart-form"]', "9999999999")
            wait_and_send_keys(browser, '//input[@id="email-cart-form"]', "auto@tests.tests")
            wait_and_send_keys(browser, '//input[@id="address-cart-form"]', "test 99-99-99")
            logger.info("Заполнили форму")

        with allure.step("Отправка формы"):
            wait_and_click(browser, '//button[text()="Отправить"]')
            logger.info("Отправили форму")

        with allure.step("Возврат в каталог"):
            wait_and_click(browser, '//a[text()="Перейти в каталог"]')
            logger.info("Вошли в каталог")


    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=AttachmentType.TEXT)

    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=AttachmentType.PNG)
   

if __name__ == "__main__":
    pytest.main([__file__, '--alluredir', './allure-results'])
