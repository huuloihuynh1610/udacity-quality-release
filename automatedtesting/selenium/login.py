# #!/usr/bin/env python
import sys
import datetime
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import NoSuchElementException

def login(user, password):
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')
    logging.info( 'Starting the browser...' )
    logging.info()
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.nl/')

    logging.info('Browser started successfully.')
    logging.info()
    logging.info('Navigating to the login page.')
    logging.info()
    driver.get('https://www.saucedemo.com/')
    logging.info( 'Loging in to https://www.saucedemo.com/')
    driver.find_element_by_css_selector('input[data-test="username"]').send_keys(user)
    driver.find_element_by_css_selector('input[data-test="password"]').send_keys(password)
    driver.find_element_by_css_selector('input[value=Login]').click()

    logging.info('Searching for Products.')
    headerLb = driver.find_element_by_class_name('header_secondary_container').text
    assert "PRODUCTS" in headerLb
    logging.info('Successfully logged in ' + user + '.')
    logging.info()
    logging.info('Selecting products.')
    prods = driver.find_elements_by_css_selector('.inventory_item')
    logging.info()
    logging.info('Adding products to cart.')
    logging.info()
    for prod in prods:
        prod_name = prod.find_element_by_css_selector(
            '.inventory_item_name').text
        prod.find_element_by_css_selector('button.btn_inventory').click()
        logging.info(pro_name + 'successfully add to cart.')

    cart_lb = driver.find_element_by_css_selector(
        '.shopping_cart_badge').text
    assert cart_lb == '6'

    driver.find_element_by_css_selector('a.shopping_cart_link').click()
    assert '/cart.html' in driver.current_url,'Navigation to shopping cart unsuccessfully.'

    logging.info('Remove product from cart.')
    cart_prods = driver.find_elements_by_css_selector('.cart_item')
    for prod in cart_prods:
        prod_name = prod.find_element_by_css_selector(
            '.inventory_item_name').text
        prod.find_element_by_css_selector('button.cart_button').click()
        logging.info(prod_name + ' successfully removed from shopping cart.')
        
    if driver.find_elements_by_css_selector('.shopping_cart_badge'):
        cart_bool = False
    else:
        cart_bool = True
    assert cart_bool == True
    logging.info('Shopping cart success + : ' + str(cart_bool))

login('standard_user', 'secret_sauce')