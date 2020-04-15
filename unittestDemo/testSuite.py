#encoding:utf8

import unittest
# from unittestDemo import * #不要写成这样
from unittestDemo.testYml import *

#创建测试套件 == list
suite = unittest.TestSuite()

#方法1：指定某个类的某些用例统一执行
#添加测试用例（子元素）到测试套件（集合）  写法是固定的，不是传统的面向对象写法
# suite.addTest(forYml('test_1')) #提示不存在test_1方法
# suite.addTest(forYml('test_6')) #@unittest.skip导致这里没法运行，提示不存在test_6方法
# suite.addTest(forYml('test_7')) #可运行
# suite.addTest(forYml('test_8')) #可运行
# suite.addTest(forYml('test_9')) #可运行

#方法2：指定某个类的某些用例统一执行
# case = [forYml('test_9'),forYml('test_7'),forYml('test_8')]
# suite.addTests(case) #注意这里是addTests

#方法3：指定运行路径，匹配想要运行的用例文件
# test_dir = './'
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

#方法4：指定某个类，运行里面的所有用例
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(forYml))
# suite.addTests(unittest.TestLoader().loadTestsFromName('unittestDemo.testYml')) #一样的效果，上面那种用的多一点

#套件通过TextTestRunner对象进行运行 ≈ unittest.main()
runner = unittest.TextTestRunner()
runner.run(suite)
# runner.run(discover) #方法3