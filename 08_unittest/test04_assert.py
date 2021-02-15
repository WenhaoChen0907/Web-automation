import unittest
class Test(unittest.TestCase):
    def test_assert(self):
        # 注意，必须是self调用断言方法
        # self.assertEqual(1, 2)
        self.assertIn("A", "SDAm")