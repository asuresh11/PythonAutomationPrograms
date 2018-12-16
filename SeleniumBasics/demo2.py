from selenium import webdriver
import time
class Demo1:

    def seleniumpgm(self):
        driver = webdriver.Chrome()
        driver.get("file:///C:/Users/amsuresh/Documents/Selenium%20class/demo1.html")
        time.sleep(10)
        print("program successful")
        driver.find_element_by_id("id-search-field").send_keys("Ambika")
        print("program successful")
        time.sleep(5)


sel = Demo1()
sel.seleniumpgm()