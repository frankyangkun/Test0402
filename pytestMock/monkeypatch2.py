# -*- coding:utf8 -*-
"""
2020-06-05 16:13:37
使用monkeypatch.setattr()可以将函数或者属性修改为你希望的行为
使用monkeypatch.setattr()结合类，模拟函数的返回对象
"""

# 假设有一个简单的功能，访问一个url返回网页内容
from urllib import request

def get(url):
    r = request.urlopen(url)  # 把url对应的网页内容抓下来
    print("***", r.read().decode('utf-8'))
    return r.read().decode('utf-8')


# if __name__ == '__main__':
#     get("http://140.246.137.19:45680")  # 返回对应url的html内容