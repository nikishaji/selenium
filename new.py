from selenium import webdriver
import time
browser = webdriver.Firefox()
#To navigate through an application
browser.get('http://thedemosite.co.uk/addauser.php')
#To get the title of the page
title=browser.title 
print("The title of the page is:-")
print(title) 
#To locate the element in the browser by name attribute and enter some text to the input box
browser.find_element_by_name('username').send_keys('Niki') 
browser.find_element_by_name('password').send_keys('Niki1')
#To suspend(wait) the current the execution
time.sleep(10)
#To locate the element in the browser by name attribute and submit the form
browser.find_element_by_name('FormsButton2').submit() 
time.sleep(10)
print("Successfully registered")

browser.get('http://thedemosite.co.uk/login.php')
title=browser.title
print("The title of the page is:-")
print(title)
browser.find_element_by_name('username').send_keys('ann')
browser.find_element_by_name('password').send_keys('Ni123')
time.sleep(20)
browser.find_element_by_name('FormsButton2').submit()
print("Login Failed")
time.sleep(10)
#To clear the contents of the input box
browser.find_element_by_name('username').clear()
browser.find_element_by_name('password').clear()
browser.find_element_by_name('username').send_keys('Niki')
browser.find_element_by_name('password').send_keys('Niki1')
time.sleep(20)
browser.find_element_by_name('FormsButton2').submit()
print("Successful Login")

