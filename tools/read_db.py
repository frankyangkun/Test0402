"""
目标：完成数据库相关工具类封装
分析：1、主要方法
        假设：def get_sql_one(sql)
     2、辅助方法
        1、获取连接对象
        2、获取游标对象
        3、关闭游标对象方法
        4、关闭连接对象方法
"""
#导包 pymysql
import pymysql

#新建工具类 数据库
class ReadDB(object): #也可不写(object)
    conn = None
    #获取连接对象方法封装
    def get_conn(self):
        if self.conn is None:
            pymysql.connect("127.0.0.1","root","123456","hmtt",charset="utf8")
        return self.conn

    #获取游标对象方法封装
    def get_cursor(self):
        return self.get_conn().cursor()

    #关闭游标对象方法封装
    def close_cursor(self,cursor):#必须指定要关闭的游标
        if cursor:#游标对象不能为空
            cursor.close()

    #关闭连接对象方法封装
    def close_conn(self):
        if self.conn:#始终都只有1个连接对象，所以用self
            self.conn.close()
            self.conn = None#注意：关闭连接对象后，对象还在内存中，需要手工设置为None

    #主要执行方法 外界调用此方法即可
    def get_sql_one(self,sql):
        #定义游标对象及数据变量
        cursor = None
        data = None
        try:
            #获取游标对象
            cursor = self.get_cursor()
            #调用执行方法
            cursor.excute(sql)
            #获取结果
            data = cursor.fetchone()
        except Exception as e:
            print "get_sql_one error:",e #如果出现异常，打印异常信息
        finally:#无论是否有异常，都要关闭对象
            #关闭游标对象
            self.close_cursor(cursor)
            #关闭连接对象
            self.close_conn()
            #返回执行结果
            return data