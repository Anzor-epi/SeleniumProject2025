# XPATH and CSS Selector

# Xpath Syntax:  xpath=//tagname[@attribute='value']

#                                     usually//*  but since we know it's div
# RELATIVE xpath (use this in your script): //div[@id="flash_notice"] (copy> xpath)

# ABSOLUTE xpath of 'signed in' message -› '/html/body/div/div[2]' (copy > FullXpath)
# example 2: "/html/body/div[1]/header/div/div[1]/div[3]/div/a[4]/div[1]/span[1]"

#CSS Selector:
# css=tag#id
# xpath: '//div[@id="flash _notice" and @class='nav_bar left']' -> css_selector:
# "div#flash_notice"
# "button#login"
# "input#password"

# css=tag. class
# xpath: "//div[@class="nav_bar"]" -> css_select: "div.nav_bar"


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# amazon.com , find cart element to click

driver1 = webdriver.Chrome()
driver1.get("https://www.amazon.com")

cart = driver1.find_element(By.XPATH, '//div[@id="nav-cart-count-container"]/span[2]')
cart.click()

search = driver1.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
search.send_keys("black friday")
time.sleep(4)
