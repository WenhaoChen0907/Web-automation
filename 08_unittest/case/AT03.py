import unittest
import sys
import time
from selenium import webdriver
class T03(unittest.TestCase):

    def test(self):
        print("t03被执行")
        try:
            self.assertIn("admin", "hello")
        except AssertionError:
            # 抛出异常
            raise AssertionError

    def setUp(self):

        print("*开启浏览器*")

    def tearDown(self):
        print("*关闭浏览器*")