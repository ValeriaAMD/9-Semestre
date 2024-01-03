from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
def version_dados():
    
    driver.get('https://testsheepnz.github.io/random-number.html')
    driver.implicitly_wait(20)
    
    select_element2 = driver.find_element(By.ID,'buildNumber')
    select2 = Select(select_element2)
    select2.select_by_value(0)
    
    driver.find_element(By.ID,'rollDiceButton').click()
    driver.implicitly_wait(20)
    
    driver.find_element(By.ID,'numberGuess').send_keys('3')
        
    driver.find_element(By.ID,'submitButton').click()
    driver.implicitly_wait(20)
    
    element = driver.find_element(By.ID,'feedbackLabel')
    driver.implicitly_wait(20)
    
    result = element.get_attribute("value")
    driver.refresh()
    
    return int(result)