# -*- coding:utf8 -*-
"""
2020-06-02 15:34:50
关联函数
注意main中的用法测试，取token
一般如果是json格式的数据，就按照平时的取值方式即可，比如response.json()["resultStatus"]["resultMessage"]
除非是普通的str类型字符串，比如取出来断言，可以用到这里的方法，已经测试成功，可用。
"""
import re  # re是python匹配字符串的模块，基于正则表达式实现
import json

def fetchStringByBoundary(data, LB=None, RB=None):
    rule = LB + r"(.*?)" + RB  # 遇到开始和结束就进行截取，比如accb，取cc(.*?)只保留括号内的内容
    print(type(rule),rule)
    slotList = re.findall(rule, data)
    return slotList


# if __name__ == '__main__':
#     re1 = "{\"resultStatus\":{\"resultCode\":\"0000\",\"resultMessage\":\"登录成功！\",\"timeStamp\":\"2020-06-03 10:52:48\"},\"value\":{\"loginAccount\":\"pzadmin\",\"password\":\"96E79218965EB72C92A549DD5A330112\",\"userId\":\"21cedd3bef6d4162a7f3a39be9cc7cd7\",\"token\":\"token-b476df1ede4d4c7da65d5982e9cbb9e3\"},\"exception\":null,\"attachments\":{}}"
#     # res = re.findall(r"token\":\"(.*?)\"},", re1)  # .*? 非贪婪(不加?就是贪婪，所有结果截在一起)，遇到开始和结束就进行截取，因此截取多次符合的结果，中间没有字符也会被截取
#     # print(type(res),res[0])  # 类型是list，取第一个即可得到token，获取成功
#
#
#     ss2 = json.loads(re1)  #当前re1是str类型，需要转换成json类型（真实情况可能获取的就是json格式，但json格式取值无需用正则，所以这里一般还是用于str的过滤）
#     # print("ss2-json", type(ss2), ss2)  # dict
#     # print("ss2-str", type(json.dumps(ss2)), json.dumps(ss2))  # str
#     ss = fetchStringByBoundary(re1, "token\":\"", "\"},")  # 这里的data还只能传str类型的，json类型的不支持,一般还是用于str的过滤
#     print(ss)  # 获取成功