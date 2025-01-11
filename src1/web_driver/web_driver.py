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
driver.implicitly_wait(20) # applies all find_element or interactions with browser elements
driver.get(URL)
driver.maximize_window()

print("disabling google adds")
time.sleep(0.5)
disable_google_ads(driver)

print("# webDriver class attributes/properties")
print('name of the browser:', driver.name) # property
print('title of the webpage', driver.title)
print('current url of page', driver.current_url)
main_tab_handle = driver.current_window_handle
print("ID of the current browser tab or window:", main_tab_handle)

print(" # webDriver class method:  ")
driver.back()
print("current url", driver.current_url) # ' data:, '
assert driver.current_url == 'data:,'

driver.forward()
time.sleep(1)
disable_google_ads(driver)
assert driver.current_url == 'https://demoqa.com/browser-windows', 'url verification failed on forward()'


driver.refresh()
time.sleep(2)
disable_google_ads(driver)
assert driver.current_url == 'https://demoqa.com/browser-windows', 'url verification failed on refresh()'

print("switching between tabs...")
print("find the element, click on it, it should open the new tab")
newtab_button = driver.find_element(By.XPATH, '//button[@id="tabButton"]')
newtab_button.click()


print("switch to the new tab: get all window handles, switch to id other than main tab id ")
all_ids = driver.window_handles # list of all ID on the Chrome browser
print('IDs of browser tabs:', all_ids)
driver.switch_to.window(all_ids[1])
print('switched to new tab')

print("verify we are on the new tab: find the element with the text, verify the text as expected")
massage = driver.find_element(By.XPATH,'//h1[@id="sampleHeading"]').text
assert massage == 'This is a sample page', 'ERROR: text verification on the new tab FAILED'
# assert massage.lower() == 'This is a sample page'.lower()
print('text to new tab verified')

print("switch back to original tab")
driver.close() # closes second tab
driver.switch_to.window(all_ids[0])

# H/W : try the same way to switch between browser windows
win_button = '//button[@id="windowButton"]'

print("closing browser...")
time.sleep(5)
driver.quit() # closes browser
