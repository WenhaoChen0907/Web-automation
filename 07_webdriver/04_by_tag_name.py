from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://www.baidu.com"
driver.get(url)

# 通过标签名字定位元素
# 注意：返回第一个标签元素
driver.find_element_by_tag_name("input").send_keys("通过标签定位")

sleep(3)

driver.quit()