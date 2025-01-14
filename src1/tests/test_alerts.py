import time

from src1.web_elements.form_elements import *

URL = "https://demoqa.com/alerts"

# Execution:
driver = initialize_browser()
open_website(driver, URL)

print("********** Scenario 1: automating alert interaction started ********")
time.sleep(2)

print("********* Scenario 1: automating alert interaction completed ********")

close_browser(driver)