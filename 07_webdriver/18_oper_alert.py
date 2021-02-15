# 操作警告框
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)

url = 'file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)

"""
需求：首先点击页面alert按钮，其次输入用户名：admin

"""
# 定位
driver.find_element_by_css_selector("#alert").click()

# 处理警告框
# 第一步：获取
alert = driver.switch_to.alert

"""第二步：处理 
1. text                 --> 返回alert/confirm/prompt中的文字信息
2. accept()                --> 接受对话框选项
3. dismiss()            --> 取消对话框选项
"""
alert.accept()

# 输入用户信息
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("123")
driver.find_element_by_css_selector("#tel").send_keys("admin")
driver.find_element_by_css_selector("#email").send_keys("admin")

sleep(3)
driver.quit()

