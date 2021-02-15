# 要使用操作键盘方法，必须导入类 Keys
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

url = 'file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)

ele = driver.find_element_by_css_selector("#user")
ele.send_keys("admin1")
sleep(3)
# 键盘删除一个字符
ele.send_keys(Keys.BACK_SPACE)
sleep(3)
# 键盘全选
ele.send_keys(Keys.CONTROL, 'a')
sleep(3)
# 键盘复制
ele.send_keys(Keys.CONTROL, 'c')
sleep(3)
# 键盘粘贴
pwd = driver.find_element_by_css_selector("#password")
pwd.send_keys(Keys.CONTROL, 'v')

sleep(3)
driver.quit()
"""
常用键盘操作方法
1.send_keys(Keys.BACK_SPACE)
2.send_keys(Keys.SPACE) 空格键
3.send_keys(Keys.TAB) 制表符
4.send_keys(Keys.ESCAPE) 回退键
5.send_keys(Keys.ENTER) 回车键
6.send_keys(Keys.CONTROL, 'a') 全选
7.send_keys(Keys.CONTROL, 'c') 复制
8.send_keys(Keys.CONTROL, 'v') 粘贴
"""