import unittest
class T02(unittest.TestCase):
    def test001(self):
        print("t02---test001被执行")

    def test002(self):
        print("t02---test002被执行")

    def setUp(self):
        print("*开启浏览器*")

    def tearDown(self):
        print("*关闭浏览器*")