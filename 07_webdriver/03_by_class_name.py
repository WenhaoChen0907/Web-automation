from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://www.baidu.com"
driver.get(url)

# 通过class属性定位元素
driver.find_element_by_class_name("s_ipt").send_keys("通过class定位")

sleep(3)

driver.quit()