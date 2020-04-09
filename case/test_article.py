# -*- coding:utf8 -*-
#导包
import unittest
from api.api_article import ApiArticle
from parameterized import parameterized
from tools.read_json import ReadJson

#获取收藏文章数据
def get_data_add():
    data = ReadJson("article_add.json").read_json()
    arrs = []
    # append本身添加的就是[]，而我们需要的是[()]，所以里面要加上(),否则就把所有内容都添加到一个列表里了
    arrs.append((data.get("url"),  # data["url"]和get方式的区别是前者如果获取错误会报异常，后者则为空
                 data.get("headers"),
                 data.get("data"),
                 data.get("except_result"),
                 data.get("status_code")
                 ))
    return arrs


#获取取消收藏文章数据
def get_data_cancel():
    data = ReadJson("article_cancel.json").read_json()
    arrs = []
    # append本身添加的就是[]，而我们需要的是[()]，所以里面要加上(),否则就把所有内容都添加到一个列表里了
    arrs.append((data.get("url"),  # data["url"]和get方式的区别是前者如果获取错误会报异常，后者则为空
                 data.get("headers"),
                 data.get("status_code")
                 ))
    return arrs


#新建测试类 继承
class TestArticle(unittest.TestCase):
    #新建收藏文章方法
    @parameterized.expand(get_data_add())
    def test01_collection(self,url,headers,data,except_result,status_code):
        #临时数据
        # url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections"
        # headers = {"Content-Type": "application/json", "Authorization": "Bearer token-c9cdbf31e439486f9637471eb1630aee"}
        # data = {"target":1}

        #调用收藏文章方法
        r = ApiArticle().api_post_collection(url, headers, data)
        #断言
        # self.assertEqual(201,r.status_code)
        # self.assertEqual("OK",r.json()["message"])
        print "收藏响应数据为：",r.json()
        #使用动态数据获取状态码
        self.assertEqual(status_code, r.status_code)
        self.assertEqual(except_result, r.json()["message"])

    # 新建取消收藏方法
    @parameterized.expand(get_data_cancel())
    def test02_cancel(self, url, headers, status_code):
        # 临时数据,target暂时用1代替,header和前面有所不同
        # url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections/1"
        # headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Bearer token-c9cdbf31e439486f9637471eb1630aee"}

        # 调用取消收藏方法
        r = ApiArticle().api_del_collection(url, headers)#必须要有括号才代表ApiArticle类的实例
        # 断言
        # self.assertEqual(204,r.status_code)
        #使用动态数据获取状态码
        self.assertEqual(status_code, r.status_code)


if __name__ == '__main__':
    unittest.main()