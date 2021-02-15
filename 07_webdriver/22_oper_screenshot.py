# 窗口截图
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)

url = 'file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)
sleep(2)

cur_handle = driver.current_window_handle

driver.find_element_by_link_text("注册A网页").click()

handles = driver.window_handles

for handle in handles:
    if handle != cur_handle:
        driver.switch_to.window(handle)

        driver.find_element_by_css_selector("#userA").send_keys("admin")
        driver.find_element_by_css_selector("#passwordA").send_keys("123456")
        driver.find_element_by_css_selector("#telA").send_keys("18711111111")
        driver.find_element_by_css_selector("#emailA").send_keys("admin@qq.com")
        # 保存截图
        driver.get_screenshot_as_file("../images/img1.jpg")


sleep(2)
driver.quit()