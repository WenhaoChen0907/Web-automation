# 生成报告
import time
import unittest
from Tools.HTMLTestRunner import  HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("case/", pattern="*.py")

    # 1.定义报告的位置
    path = "Report/"
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    filename = path + now + "Report.html"

    # 2.给文件写入数据
    with open(filename, "wb") as f:
        runner = HTMLTestRunner(stream=f, title="web自动化测试报告", description="win7系统")
        runner.run(suite)