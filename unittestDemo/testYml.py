#encoding:utf8

import yaml
import io
import unittest
from ddt import ddt,file_data

def readFile():
    params = []
    file = io.open('param.txt','r',encoding='utf8')
    for line in file.readlines():
        params.append(line.strip('\n').split(',')) #strip('\n')是读文件时去掉换行,readlines以每行为单位读取出来作为1个整体存入list
    return params

@ddt #必须要有@ddt
class forYml(unittest.TestCase):
    name = 123

    def setUp(self):
        print "**********setUP**********."

    def tearDown(self):
        print "**********tearDown**********."

    @file_data('ppp2.yml') #不要写错地方了，@file_data是写在方法上面，不是类上面
    def test_1(self, **kwargs): #不确定参数个数的写法
        self.name = kwargs.get('name')   #获取不了data: a: 111这种，会报错
        age = kwargs.get('age')
        print self.name #不能用这种方式赋值name，依然是原来的值123
        print age

        # self.assertEqual(name, 'frank', msg='not equal') #如果断言不相等，就打印括号里的字符串，自定义打印信息
        self.assertEquals(self.name, 'frank') #这种方式也可以，打印的是默认信息


    @unittest.skip('无条件跳过')
    @file_data('ppp.yml') #获取不了data: a: 111这种，会报错，其他的可以获取
    def test_6(self, value):
        print value

    @unittest.skipIf(readFile()!='', '结果为空，所以不运行！')
    def test_7(self): #这种方式可以获取data: a: 111
        print "global name is: ",self.name
        file = io.open("ppp2.yml",'r',encoding='utf8')
        result = yaml.load(file,Loader=yaml.FullLoader)
        print result

    @unittest.expectedFailure  #正常运行，但是如果运行出错，在结果中不算作出错处理，而是跳过的效果
    def test_8(self):
        self.assertEquals(1,2)

    def test_9(self):
        print 999
if __name__ == '__main__':
    unittest.main()

