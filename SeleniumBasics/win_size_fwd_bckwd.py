from selenium import webdriver
import time

class Demo:
    def method(self):
        driver = webdriver.Chrome()
        driver.get("https://www.flipkart.com/")
        print(driver.get_window_size())
        driver.forward()
        driver.back()
        time.sleep(5)

d = Demo()
d.method()
#container > div > header > div._1tz-RS > div > div._1Wr4v5 > a > div > span