from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
length = len(driver.find_elements_by_xpath("//img"))
print(length)