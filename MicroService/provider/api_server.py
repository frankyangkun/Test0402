# -*- coding:utf8 -*-
"""
2020-06-24 15:32:56
生产者服务，给我们提供json数据
"""
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # 默认为True，json 字符串中 key 的顺序与表中字段的顺序不一致
# flask 的 jsonfify() 方法在输出字段时，受app.config['JSON_SORT_KEYS'] 控制，默认为True，所以一般情况下 json 的输出是 key 的字母顺序输出的。
# jsonfiy() 方法会同时将 minetype 设置为 application/json


rsp_body = [
    {
        "salary": 45000,
        "name": "Hatsune Miku",
        "nationality": "Japan",
        "contact": {
            "Email": "hatsune.miku@woniuxy.com",
            "Phone Number": "13982739999"
        }
    }, {
        "salary": 80000,
        "name": "Takamachi Nahoha",
        "nationality": "Japan",
        "contact": {
            "Email": "takamachi.nahoha@woniuxy.com",
            "Phone Number": "18783723445"
        }
    }
]


@app.route('/information', methods=['GET'])
def test():
    get_name = request.args.get("name", "").lower()
    if get_name == 'miku':
        rsp = jsonify(rsp_body[0])
    elif get_name == 'nanoha':
        rsp = jsonify(rsp_body[1])
    else:
        rsp = jsonify({'status': '404 not found.'})
    return rsp


# 这个路由的定义主要是为了演示pact的ProviderState特性
@app.route('/setup', methods=['POST'])
def setup():  # 方法名字无所谓
    states = request.json.get("state")  # 这是flask框架中获取用户提交的json数据的方法
    # 通过这个状态字段的检查，来动态修改生产者服务端返回的数据内容
    if states == "No nationality":
        rsp_body[1]['nationality'] = None  # 这里直接用rsp_body的数据，为了省事
    else:
        rsp_body[1]['nationality'] = "Japan"
    return jsonify()  # 返回json数据，flask的用法


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
