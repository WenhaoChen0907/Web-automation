# 操作滚动条
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)

url = 'file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)
sleep(2)

"""需求:打开页面2秒后，滚动条拉倒最底层"""
"""
第一步：定义js语句，第二步，webdriver执行js语句
"""
js1 = "window.scrollTo(0, 10000)"
driver.execute_script(js1)



sleep(2)
driver.quit()