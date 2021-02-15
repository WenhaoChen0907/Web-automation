# 显式等待（了解即可）
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
sleep(3)


# 显式等待 
# By类的使用
ele = (By.CSS_SELECTOR, "#use")
# 如果元素找不到 10秒钟后报异常，找到的话发送admin
WebDriverWait(driver, 10).until(EC.presence_of_element_located(ele)).send_keys("admin")



sleep(3)
driver.quit()