# -*- coding:utf8 -*-
#导包
import unittest
from api.api_article import ApiArticle

#新建测试类 继承
class TestArticle(unittest.TestCase):
    #新建收藏文章方法
    def test01_collection(self):
        #临时数据
        url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer token-c9cdbf31e439486f9637471eb1630aee"}
        data = {"target":1}
        #调用收藏文章方法
        r = ApiArticle().api_post_collection(url, headers, data)
        #断言
        self.assertEqual(201,r.status_code)
        self.assertEqual("OK",r.json()["message"])
        print "收藏响应数据为：",r.json()

    # 新建取消收藏方法
    def test02_cancel(self):
        # 临时数据,target暂时用1代替,header和前面有所不同
        url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections/1"
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Bearer token-c9cdbf31e439486f9637471eb1630aee"}

        # 调用取消收藏方法
        r = ApiArticle().api_del_collection(url, headers)#必须要有括号才代表ApiArticle类的实例
        # 断言
        self.assertEqual(204,r.status_code)


if __name__ == '__main__':
    unittest.main()