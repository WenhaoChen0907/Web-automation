# 套件的运行案例需要 TestCase(里面有Fixture) TextTestRunner配合使用

# 1.导包
import unittest
from case.T01 import T01
from case.T02 import T02

if __name__ == '__main__':


    """
    # 2.实例化
    suite = unittest.TestSuite()
    # 3.1添加testcase--方法一（一个test方法添加一次）比较笨需要一个一个添加
    suite.addTest(T01("test001"))
    suite.addTest(T01("test002"))
    suite.addTest(T02("test001"))
    suite.addTest(T02("test002"))
    """

    """
    # 2.实例化
    suite = unittest.TestSuite()
    # 3.2添加testcase--方法二（一个类添加一次）稍微好一点
    suite.addTest(unittest.makeSuite(T01))
    suite.addTest(unittest.makeSuite(T02))
    """


    # 2.实例化
    # 3.3添加testcase--方法三（一次性添加文件夹下所有py文件）[重点]
    suite = unittest.defaultTestLoader.discover("case/", pattern="T*.py")


    # 4.运行
    runner = unittest.TextTestRunner()
    runner.run(suite)


