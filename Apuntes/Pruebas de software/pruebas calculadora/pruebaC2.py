from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()
driver.get('https://testsheepnz.github.io/BasicCalculator.html')
select_element = driver.find_element(By.ID,'selectBuild')
select = Select(select_element)
select.select_by_value('2')
driver.implicitly_wait(15)
driver.find_element(By.ID,'number1Field').send_keys('30')
driver.find_element(By.ID,'number2Field').send_keys('50')
driver.find_element(By.ID,'selectOperationDropdown').send_keys('0')
driver.implicitly_wait(15)
driver.find_element(By.ID,'calculateButton').click()
driver.implicitly_wait(15)
driver.find_element(By.XPATH,"/html/body/section/div/div/div/form[5]/div/div[2]/font/font/input").click()
