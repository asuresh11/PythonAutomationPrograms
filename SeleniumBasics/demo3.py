from selenium import webdriver

driver = webdriver.Chrome()
expectedTitle = "ixigo - Flight Booking, Train Reservation, Hotels, Cheap Air Tickets"
driver.get("https://www.ixigo.com/")
actualTitle = driver.title
if expectedTitle == actualTitle:
    print("Title is correct")
    print(actualTitle)

