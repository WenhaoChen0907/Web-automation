# 隐式等待（掌握）
from selenium import webdriver

from time import sleep
from selenium.webdriver.common.by import By
# 导入等待类
from selenium.webdriver.support.wait import WebDriverWait
# 导入判断条件成立方法
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
url = 'file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)




# 隐式等待-全局元素生效 等待元素加载指定的时长，超出抛出NoSuchElementException异常
driver.implicitly_wait(10)
driver.find_element_by_css_selector("#use").send_keys("admin")



sleep(3)
driver.quit()