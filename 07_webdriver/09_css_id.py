# 相对路径

from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://www.baidu.com"
driver.get(url)

# 这里是通过css定位-id
"""
css定位方法：
1.通过id属性定位   #id
2.通过class选择器   .class
3.通过元素选择器    input
4.属性选择器        [type=""]
5.层级选择器       p>input
另外还有一些扩展：
1.input[type^="p"] 以p开头
1.input[type$="p"] 以p结尾
1.input[type*="p"] 包含p

"""
driver.find_element_by_css_selector("#kw").send_keys("通过id")

sleep(3)

driver.quit()