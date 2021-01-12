# -*- coding:utf8 -*-
"""
2021-01-12 10:16:51
实现用scapy来做端口扫描，看端口是否是看着
ps:实际中使用nmap，或者直接用python调用nmap，这里主要是了解原理
"""
from scapy.all import *
# from scapy.layers.inet import IP, TCP

conf.verb = 0  # 屏蔽掉发包的中间过程，不用一直刷屏
ip = input("请输入要扫描的IP地址：")
lport = input("请输入要扫描的起始端口：")
hport = input("请输入要扫描的结束端口：")

for i in range(int(lport),int(hport)):
    pkt = IP(dst=ip) / TCP(dport=i)  # 不用导入第8行好像也可以，第7行就全导入了，但不知为何会有错误提示
    ans,uans = sr(pkt)  # sr的结果有2种，一种是回答的，一种是没有回答的，这里用回答了的
    res = str(ans[0])
    # print (res)
    if re.findall("SA",res):
        print(str(i)+"yes")
    else:
        pass


