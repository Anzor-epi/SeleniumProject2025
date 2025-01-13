
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src1.utilites import *

# Examples of webDelements class properties and methods

#URL = "https://demoqa.com/browser-windows"
URL = "https://travel.agileway.net/login"

uname = 'agileway'
passwrd = 'testwise'
flights_url = "https://travel.agileway.net/flights/start"
# locators

header_xpath = '//*[@id="container"]/h2'
username_id = 'username'
password_id = 'password'
remember_id = 'remember_me'
sign_in_name = 'commit'
flash_notice_id = 'flash_notice'

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
print("verify the remember me check box is checked")
print(f"is remember me checked: {checkbox.is_selected()}")
assert checkbox.is_selected(), 'checked box verification failed!'

print("check signin button is enabled")
signin = driver.find_element(By.NAME, sign_in_name)
print(f"is signin button enabled: {signin.is_enabled()}")
assert signin.is_enabled(), 'Signin button is not enabled!'

print("submit form")
signin.click()
time.sleep(5)

print("verify expected url: https://travel.agileway.net/flights/start ")
assert driver.current_url == 'https://travel.agileway.net/flights/start', 'signin failed flights page was not opened'

print("verify that signin message is displayed")
msg = driver.find_element(By.ID, flash_notice_id).text
assert msg == 'Signed in!', 'verification flash notice failed!'

print('click on sign off')
driver.find_element(By.LINK_TEXT, 'Sign off (agileway)').click()
#driver.find_element(By.PARTIAL_LINK_TEXT, 'gn off (agileway)').click()

print("verify flash notice is Signed out!")
msg = driver.find_element(By.ID, flash_notice_id).text
assert msg == 'Signed out!', 'signin off failed'
time.sleep(5)