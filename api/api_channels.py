# -*- coding:utf8 -*-
#导包
import requests

#新建对象类
class ApiChannels(object):
    #新建获取用户频道列表方法
    def api_get_channels(self,url,headers):
        #调用get请求
        return requests.get(url,headers=headers)