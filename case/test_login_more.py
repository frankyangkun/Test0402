# -*- coding:utf8 -*-
"""
    基于unittest框架实现
    目标：完成登录业务层实现
"""

#导包 unittest ApiLogin
import unittest
from api.api_login import ApiLogin
from tools.read_json import ReadJson
from parameterized import parameterized

def get_data():#处理返回的json中字典内容，达到我们要求的[()]格式
    datas = ReadJson("login_more.json").read_json()
    arrs = []
    for data in datas.values():  # 遍历获取所有value
        # append本身添加的就是[]，而我们需要的是[()]，所以里面要加上(),否则就把所有内容都添加到一个列表里了
        arrs.append((data.get("url"),  # data["url"]和get方式的区别是前者如果获取错误会报异常，后者则为空
                     data.get("mobile"),
                     data.get("code"),
                     data.get("except_result"),
                     data.get("status_code")
                     ))
    return arrs

#新建测试类
class TestLogin(unittest.TestCase):
    """
        使用unittest时要使用用例去执行，要想让unitest认识是用例，需要继承unittest.TestCase
    """
#新建测试方法
    @parameterized.expand(get_data())
    def test_login(self,url,mobile,code,except_result,status_code):
        #暂时存放数据 url，mobile，code
        # url = "http://ttapi.research.itcast.cn/app/v1_0/authorizations"
        # mobile = "13320192033"
        # code = "882477" #通过在浏览器执行另一个验证码接口在手机上收到

        #调用登录方法
        s = ApiLogin().api_post_login(url,mobile,code)
        print "查看响应结果：",s.json() #不要加括号，否则中文解析不出来
        #断言，响应信息及状态码
        # self.assertEquals("OK",s.json()['message'])
        self.assertEquals(except_result, s.json()['message'])
        # self.assertEquals(201, s.status_code)
        self.assertEquals(status_code, s.status_code)

if __name__ == '__main__':
    unittest.main() #用来测试 类中以 test 开头的测试用例
