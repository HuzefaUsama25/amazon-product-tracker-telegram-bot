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
print()

count = 1
for i in links:
    driver.get(i)
    try:
        productname = driver.find_element_by_xpath('//*[@id="productTitle"]').text
    except:
        productname = ""
    try:
        productprice = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
    except:
        try:
            productprice = driver.find_element_by_xpath('//*[@id="priceblock_saleprice"]').text
        except:
            productprice = ""
    try:
        stock = driver.find_element_by_xpath('//*[@id="availability"]/span').text.lower()
    except:
        stock = ""
    print(driver.current_url)
    print(productname)
    print(productprice)
    print(stock)
    print()

i = input("What to add to cart [Enter url]: ")
driver.get(i)
addcart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
addcart.click()












