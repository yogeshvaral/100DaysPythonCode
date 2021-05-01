chrome_driver_path = "C:/Yogesh/Softwares/chromedriver_win32/chromedriver.exe"
from selenium import webdriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

list =  driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul')


event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
driver.quit()