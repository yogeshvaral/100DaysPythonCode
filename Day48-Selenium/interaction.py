chrome_driver_path = "C:/Yogesh/Softwares/chromedriver_win32/chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

stats = driver.find_element_by_id("articlecount")
print(stats.text.split(" ")[0])
article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
# article_count.click()
all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()
search =  driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

btn = driver.find_element_by_css_selector("")

# driver.quit()


