
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src1.utilites import *

# Examples of webDelements class properties and methods

#URL = "https://demoqa.com/browser-windows"
URL = "https://travel.agileway.net/login"

uname = 'agileway'
passwrd = 'testwise'

# locators

header_xpath = '//*[@id="container"]/h2'
username_id = 'username'
password_id = 'password'
remember_id = 'remember_me'
sign_in_name = 'commit'

print("Initializing the browser, with chrome options")
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)  # instantiating webDriver class, driver object created
driver.implicitly_wait(20) # applies all find_element or interactions with browser elements
driver.get(URL)
driver.maximize_window()
time.sleep(1)

print("verify header text")
header_text = driver.find_element(By.XPATH, header_xpath).text
assert header_text == 'Agile Travel', 'header text verification FAILED!'

print("enter username")
driver.find_element(By.ID, username_id).send_keys(uname)

print("enter password")
driver.find_element(By.ID, password_id).send_keys(passwrd)

print("check remember me check box")
checkbox = driver.find_element(By.ID, remember_id)
checkbox.click()
print(f"if remember me is checked: {checkbox.is_selected()}")
assert checkbox.is_selected(), 'checked box verification failed!'

print("verify the remember me check box is checked")

print("check signin button is enabled")

print("submit form")

print("verify expected url: https://travel.agileway.net/flights/start ")

print("verify that signin meassage is displayed")