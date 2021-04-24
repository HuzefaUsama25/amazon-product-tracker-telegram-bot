doc = '''
2nd Script(auto buy):
1- take link/productID as query
2- track links for stock
3- add to cart if product comes in stock
4- checkout with predefined address and payment method
'''

import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import random


chrome_options = Options()
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)

links = input("links: ").split("^^")

for i in links:
    driver.get(i)
    while True:
        try:
            stock = driver.find_element_by_xpath('//*[@id="availability"]/span').text.lower()
        except:
            stock = ""
        if stock = 