# -*- coding:utf8 -*-
"""
2020-06-08 11:27:15
模拟真实的支付接口
"""
import requests

# 这里接口用于测试，只返回数据，没有任何逻辑
data = {
    'out_trade_no': '20200608000001',
    'auth_code': '238462786598',
    'buyer_id': '230849038023',
    'seller_id': '293834982039',
    'subject': 'iphone11',
    'total_amount': '100'
}

resp = requests.post('http://localhost:9090/trade/purchase', json=data)
print(resp.json())