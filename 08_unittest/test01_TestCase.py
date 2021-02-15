# 1.导包
import unittest

# 2.定义类必须继承unittest.TestCase,这样才表示这个类是一个测试用例
class Test(unittest.TestCase):

    # 3.方法名称必须test开头，这样unittest.TestCase才会自动执行
    def test_01(self):
        print("test01被执行")

    def test_02(self):
        print("test02被执行")



