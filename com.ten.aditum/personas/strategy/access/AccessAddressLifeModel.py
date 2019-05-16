"""
基于访问地点AccessAddress中的家庭住址信息 的 用户生活模型 画像分析
"""

import BackRemoteApi
from label.BaseTimeLabel import BaseTimeLabel
from label.BusyTimeLabel import BusyTimeLabel
from label.CommonTimeLabel import CommonTimeLabel
from label.EasyTimeLabel import EasyTimeLabel


def initPersonData():
    personList = BackRemoteApi.getForAllPerson()
    return personList


def initAccessTimeData(personList):
    personAccessTimeList = []
    for person in personList:
        personAccessTime = BackRemoteApi.getForAccessTimeByPersonId(person.personnelId)
        if personAccessTime is not None:
            personAccessTimeList.append(personAccessTime)
    return personAccessTimeList


if __name__ == '__main__':
    # Person集合
    personList = initPersonData()
    print(personList)

    # PersonAccessTime集合
    # personAccessTimeList = initAccessTimeData(personList=personList)
    # print(personAccessTimeList)

    # 标签库
    lableList = []
    lableList.append(EasyTimeLabel())
    lableList.append(CommonTimeLabel())
    lableList.append(BusyTimeLabel())
    print(lableList)

    print("数据获取成功，开始分析...")
