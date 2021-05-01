

chrome_driver_path = "C:/Yogesh/Softwares/chromedriver_win32/chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
count = 5000
while count >0:

    cookie.click()
    count -= 1