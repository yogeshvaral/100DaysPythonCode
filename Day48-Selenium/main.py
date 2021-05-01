chrome_driver_path = "C:/Yogesh/Softwares/chromedriver_win32/chromedriver.exe"
from selenium import webdriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.in/dp/B07X8V5YKR/ref=pc_mcnc_merchandised-search-11_?pf_rd_s=merchandised-search-11&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=TQEZZ2RGHSW33KFQGDSJ&pf_rd_p=4c0716f1-441a-47ee-ad12-281cdb914f9a")
price = driver.find_element_by_id("priceblock_dealprice")
# price = driver.find_element_by_id("")
print(price.text)
priceX = driver.find_element_by_xpath('//*[@id="priceblock_dealprice"]')
print(priceX.text)
# driver.close()
driver.quit()