
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

from src1.utilites import *

# Examples of webDelements class properties and methods


# locators

header_xpath = '//*[@id="container"]/h2'
username_id = 'username'
password_id = 'password'
remember_id = 'remember_me'
sign_in_name = 'commit'
flash_notice_id = 'flash_notice'

def initialize_browser():
    print("Initializing the browser, with chrome options")
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chr_options)  # instantiating webDriver class, driver object created
    driver.implicitly_wait(20) # applies all find_element or interactions with browser elements
    return driver


def open_website(driver,url):
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)


def signin(driver, uname, passwrd):
    flights_url = "https://travel.agileway.net/flights/start"

    print("verify header text")
    header_text = driver.find_element(By.XPATH, header_xpath).text
    assert header_text == 'Agile Travel', 'header text verification FAILED!'

    print("enter username")
    driver.find_element(By.ID, username_id).send_keys(uname)

    print("enter password")
    driver.find_element(By.ID, password_id).send_keys(passwrd)

    print("check remember me check box")
    checkbox = driver.find_element(By.ID, remember_id)
    checkbox.click()
    print("verify the remember me check box is checked")
    print(f"is remember me checked: {checkbox.is_selected()}")
    assert checkbox.is_selected(), 'checked box verification failed!'

    print("check signin button is enabled")
    signin = driver.find_element(By.NAME, sign_in_name)
    print(f"is signin button enabled: {signin.is_enabled()}")
    assert signin.is_enabled(), 'Signin button is not enabled!'

    print("submit form")
    signin.click()
    time.sleep(5)

    print("verify expected url: https://travel.agileway.net/flights/start ")
    assert driver.current_url == 'https://travel.agileway.net/flights/start', 'signin failed flights page was not opened'

    print("verify that signin message is displayed")
    msg = driver.find_element(By.ID, flash_notice_id).text
    assert msg == 'Signed in!', 'verification flash notice failed!'


def singoff(driver):
    print('click on sign off')
    driver.find_element(By.LINK_TEXT, 'Sign off (agileway)').click()
    #driver.find_element(By.PARTIAL_LINK_TEXT, 'gn off (agileway)').click()

    print("verify flash notice is Signed out!")
    msg = driver.find_element(By.ID, flash_notice_id)
    assert msg.is_displayed
    print(f"flash notice text: {msg.text}")
    assert msg.text == 'Signed out!', 'signin off failed'
    time.sleep(5)


def close_browser(driver):
    print("closing browser ...")
    driver.quit()


def enter_flights_details(driver, from_city, to_city):
    # locators
    trip_type_xpath= "//input[@value='return']"
    origin_name = 'fromPort'
    destination_name = 'toPort'
    second_checkbox_xpath = '//table[@id="flights"]/tbody/tr[2]/th/input'
    continue_xpath = "//input[@value='Continue']"

    print("# flights: select a flights")
    trip_type = driver.find_element(By.XPATH, trip_type_xpath)
    print(f"is return trip type selected:, {trip_type.is_selected()}")

    # check="true" - means returns should be selected by default
    print(f"attribute value: {trip_type.get_attribute('checked')}")
    print("select origin: New York")
    origin = Select(driver.find_element(By.NAME, origin_name))
    origin.select_by_visible_text(from_city)
    origin.select_by_index(1)

    print("select destination: Sydney")
    destination = Select(driver.find_element(By.NAME, destination_name))
    destination.select_by_visible_text(to_city)

    print("Select departure month and year")
    departing = Select(driver.find_element(By.ID, 'departMonth'))
    # departing.select_by_visible_text('January 2025')
    departing.select_by_value('012025')

    print("Select return month and year")
    returning = Select(driver.find_element(By.ID, 'returnMonth'))
    # returning.select_by_visible_text('March 2025')
    # returning.select_by_value('032025')
    returning.select_by_index(2)

    print("select second flight from the list")
    second_checkbox = driver.find_element(By.XPATH, second_checkbox_xpath)
    second_checkbox.click()
    print(f"is flight checked: {second_checkbox.is_selected()}")

    print("continue to next page")
    # driver.find_element(By.XPATH, "//input[@value='Continue' and @type='submit']").click()
    driver.find_element(By.XPATH, continue_xpath).click()


def enter_passenger_details(driver):
    """ create steps in test files then transfer here """
    pass


def pay_ticket(driver):
    """ create steps in test files then transfer here """
    pass

# Execution open test_webelements_forms

