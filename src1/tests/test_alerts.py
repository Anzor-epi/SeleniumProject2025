import time

from click import prompt

from src1.web_elements.form_elements import *

URL = "https://demoqa.com/alerts"

# Execution:
driver = initialize_browser()
open_website(driver, URL)

print("********** Scenario 1: automating alert interaction started ********")

print("********** Test case 1: getting text and clicking Ok button on Alert********")

print('# click on "click me" button for Ok-Cencel case')
confirm_button_xpath = '//button[@id="confirmButton"]'
click_me3 = driver.find_element(By.XPATH, confirm_button_xpath)
click_me3.click()

alert_box = driver.switch_to.alert
print(f"massage on the alert box: {alert_box.text} ------")
print('# clicking Ok on Alert')
alert_box.accept() # clicking ok button alert
time.sleep(0.5)

# than verifying green text showing " You selected Ok"
confirm_result_xpath = '//span[@id="confirmResult"]'
confirm_result_msg = driver.find_element(By.XPATH, confirm_result_xpath).text
print(f"confirmation result: '{confirm_result_msg}' ---- ")
assert confirm_result_msg.strip() == 'You selected Ok', 'ERROR: confirmation text verification FAILED!!'
time.sleep(0.5)
print("********** Test case 1: Completed  ********")

########################################################

print("********** Test case 2: clicking Cancel button on Alert********")
print('# click on "click me" button for Ok-Cencel case')
confirm_button_xpath = '//button[@id="confirmButton"]'
click_me3 = driver.find_element(By.XPATH, confirm_button_xpath)
click_me3.click()

print("# Click on Cancel")
alert_box = driver.switch_to.alert
alert_box.dismiss() # clicking Cancel on the Alert window
time.sleep(0.5)

print("# then verifying green text showing 'You selected Cancel' ")
confirm_result_msg = driver.find_element(By.XPATH, confirm_result_xpath).text
print(f"confirmation result: '{confirm_result_msg}' ---- ")
assert confirm_result_msg.strip() == 'You selected Cancel', 'ERROR: confirmation text verification FAILED!!'
time.sleep(0.5)

print("********** Test case 2: Completed  ********")

print("********** Test case 3: entering text and clicking Ok button on Alert********")
print('# click on "click me" button for Input-Ok-Cencel case')
click_me4_xpath = '//button[@id="promtButton"]'
prompt_result_xpath = '//span[@id="promptResult"]'
click_me4 = driver.find_element(By.XPATH, click_me4_xpath)
click_me4.click()

print('# enter "john doe" on the Alert window')
alert_box = driver.switch_to.alert
alert_box.send_keys('john doe')
print("click Okay!")
alert_box.accept() # clicking Okay on Alert tab
time.sleep(0.5)

print("# then verifying green text showing 'john doe' as part of the massage ") # same steps es before
prompt_result_msg = driver.find_element(By.XPATH, prompt_result_xpath).text  # changed to promt_result_xpath
print(f"confirmation result: '{prompt_result_msg}' ---- ")
assert "john doe" in prompt_result_msg, 'ERROR: confirmation text verification FAILED!!'
time.sleep(0.5)

print("********** Test case 3: Completed  ********")

print("********* Scenario 1: automating alert interaction completed ********")

close_browser(driver)