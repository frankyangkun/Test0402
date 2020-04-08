# -*- coding:utf8 -*-
#导包 requests
import requests

#新建文章对象类
class ApiArticle(object):
    #封装收藏文章方法
    def api_post_collection(self,url,headers,data):
        return requests.post(url,headers=headers,json=data)

    #封装取消收藏文章方法
    def api_del_collection(self,url,headers):
        return requests.delete(url,headers=headers)
