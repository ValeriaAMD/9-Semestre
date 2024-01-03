from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://192.168.100.26:3000/inicio/agregarL')
driver.find_element(By.ID,'nombrelibro').send_keys('prueba')
driver.find_element(By.ID,'isbn').send_keys('6666666')
driver.find_element(By.ID,'autorid').send_keys('2')
driver.find_element(By.ID,'editorial').send_keys('3')
driver.find_element(By.ID,'categoria').send_keys('1')
driver.find_element(By.XPATH, "/html/body/div/div/button").click()
#id autor 2
#id editorial 3
#id categoria 1