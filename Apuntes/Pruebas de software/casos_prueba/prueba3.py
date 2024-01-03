from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://192.168.100.26:3000/inicio/listaL')
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/table/tbody/tr[2]/td[7]/center/button').click()
