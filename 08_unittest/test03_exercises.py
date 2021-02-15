# iwebshop正向登录代码练习
import unittest
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
        driver.find_element_by_css_selector(".reg").click()


if __name__ == '__main__':
    # 调用main方法执行unitetest内所有test开头方法
    unittest.main()
