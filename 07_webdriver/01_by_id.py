# 1.导入包
from time import sleep

from selenium import webdriver
# 2.实例化浏览器
driver = webdriver.Firefox()
# 打开项目-url
driver.get("http://www.baidu.com")
# 通过id属性定位元素
input = driver.find_element_by_id("kw")
# 操作元素
input.send_keys("淘宝")
# 暂停三秒
sleep(3)
# 关闭浏览器
driver.quit()
