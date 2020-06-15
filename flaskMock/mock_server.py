# -*- coding:utf8 -*-
"""
2020-06-08 10:19:47
1、利用Flask框架mock接口，开发一个真正的web服务接口用于测试。
2、再结合pytest或unittest的mock模块写接口测试脚本。
"""
from flask import Flask, request, json  # 这个request是处理请求的，而requests库是发送请求的
import time
import random

# 实例化一个web服务对象
app = Flask(__name__)


# 创建一个方法来处理请求
# 定义一个路由，访问服务的根目录就可得到结果
@app.route("/")
def hello():
    return "<h1>hello flask.</h1>"  # 用浏览器就可以模拟，默认就是普通的get请求


# 构造一个接受post请求的响应
@app.route("/post", methods=['POST'])
def test_post():
    # 处理接口发送过来的两个参数，将两个参数拼接成一个字符串返回
    d1 = request.form['d1']  # 表单格式的数据
    d2 = request.form['d2']

    return d1 + d2


# 处理交易接口
@app.route("/trade/purchase", methods=['POST'])
def purchase():
    # 拿到客户端返回的数据
    data_client = json.loads(request.get_data())
    out_trade_no = data_client['out_trade_no']
    trade_no = time.strftime("%Y%m%d%H%M%S") + str(random.random()).replace("0.", '')  # 模拟trade_no
    auth_code = data_client['auth_code']

    data = {
        'code': '40004',
        'msg': 'Business Failed',
        'sub_code': 'ACQ.TRADE_HAS_SUCCESS',
        'sub_msg': '交易已被支付',
        'trade_no': '20200608000001999',  # 必须每次都是不一样的
        'out_trade_no': '3423232'  # 这个是client端发过来的，必须一致
    }

    # 把out_trade_no改成客户端发过来的数据
    data['out_trade_no'] = out_trade_no
    data['trade_no'] = trade_no

    # 验证授权码，这里做了简化，实际这个值应该是客户端向服务端申请的，确定好的
    if auth_code != '238462786598':
        return {'code': "50000", 'msg': '请求验证码失败。'}

    return data


if __name__ == '__main__':
    # 运行服务，并确定服务的ip和端口
    app.run("localhost", "9090")
