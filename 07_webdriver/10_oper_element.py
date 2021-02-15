
"""
# 元素常用操作方法
1.send_keys()
2.clear()
3.click()
其他操作方法
1.size 返回元素大小
2.text 获取元素的文本
3.title 获取页面title
4.current_url 获取当前页面的url
5.get_attribute("xxx") 获取属性
6.is_displayed() 判断元素是否可见
7.is_enabled() 判断元素是否可用
"""

from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
driver.get(url)

driver.find_element_by_css_selector("#user").send_keys("admin")
sleep(3)
driver.find_element_by_css_selector("#password").send_keys("123456")
sleep(3)
driver.find_element_by_css_selector("#tel").send_keys("18611111111")
sleep(3)
driver.find_element_by_css_selector("#email").send_keys("132@qq.com")
sleep(3)
driver.find_element_by_css_selector("#tel").clear()
driver.find_element_by_css_selector("#tel").send_keys("18600000000")
sleep(3)
driver.find_element_by_css_selector("button").click()
sleep(3)

driver.quit()
