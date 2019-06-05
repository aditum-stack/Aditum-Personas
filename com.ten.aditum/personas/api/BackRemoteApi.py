"""
接口服务工具，包含了从Aditum-Back服务中获取接口数据的各种方法
"""

import json
import logging
import requests

from entity.DeviceAccessCount import DeviceAccessCount
from util import TimeUtil

"""
数据结构类
"""
from entity.Community import *
from entity.Device import *
from entity.Person import *
from entity.Record import *
from entity.AccessAddress import *
from entity.AccessTime import *

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
统计分析数据接口
"""
accessPersonUrl = backIp + "/access/person"
accessDeviceUrl = backIp + "/access/device"

"""
HTTP参数
"""
headers = {'content-type': 'application/json'}


# 获取全量数据

def getForAllPerson(communityId=""):
    """
    获取该社区下的所有person

    :param: communityId社区ID，若不填，则全量
    :return: person[]
    """
    if communityId != "":
        request = {"communityId": communityId}
        personJsonList = requests.get(personUrl, params=request, headers=headers).json().get("data")
    else:
        personJsonList = requests.get(personUrl, params={}, headers=headers).json().get("data")

    if personJsonList == "":
        logging.warning("getForAllPerson fail")
        return None
    if personJsonList is None:
        logging.warning("getForAllPerson fail")
        return None

    personList = []
    for personJson in personJsonList:
        personEntity = Person(personJson)
        personList.append(personEntity)
    return personList


def getForAllRecord():
    """
    获取所有record

    :return: record[]
    """
    recordJsonList = requests.get(recordUrl, params={}, headers=headers).json().get("data")

    if recordJsonList == "":
        logging.warning("getForAllRecord fail")
        return None
    if recordJsonList is None:
        logging.warning("getForAllRecord fail")
        return None

    recordList = []
    for recordJson in recordJsonList:
        recordEntity = Record(recordJson)
        recordList.append(recordEntity)
    return recordList


# 获取Person相关数据

def getForRecordByPersonId(personnelId):
    """
    获取指定person的所有record

    :param personnelId: personnelId
    :return: record[]
    """
    request = {"personnelId": personnelId}
    recordJsonList = requests.get(recordUrl, params=request, headers=headers).json().get("data")

    if recordJsonList == "":
        logging.warning("getForRecordByPersonId fail")
        return None
    if recordJsonList is None:
        logging.warning("getForRecordByPersonId fail")
        return None

    recordList = []
    for recordJson in recordJsonList:
        recordEntity = Record(recordJson)
        recordList.append(recordEntity)
    return recordList


def getForAccessTimeByPersonId(personnelId):
    """
    获取指定person的所有accessTime

    :param personnelId: personnelId
    :return: accessTime
    """
    request = {"personnelId": personnelId}
    accessTimeJson = requests.get(accessPersonUrl + "/time", params=request, headers=headers).json().get("data")
    if accessTimeJson == "":
        logging.warning("getForAccessTimeByPersonId fail")
        return None
    if accessTimeJson is None:
        logging.warning("getForAccessTimeByPersonId fail")
        return None

    accessTime = AccessTime(accessTimeJson)
    return accessTime


def getForAccessAddressByPersonId(personnelId):
    """
    获取指定person的所有accessAddress

    :param personnelId: personnelId
    :return: accessAddress
    """
    request = {"personnelId": personnelId}
    accessAddressJson = requests.get(accessPersonUrl + "/address", params=request, headers=headers).json().get("data")

    if accessAddressJson == "":
        logging.warning("getForAccessAddressByPersonId fail")
        return None
    if accessAddressJson is None:
        logging.warning("getForAccessAddressByPersonId fail")
        return None

    accessAddress = AccessAddress(accessAddressJson)
    return accessAddress


# 获取Device相关数据

def getForYesterdayDeviceCount():
    """
    获取T+1的所有设备按天访问热度

    :return: deviceCountList
    """
    yesterday = TimeUtil.getYesterdayDate()
    # test数据 yesterday = "2019-05-28"
    request = {"logDate": yesterday}
    deviceCountJson = requests.get(accessDeviceUrl + "/countByDay", params=request, headers=headers).json().get("data")

    if deviceCountJson == "":
        logging.warning("getForYesterdayDeviceCount fail")
        return None
    if deviceCountJson is None:
        logging.warning("getForYesterdayDeviceCount fail")
        return None

    deviceCountList = []
    for deviceCountJson in deviceCountJson:
        deviceCount = DeviceAccessCount(deviceCountJson)
        deviceCountList.append(deviceCount)
    return deviceCountList


def testForAllApi():
    """
    接口测试
    """
    # # 全量测试
    # personList = getForAllPerson()
    # print(personList)
    # print()
    #
    # recordList = getForAllRecord()
    # print(recordList)
    # print()
    #
    # # 单条Person
    # thePerson = personList[0]
    # thPersonnelId = thePerson.personnelId
    #
    # # 单条Person测试
    # record = getForRecordByPersonId(thPersonnelId)
    # print(record)
    # print()
    #
    # time = getForAccessTimeByPersonId(thPersonnelId)
    # print(time)
    # print()
    #
    # address = getForAccessAddressByPersonId(thPersonnelId)
    # print(address)
    # print()

    # device测试
    # print(getForYesterdayDeviceCount())


if __name__ == '__main__':
    testForAllApi()
