# 操作frame/iframe表单
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)

url = 'file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)
sleep(2)

"""需求:此页面有三个注册界面，先填写最上边注册信息，
其次填写注册A页面注册信息，最后填写注册B页面信息"""
# 1.填写上面注册信息
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("123456")
driver.find_element_by_css_selector("#tel").send_keys("18711111111")
driver.find_element_by_css_selector("#email").send_keys("admin@qq.com")

# 2.切换到左侧的frame表单
driver.switch_to.frame("myframe1")

# 3.填写左侧注册信息
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("18711111111")
driver.find_element_by_css_selector("#emailA").send_keys("admin@qq.com")

# 4.切回到主页面
driver.switch_to.default_content()

# 5.切换到右侧的frame表单
driver.switch_to.frame("myframe2")

# 6.填写右侧注册信息
driver.find_element_by_css_selector("#userB").send_keys("admin")
driver.find_element_by_css_selector("#passwordB").send_keys("123456")
driver.find_element_by_css_selector("#telB").send_keys("18711111111")
driver.find_element_by_css_selector("#emailB").send_keys("admin@qq.com")



sleep(2)
driver.quit()