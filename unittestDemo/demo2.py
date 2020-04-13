# coding:utf-8
'''
结合DDT自动化实现
'''
import unittest
from selenium import webdriver
import time
from ddt import ddt, data, unpack, file_data
import io


# 类外面的方法不用加self
def readFile():
    params = []
    file = io.open('param.txt','r',encoding='utf8')
    for line in file.readlines():
        params.append(line.strip('\n').split(',')) #strip('\n')是读文件时去掉换行,readlines以每行为单位读取出来作为1个整体存入list
    return params

@ddt
class forTest(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get('http://www.baidu.com')
        print "**********setUP**********."

    def tearDown(self):
        # time.sleep(5)
        # self.driver.quit() #确保浏览器退出
        print "**********tearDown**********."

    # @data(('xx1','xx2'),('yy1','yy2'))
    # def test_1(self,txt1,txt2):
    #     self.driver.find_element_by_id('kw').send_keys(txt1)
    #     self.driver.find_element_by_id('su').click()
    #     print txt2

    # @data(('aa', 'AA'), ('bb', 'BB'))
    # @unpack
    # def test_2(self, x, y):
    #     print "x:", x
    #     print "y:", y
    #     print "*********"

    # @data([1,2],('rr','tt')) #也可以写成(1,2)
    # @unpack
    # def test_3(self,x,y):
    #     print "x:", x
    #     print "y:", y
    #     print "*********"

    # @file_data("../data/login.json") #只能单个参数轮询，不能多参数指定，还是 @parameterized.expand(get_data_add())更加实用
    # def test_4(self,value):
    #     print "json value1:", value

    # @data(*readFile()) #readFile读取的数据是存放在列表[]中，所以要加*，如果存放在字典，就加**
    # @unpack
    # def test_5(self,param1,param2):#如果txt里的4个数据都是写到一行，这里就需要传4个参数
    #     print param1
    #     print param2


    @file_data('ppp.yml')
    def test_6(self,value):
        print value

if __name__ == '__main__':
    unittest.main(verbosity=2)