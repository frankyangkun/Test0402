# -*- coding:utf8 -*-
"""
用例地址 /Users/yang/PycharmProjects/Test0402_git/loginDemo/tests/test_login/test_login3.json.py
数据地址 /Users/yang/PycharmProjects/Test0402_git/loginDemo/data/test_login/test_login3.json
区别就是一个是tests目录，一个是data目录，文件后缀不同。即可根据测试用例目录获取到测试数据所在目录
"""

import os
import json


def get_data_path(case_path):
    file_name = os.path.dirname(case_path).split(os.sep + 'tests' + os.sep, 1)  # os.sep判断不同平台的分隔符，/或\，1表示1次分割
    test_data = os.sep.join([file_name[0], 'data', file_name[1], os.path.basename(case_path).replace('.py', '.json')])  # 拼接目录
    print("filename:", file_name)
    return test_data



def get_test_data(test_data_path):
    case = []
    headers = []
    # querystring = []
    payload = []
    expected = []

    with open(test_data_path, encoding='utf-8') as f:
        dat = json.loads(f.read())
        test = dat['test']
        for td in test:
            case.append(td['case'])
            headers.append(td.get('headers', {}))
            # querystring.append(td.get('querystring', {}))
            payload.append(td.get('payload', {}))
            expected.append(td.get('expected', {}))
    list_parameters = list(zip(case, headers, payload, expected))
    return case, list_parameters


# if __name__ == '__main__':
#     # print("datapath:", get_data_path("/Users/yang/PycharmProjects/Test0402_git/loginDemo/tests/test_login/test_login2.py"))
#     print(get_test_data("/Users/yang/PycharmProjects/Test0402_git/loginDemo/data/test_login/test_login3.json"))