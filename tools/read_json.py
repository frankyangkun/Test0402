# -*- coding:utf8 -*-
#导包
import json
import io #python2.7如需要在open()函数中使用encoding，需引用io模块

#打开json文件并获取文件流
# with io.open("../data/login.json", "r", encoding="utf-8") as f: #r表示读取，读取的文件命名为f
#     data = json.load(f)#调用load方法加载文件流
#     print "获取的数据为：", data #不要加括号，否则中文解析不出来
#     #print ('hhh', 'ggg') #加括号，解释器可能会把他当成元祖,打印的是('hhh','ggg')，而python3打印的是hhh ggg

#使用函数封装
# def read_json():
#     with io.open("../data/login.json", "r", encoding="utf-8") as f:
#         return json.load(f)

#使用函数封装，替换静态文件名
# def read_json():
#     with io.open("../data/login.json", "r", encoding="utf-8") as f:
#         return json.load(f)

#面向对象，用类的方式封装
class ReadJson(object):
    def __init__(self,filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with io.open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

# if __name__ == '__main__':
#     data = ReadJson("login.json").read_json()
    # arrs = []
    # #append本身添加的就是[]，而我们需要的是[()]，所以里面要加上(),否则就把所有内容都添加到一个列表里了
    # arrs.append((data.get("url"), #data["url"]和get方式的区别是前者如果获取错误会报异常，后者则为空
    #              data.get("mobile"),
    #              data.get("code"),
    #              data.get("except_result"),
    #              data.get("status_code")
    #              ))
    # print arrs
