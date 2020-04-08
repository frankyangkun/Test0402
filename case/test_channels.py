# -*- coding:utf8 -*-
#导包 unittest，ApiChannels
import unittest
from api.api_channels import ApiChannels
from tools.read_json import ReadJson
from parameterized import parameterized

def get_data():
    data = ReadJson("channel.json").read_json()
    arrs = []
    # append本身添加的就是[]，而我们需要的是[()]，所以里面要加上(),否则就把所有内容都添加到一个列表里了
    arrs.append((data.get("url"),  # data["url"]和get方式的区别是前者如果获取错误会报异常，后者则为空
                 data.get("headers"),
                 data.get("except_result"),
                 data.get("status_code")
                 ))
    return arrs

#新建测试类 继承
class TestChannels(unittest.TestCase):
    #新建测试方法
    @parameterized.expand(get_data())
    def test_channels(self,url,headers,status_code,except_result):#测试方法一定要test开头
        #临时数据，token需先运行登录接口获取，这里的token前有个空格和Bearer
        # url = "http://ttapi.research.itcast.cn/app/v1_0/users/channels"
        # headers = {"Content-Type": "application/json", "Authorization": "Bearer wehfuiDUIwoweIUAdwexjDjdwOKDeowieuxmnNBbdww"}#这里的token是随便写的
        #调用获取用户频道列表方法
        r = ApiChannels().api_get_channels(url,headers)#ApiChannels()必须要有括号才代表ApiChannels类的实例
        print "响应结果：",r.json()
        #断言 状态码和响应信息
        # self.assertEqual(200,r.status_code)
        # self.assertEqual("OK",r.json()['message'])
        #断言，使用参数化
        self.assertEqual(status_code, r.status_code)
        self.assertEqual(except_result, r.json()['message'])
if __name__ == '__main__':
    unittest.main()
