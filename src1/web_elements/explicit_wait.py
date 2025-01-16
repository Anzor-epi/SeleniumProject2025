import time

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions # as EC

from src1.web_elements.form_elements import *

URL = 'https://demoqa.com/dynamic-properties'

print("********* Scenario 1: dynamic element handling ********")
# Execution:
driver = initialize_browser()
open_website(driver, URL)
disable_google_ads(driver)

enable_5sec_xpath = '//button[@id="enableAfter"]'
visible_5sec_xpath = '//button[@id="visibleAfter"]'

# two option
#enable_5sec = driver.find_element(By.XPATH, enable_5sec_xpath)  # option 1

wwait = WebDriverWait(driver,60)
enable_5sec = wwait.until(expected_conditions.element_to_be_clickable((By.XPATH, enable_5sec_xpath))) # option 2 MOSTLY USED

#enable_5sec = wwait.until(EC.presence_of_element_located((By.XPATH, enable_5sec_xpath)))

#enable_5sec = WebDriverWait(driver,45).until(expected_conditions.visibility_of_element_located((By.XPATH, enable_5sec_xpath)))
#enable_5sec = WebDriverWait(driver,60).until(expected_conditions.element_located_to_be_selected((By.XPATH, enable_5sec_xpath)))

enable_5sec.click()
print("element clicked...")
time.sleep(10)
driver.close()