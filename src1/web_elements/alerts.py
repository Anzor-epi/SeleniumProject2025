import time

from selenium.webdriver.common.by import By

# locators:
confirm_button_xpath = '//button[@id="confirmButton"]'
confirm_result_xpath = '//span[@id="confirmResult"]'
click_me4_xpath = '//button[@id="promtButton"]'
prompt_result_xpath = '//span[@id="promptResult"]'


def alert_get_text_and_click_ok(driver):
    # test data:
    expacted_confirm_msg = 'You selected Ok'

    print("********** Test case 1: getting text and clicking Ok button on Alert********")
    print('# click on "click me" button for Ok-Cencel case')


    click_me3 = driver.find_element(By.XPATH, confirm_button_xpath)
    click_me3.click()

    alert_box = driver.switch_to.alert
    print(f"massage on the alert box: {alert_box.text} ------")
    print('# clicking Ok on Alert')
    alert_box.accept() # clicking ok button alert
    time.sleep(0.5)

    print("# than verifying green text showing expacted_confirm_msg")
    confirm_result_msg = driver.find_element(By.XPATH, confirm_result_xpath).text
    print(f"confirmation result: '{confirm_result_msg}' ---- ")
    assert confirm_result_msg.strip() == expacted_confirm_msg, 'ERROR: confirmation text verification FAILED!!'
    time.sleep(0.5)
    print("********** Test case 1: Completed  ********")


def alter_click_cancel(driver):
    expacted_confirm_msg = 'You selected Cancel'

    print("********** Test case 2: clicking Cancel button on Alert********")
    print('# click on "click me" button for Ok-Cencel case')
    confirm_button_xpath = '//button[@id="confirmButton"]'
    click_me3 = driver.find_element(By.XPATH, confirm_button_xpath)
    click_me3.click()

    print("# Click on Cancel")
    alert_box = driver.switch_to.alert
    alert_box.dismiss()  # clicking Cancel on the Alert window
    time.sleep(0.5)

    print("# then verifying green text showing expacted_confirm_msg ")
    confirm_result_msg = driver.find_element(By.XPATH, confirm_result_xpath).text
    print(f"confirmation result: '{confirm_result_msg}' ---- ")
    assert confirm_result_msg.strip() == expacted_confirm_msg, 'ERROR: confirmation text verification FAILED!!'
    time.sleep(0.5)

    print("********** Test case 2: Completed  ********")


def alter_enter_text_and_click_ok(driver, alert_input):
    print("********** Test case 3: entering text and clicking Ok button on Alert********")
    print('# click on "click me" button for Input-Ok-Cencel case')
    click_me4 = driver.find_element(By.XPATH, click_me4_xpath)
    click_me4.click()

    print('# enter "john doe" on the Alert window')
    alert_box = driver.switch_to.alert
    alert_box.send_keys(alert_input)
    print("click Okay!")
    alert_box.accept()  # clicking Okay on Alert tab
    time.sleep(0.5)

    print("# then verifying green text showing alert_input as part of the massage ")  # same steps es before
    prompt_result_msg = driver.find_element(By.XPATH, prompt_result_xpath).text  # changed to promt_result_xpath
    print(f"confirmation result: '{prompt_result_msg}' ---- ")
    assert alert_input in prompt_result_msg, 'ERROR: confirmation text verification FAILED!!'
    time.sleep(0.5)

    print("********** Test case 3: Completed  ********")

