
from click import prompt

from src1.web_elements.alerts import *
from src1.web_elements.form_elements import *

URL = "https://demoqa.com/alerts"

print("********* Scenario 1: automating alert interaction started ********")
# Execution:
driver = initialize_browser()
open_website(driver, URL)

alert_get_text_and_click_ok(driver)
alter_click_cancel(driver)
alter_enter_text_and_click_ok(driver, 'john doe')
alter_enter_text_and_click_ok(driver, 'aowjdadjpa')

close_browser(driver)
print("********* Scenario 1: automating alert interaction completed ********")



