#encoding:utf8

import yaml
import io
import unittest
from ddt import ddt,file_data

# file = io.open("ppp.yml",'r', encoding='utf-8')
# result = yaml.load(file,Loader=yaml.FullLoader)
# print result

@ddt #必须要有@ddt
class forYml(unittest.TestCase):
    @file_data('ppp2.yml') #不要写错地方了，@file_data是写在方法上面，不是类上面
    def test_1(self, **kwargs): #不确定参数个数的写法
        print kwargs.get('name')
        print kwargs.get('age')
        print "********"

if __name__ == '__main__':
    unittest.main()

