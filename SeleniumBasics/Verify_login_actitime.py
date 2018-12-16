from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")

print(driver.title)

driver.find_element(By.ID, "username").send_keys("admin")

driver.find_element_by_name("pwd").send_keys("manager")

driver.find_element_by_css_selector("#loginButton > div").click()

driver.close()