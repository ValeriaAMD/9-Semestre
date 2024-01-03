from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://192.168.25.89:3000/inicio/agregarAu')
driver.find_element(By.ID,'nombreautor').send_keys('prueba')
driver.find_element(By.ID,'apellidoautor').send_keys('apellido de la prueba')
driver.find_element(By.ID,'origen').send_keys('el tec')
driver.find_element(By.LINK_TEXT, "Enviar").click()