# iwebshop正向登录代码练习
import unittest
import sys
import time
from time import sleep
from selenium import webdriver

class IwebLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost/iwebshop/")
    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def testLogin(self):
        driver = self.driver

        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_css_selector("input[alt*='邮箱']").send_keys("admin")
        driver.find_element_by_css_selector("input[alt*='密码']").send_keys("123456")
        driver.find_element_by_css_selector(".submit_login").click()
        sleep(3)

        # 获取登陆信息
        text = driver.find_element_by_css_selector(".loginfo").text
        # 断言
        try:
            self.assertIn("admin", text)
        except AssertionError:
            # driver.get_screenshot_as_file("../images/img2.jpg")
            # 图片名称添加动态时间-加时间戳的写法，-推荐
            now = time.strftime("%Y_%m_%d %H_%M_%S")
            # 图片名称添加断言错误日志
            rep = sys.exc_info()[1]
            driver.get_screenshot_as_file("../images/%s--%s.jpg" % (now, rep))
            # 抛出异常
            raise AssertionError



        sleep(3)
        driver.find_element_by_css_selector(".reg").click()


if __name__ == '__main__':
    # 调用main方法执行unitetest内所有test开头方法
    unittest.main()
