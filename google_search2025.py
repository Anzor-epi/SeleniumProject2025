import time

from selenium import webdriver

driver = webdriver.Chrome()
print('name of the brower', driver.name)
driver.maximize_window()
driver.get("https://www.google.com")
time.sleep(5)