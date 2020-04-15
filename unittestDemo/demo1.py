# -*- coding:utf8 -*-
import unittest

class forTest(unittest.TestCase):
    #类的初始化 必须要加@classmethod，传入的是cls
    @classmethod
    def setUpClass(cls):
        print "class\n"
    #类的资源释放 必须要加@classmethod，传入的是cls
    @classmethod
    def tearDownClass(cls):
        print "tclass"

    #用例的初始化
    def setUp(self):
        print "setUp."

    #用例的资源释放
    def tearDown(self):
        print "tearDown."

    #测试用例
    def test_a(self):
        print "test_a"

    def test_b(self):
        print "test_b"

    #普通方法
    def add(self,a,b):
        return a + b

    def test_callAdd(self): #作为测试用例去调用普通方法
        result = self.add(1,2)
        print result

if __name__ == '__main__':
    unittest.main(verbosity=2)
