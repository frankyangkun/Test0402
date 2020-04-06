# -*- coding:utf8 -*-
"""
    目标：实现登录接口对象封装
"""

#导包 requests
import requests

#新建类 登录接口对象
class ApiLogin(object):
#新建方法 登录方法
    def api_post_login(self,url,mobile,code):
        #headers，data 定义，调用post并返回响应对象
        headers = {"Content-Type": "application/json"}
        data = {"mobile":mobile,"code":code}
        return requests.post(url,headers=headers,json=data)
"""
    提示：url，mobile，code最后都需要从data数据文件中读取出来，做参数化使用
"""