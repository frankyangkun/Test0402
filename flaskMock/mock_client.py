# -*- coding:utf8 -*-
"""
2020-06-08 11:26:49
接口发送端
"""
import requests

body = {
    'd1': 'hello',
    'd2': 'flask123.'
}
resp = requests.post("http://localhost:9090/post", data=body)
print(resp.text)  # post请求就不能在浏览器直接访问了，只能运行后由服务端返回结果