# Selenium locators
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()

driver.get("https://demoqa.com/text-box")
time.sleep(2)

# all of below methods return single element,
# return first element if multiple elements found in html document by given locator

# ALWAYS MAKE SURE ITS UNIQE (COMMAND + F)

# <input autocomplete="off" placeholder="Full Name" type="text" id="userName" class=" mr-sm-2 form-control">
driver.find_element(By.ID, 'userName').send_keys('jonedoe')  #Fullname wiwh ID
time.sleep(1)

# <input autocomplete="off" placeholder="name@example.com" type="email" id="userEmail" class="mr-sm-2 form-control">
# driver.find_element(By.CLASS_NAME, 'mr-sm-2 form-control').send_keys("sample@mail.com") #Email with Class Didn't work beacause of the space

# //*[@id="userEmail"] Email with XPATH
driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys("sample@mail.com")
time.sleep(1)

# "#currentAddress" element that has ID='currentAddress'    ( with current address)
# ".form-contorl" element that has a class value (or part of class value) 'form-control'
driver.find_element(By.CSS_SELECTOR, '#currentAddress').send_keys('12345 current address')
time.sleep(2)


driver.get("https://amazon.com/")
time.sleep(2)

# <a href="/stores/node/20648519011?channel=discovbar?field-lbr_brands_browse-bin=AmazonBasics&amp;ref_=nav_cs_amazonbasics" >Amazon Basics</a>
driver.find_element(By.LINK_TEXT, 'Amazon Basics').click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Amazon Basics').click()

time.sleep(2)
driver.quit()

print("selenium locators completed")




#driver.find_element(By.NAME, 'q') we did it in google search
#driver.find_element(By.TAG_NAME, 'input') hard to find unqie
