from selenium import webdriver

class seleniumDemoclass():

    def seleniumdemo(self):

        driver = webdriver.Chrome()
        driver.get("https://www.python.org/")


seleniumDemoclass().seleniumdemo()