#! /usr/bin/env python
# -*- coding:utf8 -*-
"""
2020-06-25 20:26:40
Miku消费者服务和生产者服务之间的契约测试

注：这里不需要启动consumer_miku，因为它访问的是8080真实生产者服务
在此脚本里已经调用了query中的模拟消费者服务，访问的是1234pact模拟生产者服务

解决命令行执行脚本报错问题
1、找不到项目模块，sys.path.append('')添加路径到环境变量；
2、命令行执行时默认用的是python2.7，pycharm python模式执行时是3.8，搜索路径不同--指定3.8绝对路径运行解决；
3、指定3.8绝对路径后依然错误，因为pycharm是虚拟环境的3.8，pact安装在了虚拟环境，本地环境的3.8没安装，手动拷贝pact模块到本地3.8解决；
4、sys模块和atexit找不到的问题，解释器换成本地的python3.8解决；
"""
import sys

#  当我们导入一个模块时：import xxx，默认情况下python解析器会搜索当前目录、已安装的内置模块和第三方模块，搜索路径存放在sys模块的path中
#  该路径已经添加到系统的环境变量了，当我们要添加自己的搜索目录时，可以通过列表的append()方法
#  对于模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append('xxx')：
print("***sys.path***", sys.path)  # sys.path 返回的是一个列表,这个列表内的路径都添加到环境变量中去了,sys.path[0]是第一个
import os

print("当前工作目录：", os.getcwd())  # /Users/yang/PycharmProjects/Test0402_git/MicroService/Contract_test
# 获取项目路径下的目录
# os.chdir('/Users/yang/PycharmProjects/Test0402_git')  # 用于改变当前工作目录到指定的路径  必须的操作！**********************

# os.chdir('../../')  # 不把路径写死，根据具体的「当前路径」退2个路径

# 打印出项目路径下的目录
# for file in os.listdir(os.getcwd()):  # os.getcwd()查看当前工作目录
#     print("###", file)
print("修改后当前工作目录2：", os.getcwd())  # /Users/yang/PycharmProjects/Test0402_git

# 将项目路径保存至环境变量
# sys.path.append('/Users/yang/PycharmProjects/Test0402_git')  # 必须的操作！否则提示 No module named 'MicroService' *******
sys.path.append(os.getcwd())


# 注意：如果要导入该项目其他模块的包名，应将导入的方法写在上面方法的后面

import atexit  # 退出时资源自动释放,一般用来做一些资源清理的操作
from atexit import register  # 有时候重启pycharm后会找不到atexit模块，也搜不到，需要重新安装一下register
import unittest
from pact import Consumer, Provider
from MicroService.Contract_test.query import get_cartoon_characters

# 构造pact对象，定义消费者服务的名字并给它绑定一个生产者服务
pact = Consumer('Consumer Miku').has_pact_with(Provider('Provider'))  # 为消费者绑定一个生产者，名字可随便取
pact.start_service()  # 启动pact服务(Start the external Mock Service.)
atexit.register(pact.stop_service)  # 注册退出时，关闭pact服务,stop_service不能要括号，固定写法


# pact.stop_service()  # 由于atexit经常出错，可以不用


class GetMikuInfoContract(unittest.TestCase):
    def test_miku(self):
        # 定义响应的期望结果
        expected = {
            "salary": 45000,
            "name": "Hatsune Miku",
            "nationality": "Japan",
            "contact": {
                "Email": "hatsune.miku@woniuxy.com",
                "Phone Number": "13982739999"
            }
        }
        # 定义响应头
        headers = {
            "Content-Type": "application/json"
        }
        # 定义模拟生产者接受请求以及响应方式
        (pact
         .upon_receiving('a request for Miku')
         .with_request(
            method='GET',
            path='/information',
            query={'name': 'miku'})  # 如果是post请求，就是body=
         .will_respond_with(200, headers, expected))
        # 定义消费者服务向模拟生产者发出请求并获得响应
        with pact:  # 让pact去做请求
            result = get_cartoon_characters('miku')
        # 断言
        self.assertEqual(result.json(), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行前要先启动消费者服务，因为pact是模拟生产者(不过这里无需运行访问8080的，因为调用的query里已经有了访问1234的)
