# 相对路径

from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://www.baidu.com"
driver.get(url)

# 这里是通过属性定位
"""
xpath定位方法：
1.绝对路径
2.相对路径
3.通过属性+相对路径定位
4.层级+属性定位
5.逻辑+属性定位
另外还有一些扩展：
//*[text()=""]
//*[starts-with(@name, "xxx")] 表示以name属性以xxx开头
//*[contains(@name, "xxx")] 表示name属性包含xxx字符
"""
driver.find_element_by_xpath(".//*[@id='kw']").send_keys("淘宝官网")

sleep(3)

driver.quit()