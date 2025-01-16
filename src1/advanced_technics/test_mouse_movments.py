import time

from selenium.webdriver import ActionChains

from src1.web_elements.alerts import *
from src1.web_elements.form_elements import *

URL = "https://demoqa.com/droppable"

print("********* Scenario 1: advanced technics is selenium ********")
# Execution:
driver = initialize_browser()
open_website(driver, URL)

drag_xpath = '//div[@id="draggable"]'
drop_xpath = '//div[@id="droppable"]'

print("# drag the 'Drag me' box to 'Drop here' box")
print("find 'Drag me' box")
drag_me = driver.find_element(By.XPATH, drag_xpath)

print("find 'Drop here' box")
drop_here = driver.find_element(By.XPATH, drop_xpath)

print("mouse movement Drag and Drop")
actions = ActionChains(driver) # remember this class !!!
actions.drag_and_drop(drag_me, drop_here).perform()

dropped = driver.find_element(By.XPATH, drop_xpath).text
assert dropped == 'Dropped!', 'ERROR: verification Dropped failed!'

print("# javaScript executor:")
accept_tab = driver.find_element(By.ID, 'droppableExample-tab-accept')
# accept_tab.click()   # clicking using the Selenium method
print("# clicking using the javaScript")
driver.execute_script("arguments[0].click();", accept_tab)


time.sleep(10)
close_browser(driver)
print("********* Scenario 1: automating alert interaction completed ********")



