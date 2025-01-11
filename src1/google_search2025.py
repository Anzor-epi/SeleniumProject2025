import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

print("# Scenario: verify the google search results")
print("# open the browser")
driver = webdriver.Chrome() # initializes the browser, lunches the driver
print('name of the browser:', driver.name)
driver.maximize_window()
#time.sleep(5)

print("# open the website google.com")
driver.get("https://www.google.com")
time.sleep(1)

print("# enter 'selenium' ")
# Locators: ways to finding element on HTML
# ID, Name, xpath, Class name, css selector, link text, partial link text
# search_box = driver.find_element(By.ID, 'APjFqb') #id="APjFqb", MAKE Sure it's uniqe on HTML
search_box = driver.find_element(By.NAME, 'q') # name="q"
search_box.send_keys('selenium')
print("# then hit Enter button")
search_box.send_keys(Keys.ENTER)

print("# get the text of Search result ' about 277,000,000 results (0.66 seconds)")
result_msg = driver.find_element(By.ID,'result-stats').text #id="result-stats"
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

print("# verify it is more than 200000")
print("is search returned more than 200 mln results:", result_num > 200000000)
assert result_num > 200000000, "FAIL. result number verification failed"

time.sleep(15)
print("Google search scenario completed!")
