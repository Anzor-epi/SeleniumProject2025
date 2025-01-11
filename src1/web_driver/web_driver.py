import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src1.utilites import *

# Examples of webDriver class properties and methods

URL = "https://demoqa.com/browser-windows"
# locators
print("Initializing the browser, with chrome options")
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)  # instantiating webDriver class, driver object created
driver.get(URL)
driver.maximize_window()

print("disabling google adds")
time.sleep(0.5)
disable_google_ads(driver)

print("# webDriver class attributes/properties")
print('name of the browser:', driver.name) # property
print('title of the webpage', driver.title)
print('current url of page', driver.current_url)
print("ID of the current browser tab or window:", driver.current_window_handle)

print(" # webDriver class method:  ")
driver.back()
print("current url", driver.current_url) # ' data:, '
assert driver.current_url == 'data:,'

driver.forward()
time.sleep(0.5)
disable_google_ads(driver)
assert driver.current_url == 'https://demoqa.com/browser-windows', 'url verification failed on forward()'
time.sleep(2)

driver.refresh()
time.sleep(0.5)
disable_google_ads(driver)
assert driver.current_url == 'https://demoqa.com/browser-windows', 'url verification failed on refresh()'

print("switching between tabs...")
print("find the element, click on it, it should open the new tab")
print("switch to the new tab")
print("verify we are on the new tab: find the element with the text, verify the text as expected")



print("closing browser...")
time.sleep(5)
driver.quit()
