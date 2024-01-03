from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://192.168.25.89:3000/inicio/agregarM')
driver.find_element(By.ID,'monto').send_keys('25')
driver.find_element(By.ID,'fechaP').send_keys('2023-10-02')
driver.find_element(By.ID,'prest').send_keys('2')
driver.find_element(By.LINK_TEXT, "Enviar").click()