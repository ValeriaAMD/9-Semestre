from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest

driver = webdriver.Firefox()
class Testcalculadora(unittest.TestCase):

    def test_resta(self):
        a = 22
        b = 11
        resta = a + b
        driver.get('https://testsheepnz.github.io/BasicCalculator.html')
        driver.implicitly_wait(20)
        driver.find_element(By.ID,'number1Field').send_keys('22')
        driver.find_element(By.ID,'number2Field').send_keys('11')
        select_element = driver.find_element(By.ID,'selectOperationDropdown')
        select = Select(select_element)
        select.select_by_value('0')
        driver.find_element(By.ID,'calculateButton').click()
        driver.implicitly_wait(15)
        element = driver.find_element(By.NAME,'numberAnswer')
        driver.implicitly_wait(15)
        result = element.get_attribute("value")
        result = int(result)

        self.assertEquals(resta,result)

if __name__ == '_main_':
    unittest.main()