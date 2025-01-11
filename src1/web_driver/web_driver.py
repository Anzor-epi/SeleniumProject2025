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
print("disabling google adds")
time.sleep(0.5)
disable_google_ads(driver)

print("# webDriver class attributes/properties")
print('name of the browser:', driver.name) # property
driver.maximize_window()
