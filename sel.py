#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path= "/usr/bin/geckodriver")
driver.get("https://www.facebook.com")
driver.maximize_window()
fbusername = 'username'
fbpassword = 'password'

emailFieldID = 'email'
passFieldID = 'pass'
loginButtonXpath = '//input[@value="Log In"]'
fblogoXpath = '(//a[contains(@href, "logo")])[1]'	
		
emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))	
passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
		
emailFieldElement.clear()
emailFieldElement.send_keys(fbusername)
passFieldElement.clear()
passFieldElement.send_keys(fbpassword)
loginButtonElement.click()

WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fblogoXpath))
#driver.quit()
	
	
