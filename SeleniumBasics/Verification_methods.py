from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/amsuresh/Documents/Selenim%20Class/Class%20I/pratice.html")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="Pythonradio"]').click()
time.sleep(5)
bool = driver.find_element_by_xpath('//*[@id="Pythonradio"]').is_selected()
print(bool)
print(driver.find_element_by_xpath('//*[@id="Pythonradio"]').is_displayed())
print(driver.find_element_by_xpath('//*[@id="Pythonradio"]').is_enabled())
print("-------")
print(driver.find_element(By.XPATH, '//*[@id="Pythonradio"]').is_selected())