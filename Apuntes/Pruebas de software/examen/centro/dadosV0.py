from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get('https://testsheepnz.github.io/random-number.html')
driver.implicitly_wait(20) 
select_element2 = driver.find_element(By.ID,'buildNumber')
select2 = Select(select_element2)
select2.select_by_value('13')
driver.find_element(By.ID,'rollDiceButton').click()
time.sleep(5) 
driver.find_element(By.ID,'numberGuess').send_keys('4')
driver.implicitly_wait(20)      
driver.find_element(By.ID,'submitButton').click()

