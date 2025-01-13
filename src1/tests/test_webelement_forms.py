from src1.web_driver.webelements_forms import *

#URL = "https://demoqa.com/browser-windows"
URL = "https://travel.agileway.net/login"

user = 'agileway'
passw= 'testwise'

# Execution:
driver = initialize_browser()

print("Scenario 1: agileway travel website")
open_website(driver, URL)
signin(driver, user, passw)
singoff(driver)
close_browser(driver)

print("Scenario 2: select a flights")
open_website(driver, URL)
signin(driver, user, passw)
# flights: select a flights
# flights: enter passenger details
# flights: pay the ticket, get confirmation
singoff(driver)
close_browser(driver)