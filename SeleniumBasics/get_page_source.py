from selenium import webdriver

class Demo4:

    def pgm(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        url = driver.page_source
        print(url)

d1 = Demo4()
d1.pgm()
