from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
driver.find_element_by_xpath('//*[@id="top"]/nav/ul/li[4]/a').click()

driver.find_element_by_css_selector("#user-indicator > a:nth-child(3)").click()
print(driver.find_element_by_css_selector("#user-indicator > a:nth-child(3)").get_attribute("href"))
print(driver.find_element_by_css_selector("#user-indicator > a:nth-child(3)").tag_name)
Text = driver.find_element_by_css_selector("#user-indicator > a:nth-child(3)").text
print(Text)


print(driver.find_element_by_css_selector("#user-indicator > a:nth-child(3)"))
driver.find_element_by_id("username").send_keys("ambika")
driver.find_element_by_id("password").send_keys("wordpass987%")

driver.find_element_by_xpath('//*[@id="content"]/section/div/form/div[3]/div/div/input').click()
