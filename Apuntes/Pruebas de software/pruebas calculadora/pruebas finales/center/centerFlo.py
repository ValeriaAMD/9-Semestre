from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
def ope_central_flo(version,operacion,num1,num2):
    
    driver.get('https://testsheepnz.github.io/BasicCalculator.html')
    driver.implicitly_wait(20)
    
    select_element2 = driver.find_element(By.ID,'selectBuild')
    select2 = Select(select_element2)
    select2.select_by_value(version)
    
    driver.find_element(By.ID,'number1Field').send_keys(num1)
    driver.find_element(By.ID,'number2Field').send_keys(num2)
    
    select_element = driver.find_element(By.ID,'selectOperationDropdown')
    select = Select(select_element)
    select.select_by_value(operacion)
    
    driver.find_element(By.ID,'calculateButton').click()
    driver.implicitly_wait(20)
    
    element = driver.find_element(By.NAME,'numberAnswer')
    driver.implicitly_wait(20)
    
    result = element.get_attribute("value")
    driver.refresh()
    
    return float(result)