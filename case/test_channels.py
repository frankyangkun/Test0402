# -*- coding:utf8 -*-
#导包 unittest，ApiChannels
import unittest
from api.api_channels import ApiChannels

#新建测试类 继承
class TestChannels(unittest.TestCase):
    #新建测试方法
    def test_channels(self):#测试方法一定要test开头
        #临时数据，token需先运行登录接口获取，这里的token前有个空格和Bearer
        url = "http://ttapi.research.itcast.cn/app/v1_0/users/channels"
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer wehfuiDUIwoweIUAdwexjDjdwOKDeowieuxmnNBbdww"}#这里的token是随便写的
        #调用获取用户频道列表方法vvvv
        r = ApiChannels().api_get_channels(url,headers)#ApiChannels()必须要有括号才代表ApiChannels类的实例
        print "响应结果：",r.json()
        #断言 状态码和响应信息
        self.assertEqual(200,r.status_code)
        self.assertEqual("OK",r.json()['message'])

if __name__ == '__main__':
    unittest.main()
