from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.natura.com.mx/')
driver.maximize_window(20)
driver.find_element(By.LINK_TEXT, "PERFUMERÍA").click()
driver.maximize_window(20)