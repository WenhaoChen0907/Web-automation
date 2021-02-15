
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)

url = 'file:///E:/BaiduNetdiskDownload/%E8%AF%BE%E7%A8%8B%E8%B5%84%E6%96%99/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%EF%BC%9Aweb%E8%87%AA%E5%8A%A8%E5%8C%96/02-%E8%AF%BE%E7%A8%8B%E6%BC%94%E7%A4%BA%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html'
driver.get(url)

"""
需求：城市选项-暂停2秒后选择上海A，暂停2秒后选择重庆，暂停2秒后选择广州
"""
"""
# 方法一
eles = driver.find_elements_by_css_selector("option")
for ele in eles:
    if ele.get_attribute("value") == "sh":
        ele.click()
        sleep(3)
for ele in eles:
    if ele.get_attribute("value") == "cq":
        ele.click()
        sleep(3)
for ele in eles:
    if ele.get_attribute("value") == "gz":
        ele.click()
        sleep(3)
"""

"""
# 方法二
driver.find_element_by_css_selector("[value='sh']").click()
sleep(3)
driver.find_element_by_css_selector("[value='cq']").click()
sleep(3)
driver.find_element_by_css_selector("[value='gz']").click()
sleep(3)
"""

# 方式三：新知识点：使用Select类专门定位操作select
# 1.导包 from selenium.webdriver.support.select import Select
# 2.实例化
ele = driver.find_element_by_css_selector("select")
sel = Select(ele)
# 3.操作选项方法有三种
# 1. select_by_index()                --> 根据option索引来定位，从0开始
# 2. select_by_value()                --> 根据option属性 value值来定位
# 3. select_by_visible_text()            --> 根据option显示文本来定位
sel.select_by_index(1)
sleep(2)
sel.select_by_index(3)
sleep(2)
sel.select_by_index(2)



sleep(3)
driver.quit()
