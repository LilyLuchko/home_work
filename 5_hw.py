from selenium import webdriver
from selenium.webdriver.common.by import By
def saucedemo():
	driver=webdriver.Chrome()
	driver.get("https://www.saucedemo.com")
	text_username=driver.find_element(By.CSS_SELECTOR,'#user-name')
	text_password=driver.find_element(By.CSS_SELECTOR,'#password')
	butoon_submit=driver.find_element(By.CSS_SELECTOR,'#login-button')
	if text_username and text_password and butoon_submit:
		print('Элементы найдены')
    

saucedemo()
