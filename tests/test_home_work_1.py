import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

'''Необходимо написать автотесты для сайта saucedemo: Ссылка на сайт: https://www.saucedemo.com/

Функционал, который необходимо покрыть автотестами:'''

'''Авторизация

Авторизация используя корректные данные (standard_user, secret_sauce)'''


def test_auth_positive():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'

    browser.quit()


'''Авторизация используя некорректные данные (user, user)'''


def test_auth_negative():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    message = browser.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/h3')
    text = message.text
    assert text == 'Epic sadface: Username and password do not match any user in this service', "Error message doesn't match expected."
    browser.quit()


'''Корзина

Добавление товара в корзину через каталог'''


def test_add_items_in_card_in_katalog():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    browser.find_element(By.ID, 'item_2_title_link').is_displayed()
    time.sleep(5)
    browser.find_element(By.XPATH, '//button[@class="btn_primary btn_inventory"]').click()
    card = browser.find_element(By.XPATH, '//span[@class="fa-layers-counter shopping_cart_badge"]')
    text = card.text
    assert text == '1'
    browser.quit()


'''Удаление товара из корзины через корзину'''


def test_de_late_items_in_card_in_card():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    browser.find_element(By.ID, 'item_2_title_link').is_displayed()
    time.sleep(3)
    browser.find_element(By.XPATH, '//button[@class="btn_primary btn_inventory"]').click()
    browser.find_element(By.XPATH, '//span[@class="fa-layers-counter shopping_cart_badge"]').click()
    time.sleep(5)
    assert browser.current_url == 'https://www.saucedemo.com/v1/cart.html', 'url не соответствует ожидаемому'
    browser.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/button').click()
    time.sleep(5)
    de_late = browser.find_element(By.XPATH, '//*[@class="removed_cart_item"]')
    text = de_late.text
    assert text == ''
    browser.quit()


'''Добавление товара в корзину из карточки товара'''


# def test_add_items_in_card_in_productcard():
#     browser.get('https://www.saucedemo.com/v1/')
#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     browser.find_element(By.XPATH, '//*[@id="add-to-cart"]').click()
#     assert browser.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
#
#     browser.quit()


'''Удаление товара из корзины через карточку товара'''

'''Карточка товара'''

'''Успешный переход к карточке товара после клика на картинку товара'''
'''Успешный переход к карточке товара после клика на название товара'''
'''Оформление заказа'''

'''Оформление заказа используя корректные данные
Фильтр'''

'''Проверка работоспособности фильтра (A to Z)'''


def test_filter_az():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'
    browser.find_element(By.XPATH, '//select[@class="product_sort_container"]').click()
    check = browser.find_element(By.XPATH, ' //option[@value="az"]')
    text = check.text
    assert text == 'Name (A to Z)'
    expected_len = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)' ]
    cards = browser.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
    text_list = [card.text for card in cards]
    assert text_list == expected_len, f'Expected: {expected_len}, Actual: {text_list}'


'''Проверка работоспособности фильтра (Z to A)'''


def test_filter_za():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'
    browser.find_element(By.XPATH, '//select[@class="product_sort_container"]').click()
    check = browser.find_element(By.XPATH, ' //option[@value="za"]')
    text = check.text
    assert text == 'Name (Z to A)'
    expected_len = ['Test.allTheThings() T-Shirt (Red)','Sauce Labs Onesie', 'Sauce Labs Fleece Jacket', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack',]
    cards = browser.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
    text_list = [card.text for card in cards]
    assert text_list == expected_len, f'Expected: {expected_len}, Actual: {text_list}'


'''Проверка работоспособности фильтра (low to high)'''


def test_filter_low_to_high():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'


'''Проверка работоспособности фильтра (high to low)'''


def test_filter_high_to_low():
    browser.get('https://www.saucedemo.com/v1/')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'


'''Бургер меню

Выход из системы
Проверка работоспособности кнопки "About" в меню
Проверка работоспособности кнопки "Reset App State"
Чек лист достаточно примерный. Чуть позже во время практики над основным проектом мы сможем поработать с качественной документацией.

Основная суть данного задания - попробовать Selenium и Pytest на практике.

Для выполнения задания нужно создать новый репозиторий и написать некоторое количество автотестов.'''
