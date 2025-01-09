# Selenium locators

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()

driver.get("https://google.com")

# all of below methods return single element,
# return first element if multiple elements found in html document by given locator
driver.find_element(By.ID, 'search')
driver.find_element(By.NAME, 'q')
driver.find_element(By.XPATH, '//form[0]/div[0]/input[0]')
driver.find_element(By.CSS_SELECTOR, '#search')
driver.find_element(By.CLASS_NAME, 'input-text')
driver.find_element(By.TAG_NAME, 'input')
driver.find_element(By.LINK_TEXT, 'Log In')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Log')
