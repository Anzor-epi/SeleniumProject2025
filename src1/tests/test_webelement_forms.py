from selenium.webdriver.support.select import Select

from src1.web_driver.webelements_forms import *

#URL = "https://demoqa.com/browser-windows"
URL = "https://travel.agileway.net/login"

user = 'agileway'
passw= 'testwise'

# Execution:
driver = initialize_browser()

print("****** Scenario 1: agileway travel website ****** ")
open_website(driver, URL)
signin(driver, user, passw)
singoff(driver)
print("****** Scenario 1: completed ****** ")

print("******  Scenario 2: select a flights ****** ")
open_website(driver, URL)
signin(driver, user, passw)
enter_flights_details(driver,'New York', 'Sydney')
#enter_flights_details(driver,'Sydney', 'New York')
enter_passenger_details(driver)
pay_ticket(driver)



# H/W flights : enter passenger details
# verify the text:   2024-01-01 New York to Sydney,  2024-02-01 Sydney to New York
# click next verify the flash_alert, get the text to verify
# enter lastname , firstname
# click on Next

# h/w flights : pay the ticket, get confirmation
# return booking number
# booking_number = driver.find_element(By.XPATH, "//span[@id='booking_number']").text

singoff(driver)
print("****** Scenario 2: completed ****** ")
close_browser(driver)