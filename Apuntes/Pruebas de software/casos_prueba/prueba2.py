from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get('http://192.168.100.26:3000/inicio/listaL')
driver.implicitly_wait(15)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/table/tbody/tr[2]/td[7]/center/button').click()
driver.implicitly_wait(15)
driver.find_element(By.ID,'nombrelibro').send_keys('sjbfr')
driver.find_element(By.ID,'isbn').send_keys('398475')
driver.find_element(By.ID,'autorid').send_keys('2')
driver.find_element(By.ID,'editorial').send_keys('3')
driver.find_element(By.ID,'categoria').send_keys('1')
driver.implicitly_wait(15)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/button').click()