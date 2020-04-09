# -*- coding:utf8 -*-
"""
目标：
1、搜索组装测试套件
2、运行测试套件并生成测试报告（三方工具：HTMLTestRunner.py，可下载）
"""
#导包 unittest（组装测试套件）,HTMLTestRunner time
import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner

#第一步：组装测试套件
suite = unittest.defaultTestLoader.discover("./case",pattern="test*.py")

#第二步：指定报告存放路径及文件名称
file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))

#第三步：运行测试套件并生成测试报告
with open(file_path,"wb") as f: #由于是写入报告，所以是wb
    HTMLTestRunner(stream=f).run(suite) #调用报告模板，HTMLTestRunner()实例化，传入文件流f，运行测试套件
