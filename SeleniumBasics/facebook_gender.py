#<input type="radio" name="sex" value="1" id="u_0_9">


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
#driver.find_element(By.ID,"u_0_9").click()
driver.find_element_by_xpath("//label[text()='Female']").click()
print(driver.find_element_by_id("u`_0_9").is_selected())
print(driver.find_element_by_id("u_0_9").is_enabled())
print(driver.find_element_by_id("u_0_9").is_displayed())
