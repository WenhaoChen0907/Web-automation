from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://www.baidu.com"
driver.get(url)

# 通过链接 部分文本 定位元素（模糊查找）
# click()为点击方法
driver.find_element_by_partial_link_text("About  ").click()

sleep(3)

driver.quit()