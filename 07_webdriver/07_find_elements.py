from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://www.baidu.com"
driver.get(url)

# find_elements_by_xxx 方法，可获取所有符合的元素，作为列表返回
# 所以操作元素必须指定下标
driver.find_elements_by_tag_name("input")[0].send_keys("淘宝")

sleep(3)

driver.quit()