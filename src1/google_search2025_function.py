import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def google_search(search_phrase, expected_result_num):
    url = "https://www.google.com"
    #locators
    search_box_name = 'q'
    search_box_id = 'result-stats'
    #expected_result_num = 200000000

    print("# Scenario: verify the google search results")
    print("# open the browser")
    driver = webdriver.Chrome() # initializes the browser, lunches the driver
    print('name of the browser:', driver.name)
    driver.maximize_window()
    #time.sleep(5)

    print("# open the website google.com")
    driver.get(url)
    time.sleep(1)

    print("# enter search_phrase ")
    # Locators: ways to finding element on HTML
    # ID, Name, xpath, Class name, css selector, link text, partial link text
    # search_box = driver.find_element(By.ID, 'APjFqb') #id="APjFqb", MAKE Sure it's uniqe on HTML
    search_box = driver.find_element(By.NAME, search_box_name) # name="q"
    search_box.send_keys(search_phrase)
    print("# then hit Enter button")
    search_box.send_keys(Keys.ENTER)

    print("# get the text of Search result ' about 277,000,000 results (0.66 seconds)")
    result_msg = driver.find_element(By.ID,search_box_id).text #id="result-stats"
    print("extracted massage:", result_msg)
    print("# then get the number of results from the message")
    # use split() function to break the message into smaller text based on space delimiter. returs a list
    number_text = result_msg.split()[1]
    print("number_text:", number_text)
    # use replace() function, replace(',', '')
    number_text_removed_comma = number_text.replace(',', '')
    print("result_num, removed comma:", number_text_removed_comma)
    print("is it a number?", type(number_text_removed_comma))
    result_num = int(number_text_removed_comma)
    print("is it a number:", type(result_num))

    print("# verify it is more than expected number")
    print("is search returned more than 200 mln results:", result_num > expected_result_num)
    assert result_num > expected_result_num, "FAIL. result number verification failed"

    time.sleep(15)
    print("Google search scenario completed!")

google_search('selenium', 200000000)
google_search('python', 1000000000)
google_search('test automation', 1000000000)
