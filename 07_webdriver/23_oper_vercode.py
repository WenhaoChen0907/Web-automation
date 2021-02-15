"""对验证码的操作有4种方式，最常用的是cookie方式
通过传送cookie记录的方式绕过验证码，直接进入登录状态
提示：发送cookie之后要刷新
"""
from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://www.baidu.com")
sleep(2)

# 添加cookie
driver.add_cookie({"name":"BAIDUID", "value":"17519EA91171C84E74FE93D17A9FBE97:FG=1"})
driver.add_cookie({"name":"BDUSS", "value":"17519EA91171C84E74FE93D17A9FBE97"})
sleep(3)
# cookies = driver.get_cookies()
# for cook in cookies:
#     print("%s-----%s" % (cook["name"], cook["value"]) )


# 刷新
driver.refresh()
sleep(3)


driver.quit()


