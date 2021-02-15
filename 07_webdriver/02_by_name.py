from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://www.baidu.com"
driver.get(url)

# 通过name属性定位元素
driver.find_element_by_name("wd").send_keys("通过name定位")

sleep(3)

driver.quit()