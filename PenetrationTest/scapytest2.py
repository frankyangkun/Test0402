# -*- coding:utf8 -*-
"""
2021-01-12 10:23:34
自定义scapy插件
价值在于:
1、如果需要批量构造一些数据包，不需要每次都去构造比如IP()/TCP()，效率太低
2、对于一些不常见的协议，也可以用它来自定义构造协议的包，因为包的内容都可以自己设置
"""

import logging

logging.getLogger("scapy").setLevel(1)  # 作用是有可能过程中scapy会报一些错，这里将它忽略，保持界面美观一点

from scapy.all import *


class Test(Packet):
    name = "Test packet"  # 必须要写，可能是scapy必须要求的，不写可能会报错
    fields_desc = [ShortField("test1", 1),
                   ShortField("test2", 2)]  # 定义具体的包结构，变量名是内置好的


def make_test(x, y):  # 调用这个自定义包
    return Ether() / IP() / Test(test1=x, test2=y)


if __name__ == '__main__':
    interact(mydict=globals(), mybanner="Test add-on v3.14")  # main可以不写，写出来是作为提示信息
