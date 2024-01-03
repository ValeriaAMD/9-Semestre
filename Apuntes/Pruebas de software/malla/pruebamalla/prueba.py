from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()  
driver.get("https://www.ncei.noaa.gov/pub/data/nidis/shapefiles/")  
links= driver.find_elements(By.PARTIAL_LINK_TEXT, 'nadm-')
for anio in range(2010,2024):
    string='nadm-{}'.format(anio)
#for link in links:
 #   url = link.get_attribute('herf')
  #  if url.endswith('.zip'):
   #     driver.get(url)
    #    time.sleep(5)
#time.sleep(5)
#element = driver.find_element(By.LINK_TEXT, 'nadm-200211.zap')
#element.click()
#time.sleep(5)
