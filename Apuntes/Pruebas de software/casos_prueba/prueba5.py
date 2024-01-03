from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://192.168.25.89:3000/inicio/listaAu')
driver.find_element(By.LINK_TEXT, "Eliminar").click()