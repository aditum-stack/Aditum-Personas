"""
接口服务工具，通过API向Back服务更新数据
"""

import json
import logging
import requests

"""
数据结构类
"""
from entity.Personas import *

"""
Back IP
"""
backIp = "http://localhost:9006"

"""
基础数据接口
"""
communityUrl = backIp + "/community"
deviceUrl = backIp + "/device"
personUrl = backIp + "/person"
recordUrl = backIp + "/record"

"""
用户画像数据接口
"""
personasUrl = backIp + "/personas"
personasUpdateUrl = backIp + "/personas/updateByName"

"""
HTTP参数
"""
headers = {'content-type': 'application/json'}


# 添加Personas标签信息

def addPersonasByName(personnelId, labelName):
    """
    通过labelName添加用户画像标签
    """
    if personnelId == "" or labelName == "":
        logging.warning("addPersonasByName is \"\"")
        pass
    elif personnelId is None or labelName is None:
        logging.warning("addPersonasByName is None")
        pass
    else:
        request = {"personnelId": personnelId, "labelName": labelName}
        requests.post(personasUpdateUrl, params=request, headers=headers).json().get("data")


test_personnelId = 'e896799c6d0a48e6af7d184ce5bd15d6'
test_label_name = '帅'


def testForAllApi():
    """
    接口测试
    """
    addPersonasByName(test_personnelId, test_label_name)


if __name__ == '__main__':
    testForAllApi()
