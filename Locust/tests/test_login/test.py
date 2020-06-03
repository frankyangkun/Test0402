# -*- coding:utf8 -*-
# from Locust.utils.get_data import get_test_data, get_data_path
from loginDemo.utils.get_data import get_test_data, get_data_path

case, param = get_test_data(get_data_path(__file__))  # __file__当前文件路径
