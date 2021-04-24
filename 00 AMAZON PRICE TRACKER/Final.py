import time
import telebot
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


TOKEN = "1462514759:AAFywf_fO_lwsrgZZfEIwnSMDbjlKq4iva4"
bot = telebot.TeleBot(token=TOKEN)
help = '''
AddCart - Add product (link/links) to cart
Details - Give details of product (link/links)
'''
@bot.message_handler(commands=['help']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, help)


@bot.message_handler(func=lambda msg: msg.text is not None and 'AddCart' in msg.text)
def add_tocart(message):
    mes = message.text.replace("AddCart","").replace("\n","").replace(" ","")
    links = mes.split('^^')
    for i in links:
        driver.get(i)
        try:
            addcart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            addcart.click()
            print("Done")
            bot.reply_to(message, "Added to cart")
        except:
            productname = ""
            print("Coulndt do")
            bot.reply_to(message, "Could not add to cart..")

def add_cart(link):
    links = link.split('^^')
    for i in links:
        driver.get(i)
        try:
            addcart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            addcart.click()
            return "Added to cart"
        except:
            return "Could not add to cart"
            pass

@bot.message_handler(func=lambda msg: msg.text is not None and 'Details' in msg.text)
def scrape_info(message):
    mes = message.text.replace("Details","").replace("\n","").replace(" ","")
    links = mes.split(' ')
    print("DONE")
    for i in links:
        driver.get(i)
        time.sleep(0.2)
    try:
        productname = driver.find_element_by_xpath('//*[@id="productTitle"]').text
    except Exception as e:
        print(e)
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
    try:
        imageurl = driver.find_element_by_xpath('//*[@id="landingImage"]').get_attribute('src')
    except:
        imageurl = ""
    print("Done")
    bot.reply_to(message, f"Name: {productname}\nPrice: {productprice}\nAvailibility: {stock}\n{imageurl}")


@bot.message_handler(func=lambda msg: msg.text is not None and 'Autobuy' in msg.text)
def auto_buy(message):
    mes = message.text.replace("Autobuy","").replace("\n","").replace(" ","")
    while True:
        driver.get(mes)
        time.sleep(1)
        try:
            stock = driver.find_element_by_xpath('//*[@id="availability"]/span').text.lower()
        except:
            stock = ""
        print(stock)
        if stock == "in stock.":
            bot.reply_to(message, f"IN STOCK \n {add_cart(mes)}")
            break
        else:
            time.sleep(3)

    print("Done")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"[EXCEPTION] {e}")
        time.sleep(15)
