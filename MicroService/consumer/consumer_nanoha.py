# -*- coding:utf8 -*-
"""
2020-06-24 16:49:42
消费者服务Nanoha
在Python2.x中主要为urllib和urllib2，这两个标准库是不可相互替代的。但是在Python3.x中将urllib2合并到了urllib
Pyhton2.x和Python3.x都有urllib3和requests, 它们不是标准库。urllib3提供线程安全连接池和文件post等支持，与urllib及urllib2的关系不大
相比较urllib模块，requests模块要简单很多，但是需要单独安装
requests是对urllib的进一步封装，更加友好简便
"""
import urllib3
import json
from flask import Flask
from flask import render_template
app = Flask(__name__)

# urllib3主要使用连接池进行网络请求的访问，所以访问之前需要先创建一个连接池PoolManager对象
# 为何要使用连接池？每发起一个独立的请求TCP就要经过三次握手的过程，而通过重用已经连接过的socket（HTTP1.1支持），连接过程将会减少服务器端资源的占用，应答速度也更快。


@app.route('/nanoha', methods=['GET'])
def miku_html():
    params = {"name": 'nanoha'}
    http = urllib3.PoolManager()  # 需要一个PoolManager实例来生成请求,由该实例对象处理与线程池的连接以及线程安全的所有细节，不需要任何人为操作
    resp = http.request('GET', 'http://localhost:8080/information', params)  # 通过request()方法创建一个请求。向生产者服务请求数据
    result = json.loads(resp.data.decode())  # 把响应填充到事先准备好的模板里
    return render_template('nanoha.html', result=result)  # render_template是Falsk的模板，功能是先引入miku.html，同时根据后面传入的参数，对html进行修改渲染


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)