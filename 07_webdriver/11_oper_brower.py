"""
常用浏览器操作方法
1.maximize_window() 最大化
2.set_window_size(100,100) 设置浏览器大小
3.set_window_position(300,200) 浏览器位置
4.back() 后退
5.forward()前进
6.refresh()刷新
7.close() 关闭单个(主)窗口
8.quit()关闭所有webdriver启动的窗口
"""
from time import sleep

from selenium import webdriver
driver = webdriver.Firefox()
url = "file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html"
driver.get(url)
driver.maximize_window()
sleep(3)

driver.find_element_by_link_text("AA 新浪 网站").click()
sleep(3)
driver.back()
sleep(3)
driver.forward()