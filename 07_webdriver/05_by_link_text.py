from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://www.baidu.com"
driver.get(url)

# 通过链接 全部文本 定位元素
# click()为点击方法
driver.find_element_by_link_text("新闻").click()

sleep(3)

driver.quit()