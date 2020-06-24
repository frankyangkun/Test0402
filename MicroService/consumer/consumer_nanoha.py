# -*- coding:utf8 -*-
"""
2020-06-24 16:49:42
消费者服务Nanoha
"""
import urllib3
import json
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/nanoha', methods=['GET'])
def miku_html():
    params = {"name": 'nanoha'}
    http = urllib3.PoolManager()
    resp = http.request('GET', 'http://localhost:8080/information', params)  # 向生产者服务请求数据
    result = json.loads(resp.data.decode())  # 把响应填充到事先准备好的模板里
    return render_template('nanoha.html', result=result)  # render_template是Falsk的模板，功能是先引入miku.html，同时根据后面传入的参数，对html进行修改渲染


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8082)