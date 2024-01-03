from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://accounts.google.com')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.ID,'identifierId').send_keys('caro.campos251201@gmail.com')
driver.find_element(By.ID,'identifierId').send_keys(Keys.ENTER)
#driver.find_element(By.CLASS_NAME,'WpHeLc VfPpkd-mRLv6 VfPpkd').send_keys()


driver.implicitly_wait(20)