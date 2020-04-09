# -*- coding:utf8 -*-
"""
目标：在unittest框架中使用数据库工具类
"""
#导包 unittest 测试工具类
import unittest
from tools.read_db import ReadDB

#新建测试类 继承
class TestDB(unittest.TestCase):
    #新建测试方法
    def test_db(self):
        # sql = "select is_deleted from news_collection where user_id=1 and article_id=2"
        sql = "select article_id,is_deleted from news_collection where user_id=1"
        #调用get_sql_one方法
        # data = ReadDB().get_sql_one(sql)
        data = ReadDB().get_sql_all(sql)
        print "data响应数据：",data
        #断言
        sql2 = "select count(is_deleted) from news_collection where user_id=1"
        data2 = ReadDB().get_sql_one(sql2) #sql获取结果的个数
        print "sql结果获取，数量：",data2[0]

        for i in range(0,data2[0]):
            # self.assertEquals(0, data[i][1]) #多个结果中只要有1就会判定为失败，而且不会打印出失败的是哪一个，所以不方便，只适合用于判断对错
            # self.assertEqual(1, data[i][1], "deleted") #如果有结果是1的，就会判定为失败，并且会打印出deleted字样

            if data[i][1] is 0:
                print "文章id",data[i][0],"未取消收藏",data[i][1]
            else:
                print "文章id",data[i][0],"已取消收藏", data[i][1]
            #当然，这种方式就没法触发测试用例集的失败，所以还是要看具体的应用场景，如果用assertEquals，只要有不满足的，测试用例集就会运行失败。

if __name__ == '__main__':
    unittest.main()