"""
接口服务工具，包含了从Aditum-Back服务中获取接口数据的各种方法
"""

import json
import requests

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
基础数据接口
"""
communityUrl = "http://localhost:9006/community"
deviceUrl = "http://localhost:9006/device"
personUrl = "http://localhost:9006/person"
recordUrl = "http://localhost:9006/record"

"""
统计分析数据接口
"""
accessPersonUrl = "http://localhost:9006/access/person"
accessDeviceUrl = "http://localhost:9006/access/device"

"""
HTTP参数
"""
headers = {'content-type': 'application/json'}


# 获取全量数据

def getForAllPerson():
    """
    获取所有person

    :return: person[]
    """
    personJsonList = requests.get(personUrl, params={}, headers=headers).json().get("data")
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
    accessAddress = AccessAddress(accessAddressJson)
    return accessAddress


def testForAllApi():
    """
    接口测试
    """
    # 全量测试
    personList = getForAllPerson()
    print(personList)
    print()

    recordList = getForAllRecord()
    print(recordList)
    print()

    # 单条Person
    thePerson = personList[0]
    thPersonnelId = thePerson.personnelId

    # 单条Person测试
    record = getForRecordByPersonId(thPersonnelId)
    print(record)
    print()

    time = getForAccessTimeByPersonId(thPersonnelId)
    print(time)
    print()

    address = getForAccessAddressByPersonId(thPersonnelId)
    print(address)
    print()


if __name__ == '__main__':
    testForAllApi()

    # personList = getForAllPerson()
    # recordList = getForAllRecord()
    #
    # for person in personList:
    #     # print(person)
    #
    #     personEntity = Person(person)
    #
    #     recordByPersonId = getForRecordByPersonId(personEntity.personnelId)
    #
    #     for record in recordByPersonId:
    #         print(record)

    # print(getForAllPerson())
    # print(json.loads(getForPerson(requestData).text).get("data")[0])
