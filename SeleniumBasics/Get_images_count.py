from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
image = driver.find_elements_by_xpath("//img")
for i in image:
    pic = i.get_attribute("src")
    print(len(pic))
