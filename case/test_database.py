# -*- coding:utf8 -*-
"""
目标：自动化测试中操作项目数据库
案例：判断用户id1是否收藏了id为2的文章 1-为收藏 0-收藏
"""
#导包 pymysql需要安装
import pymysql
#获取连接对象
conn = pymysql.connect("127.0.0.1","root","123456","hmtt",charset="utf8")
#获取游标对象 所有的操作都在游标对象里
cursor = conn.cursor()
#执行方法sql
sql = "select is_deleted from news_collection where user_id=1 and article_id=2"
cursor.execute(sql)
#获取结果并进行断言 0-收藏
# print cursor.fetchone() #结果是(0,)，没问题
result = cursor.fetchone()
assert 0 == result[0] #元组的获取：result[0]
#关闭游标对象
cursor.close()
#关闭连接对象
conn.close()