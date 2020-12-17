# -*- coding:utf8 -*-
"""
2020-12-16 15:26:26
需求：拆回来的100个设备修复完毕，需要验证是否全部修复成功
实现：
1、根据设备id查询出设备信息；
2、根据设备信息中的最新上报时间对比当前时间，如果是今天上报的，即可判定激活成功；
"""

import requests
from ddt_excel.DDTReadExcel import ddtreadexcel
import json
import unittest
import time
from ddt import ddt, unpack, data

@ddt
class TestBattery(unittest.TestCase):

    list1 = ddtreadexcel().getdata()
    passed = []
    failed = []
    null = []
    def getDeviceTime(self, DeviceId):
        url = "http://140.246.137.19:8002/locman/binding/queryDevicesByPage"
        # header = "Content-Type: application/json;charset=utf-8"  #不能这么写
        header = {"Content-Type": "application/json", "charset": "utf-8", "Token": "token-3acf710973834332af8e15f04329f998"}
        body = '{"pageNum":1,"pageSize":12,"accessSecret":"aecde01f-9ae2-4876-84b7-c08ea25a4788","bingStatus":"","deviceTypeId":"", ' \
               '"deviceId":' + DeviceId + ', "facilityId":"","factoryId":"","whole":"false","startTime":"","endTime":"","onLineState":""}'

        # print(body)
        j = json.loads(body) #str转json
        resp = requests.post(url, headers=header, json=j)
        resp1 = resp.json()
        # devTime = resp1["value"]["list"][0]["lastReportTime"]
        return resp1

    @data(*list1)
    @unpack
    def test(self, **dict):
        DeviceId = str(int(dict.get('设备编号')))


        if (self.getDeviceTime(DeviceId)["value"]["total"] != 0):

            lastReportTime = self.getDeviceTime(DeviceId)["value"]["list"][0]["lastReportTime"]

            localtime = time.strftime("%Y-%m-%d")

            if(localtime == lastReportTime.split(" ")[0]):
                print(DeviceId + " " + lastReportTime + "验证通过！")
                self.passed.append(DeviceId)
            else:
                print(DeviceId + " " + lastReportTime + "验证不通过！")
                self.failed.append(DeviceId)
        else:
            print(DeviceId + " 设备编号不存在！")
            self.null.append(DeviceId)

    @classmethod
    def tearDownClass(self):
        print("失败数：" + str(len(self.failed)))
        print("通过数：" + str(len(self.passed)))
        print("空设备：" + str(len(self.null)) + '\n')


if __name__ == '__main__':
    unittest.main()
