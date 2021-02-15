from time import sleep
# 导包

from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver

driver = webdriver.Firefox()

url = 'file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)

# 定位源元素
source = driver.find_element_by_css_selector("#div1")
# 定位目标元素
target = driver.find_element_by_css_selector("#div2")


# 实例化ActionChains类，调用拖拽鼠标方法，并执行
ActionChains(driver).drag_and_drop(source, target).perform()



sleep(3)
driver.quit()