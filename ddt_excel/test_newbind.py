# -*- coding:utf8 -*-
"""
2020-09-10 11:12:39
1、将原设备所在设施A解绑；--> 根据原设备devA搜索出设施A的id FA_id，解绑
2、将实际安装设备所在设施B解绑； --> 根据实际设备devB搜索出设施B的id FB_id，解绑
3、将实际安装设备重新绑定在设施A；--> devB绑定FA_id
"""
import requests
from ddt_excel.DDTReadExcel import ddtreadexcel
import json
import unittest
from ddt import ddt, unpack, data

list1 = ddtreadexcel().getdata()


@ddt
class TestBind(unittest.TestCase):
    # 获取设施ID
    def getFacilityID(self, deviceName):
        url = "http://140.246.137.19:8002/locman/binding/queryDevicesByPage"
        headers = {"Content-Type": "application/json", "Token": "token-bfc76a3a2fb94fc8867001b780a37bd2"}
        body = '{"pageNum":1,"pageSize":12,"accessSecret":"aecde01f-9ae2-4876-84b7-c08ea25a4788","bingStatus":"",' \
               '"deviceTypeId":"","deviceId":' + deviceName + ',"facilityId":"","factoryId":"","whole":"false","startTim' \
                                                              'e":"","endTime":"","onLineState":""}'  # 这里的deviceId实际上是name，不是真正的id
        # print(body)
        j = json.loads(body)  # str转json

        resp = requests.post(url, headers=headers, json=j)
        resp1 = resp.json()
        return resp1

    # 设施设备解绑
    def unbind(self, deviceName):
        resp1 = self.getFacilityID(deviceName)
        valuelist = resp1["value"]["list"]
        facilityID = valuelist[0]["facilityId"]  # 原设备A的设施A的ID
        facilityCode = valuelist[0]["facilitiesCode"]
        DevID = valuelist[0]["deviceId"]
        DevCode = valuelist[0]["deviceName"]

        url = "http://140.246.137.19:8002/locman/binding/unbindFacilityWithDevices"
        headers = {"Content-Type": "application/json", "Token": "token-bfc76a3a2fb94fc8867001b780a37bd2"}
        body = '{"facilityId":"' + facilityID + '","devicesId":"' + DevID + '"}'
        # print(body)
        j = json.loads(body)  # str转json
        resp = requests.post(url, headers=headers, json=j)
        r1 = resp.json()
        print(r1["resultStatus"]["resultMessage"] + "| 设备id：" + deviceName + " | 设施id：" + facilityCode)

    # 解绑后的实际设备重新绑定原设施
    # 原设备OldDevName用于获取原设施id
    # 实际设备ActualDevName用于获取实际设备id ActualDevID
    def rebind(self, OldDevName, ActualDevName, OldFacilityID, OldFacilityCode):
        # resp1 = getFacilityID(OldDevName)  # 原设备A的name
        # valuelist = resp1["value"]["list"]
        # OldFacilityID = valuelist[0]["facilityId"]  # 原设备A的设施A的ID，由于在解绑后调用，所以这里实际已经获取不到原设施id了
        # OldFacilityCode = valuelist[0]["facilitiesCode"]

        resp2 = self.getFacilityID(ActualDevName)  # 实际设备devB的name
        valuelist = resp2["value"]["list"]
        ActualDevID = valuelist[0]["deviceId"]  # 实际设备devB的id
        ActualDevName = valuelist[0]["deviceName"]

        url = "http://140.246.137.19:8002/locman/binding/bindFacilityWithDevices"
        headers = {"Content-Type": "application/json", "Token": "token-bfc76a3a2fb94fc8867001b780a37bd2"}

        # facilityId：原设施id
        # deviceId：实际设备id，eb61d0f6f3c2819c538c11a3c3016003
        body = '{"facilityId":"' + OldFacilityID + '","deviceInfo":[{"deviceId":"' + ActualDevID + '", "deviceTypeId":"e8d9ed00278891ac4f89e96b9daf92ad"}]}'
        # print(body)
        j = json.loads(body)  # str转json
        resp = requests.post(url, headers=headers, json=j)
        r1 = resp.json()
        print(r1["resultStatus"]["resultMessage"] + "实际设备id：" + ActualDevName + " | 原设施id：" + OldFacilityCode)

    # def test(self): # 这里还没开始使用ddt模块，所以设备名写死，先跑通流程
    #     OldDevName = "29378"  # 原设备名
    #     ActualDevName = "29015"  # 实际设备名
    #
    #     resp1 = self.getFacilityID(OldDevName)  # 必须在解绑前先找到原设备对应的设施id，否则解绑后重新绑定时找不到
    #     valuelist = resp1["value"]["list"]
    #     OldFacilityID = valuelist[0]["facilityId"]  # 原设备A的设施A的ID
    #     OldFacilityCode = valuelist[0]["facilitiesCode"]
    #
    #     self.unbind(OldDevName)  # 原设备devA的name：29378，原设施id：510108011007043 解绑
    #     self.unbind(ActualDevName)  # 实际设备devB的name：29015，设施id：510108021721146 解绑
    #     self.rebind(OldDevName, ActualDevName, OldFacilityID, OldFacilityCode)

    @data(*list1)
    @unpack
    def test(self, **dict):
        OldNo = str(int(dict.get('原设备编号')))
        ActualNo = str(int(dict.get('实际安装设备编号')))
        # print(str(OldNo))
        resp1 = self.getFacilityID(OldNo)  # 必须在解绑前先找到原设备对应的设施id，否则解绑后重新绑定时找不到
        valuelist = resp1["value"]["list"]
        OldFacilityID = valuelist[0]["facilityId"]  # 原设备A的设施A的ID
        OldFacilityCode = valuelist[0]["facilitiesCode"]

        self.unbind(OldNo)  # 原设备devA的name：29378，原设施id：510108011007043 解绑
        #                 29372  510108021007042
        self.unbind(ActualNo)  # 实际设备devB的name：29015，设施id：510108021721146 解绑
        #                 29490  510108021308048
        self.rebind(OldNo, ActualNo, OldFacilityID, OldFacilityCode)


if __name__ == '__main__':
    unittest.main()
