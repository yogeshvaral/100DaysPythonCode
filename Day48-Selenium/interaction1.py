

chrome_driver_path = "C:/Yogesh/Softwares/chromedriver_win32/chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

Fname = driver.find_element_by_name("fName")
Fname.send_keys("Yogesh1")

Lname = driver.find_element_by_name("lName")
Lname.send_keys("Varal1")

Email = driver.find_element_by_name("email")
Email.send_keys("Yogesh1@gmail.com")

# btn = driver.find_element_by_xpath('/html/body/form/button')
# btn.send_keys(Keys.ENTER)

button = driver.find_element_by_css_selector("form button")
button.click()

