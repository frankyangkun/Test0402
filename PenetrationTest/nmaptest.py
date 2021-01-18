# -*- coding:utf8 -*-
"""
2021-01-15 10:52:57
调用nmap，但是会报错，提示『'nmap program was not found in path. 』但在kali上可以运行
是因为我mac上没装nmap，只装了python-nmap，python-nmap去调用nmap没发调用。而kali是两个都装了
mac端安装nmap后，可成功运行。
"""
import nmap

nm = nmap.PortScanner()
nm.scan('131.10.10.32', None, '-A')  # 第二个参数是端口，None代表全端口
status = nm.scanstats()
info = nm.scaninfo()
a = nm['131.10.10.32']
print('info:',info,'\r\n','status:',status,'\r\n',a)