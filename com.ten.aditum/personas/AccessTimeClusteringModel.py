"""
基于访问时间AccessTime[最早访问时间,最晚访问时间]的聚类分析
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import base64
import os
from util import TimeUtil
import BackRemoteApi

# 保存的临时分析图片的名字
image_path = os.getcwd() + '\\accessTimeClustering.png'


def initPersonData():
    """
    获取person数据
    """
    personList = BackRemoteApi.getForAllPerson()
    return personList


def initAccessTimeData(personList):
    """
    获取accessTime数据
    """
    personAccessTimeList = []
    for person in personList:
        personAccessTime = BackRemoteApi.getForAccessTimeByPersonId(person.personnelId)
        if personAccessTime is not None:
            personAccessTimeList.append(personAccessTime)
    return personAccessTimeList


def initEntitySet(personAccessTimeList):
    """
    初始化聚类数据集
    :param personAccessTimeList: 用户时间行为数据
    :return: 二维矩阵 [[],[]...]
    """
    timeEntitySet = []
    # 数据集
    for personAccessTime in personAccessTimeList:
        # 平均最早访问时间
        eTime = personAccessTime.averageEarliestAccessTime
        # 平均最晚访问时间
        lTime = personAccessTime.averageLatestAccessTime
        # 过滤早晚相同的数据
        if eTime == lTime:
            continue
        # 时分秒转换成秒
        es = TimeUtil.timeToS(eTime)
        ls = TimeUtil.timeToS(lTime)
        # 添加数据集
        timeEntity = [es, ls]
        timeEntitySet.append(timeEntity)
    return timeEntitySet


def kmeansClustering(entitySet, n_clusters=3):
    """
    对二维矩阵进行K-means聚类
    """
    # 聚类算法，参数n_clusters=x，聚成x类
    clf = KMeans(n_clusters=n_clusters)
    # 直接对数据进行聚类，聚类不需要进行预测
    y_pred = clf.fit_predict(entitySet)
    return y_pred


def showAndSave(entitySet, y_pred, show=0):
    """
    根据聚类结果展示散点图
    :param entitySet: 聚类数据
    :param y_pred: 聚类结果
    :return: 图片
    """
    xData = [n[0] for n in entitySet]
    yData = [n[1] for n in entitySet]
    plt.scatter(xData, yData, c=y_pred, marker='x')
    plt.title("user access time clustering")
    plt.xlabel("Earliest")
    plt.ylabel("Latest")
    plt.savefig(image_path)
    # 图片展示
    if show != 0:
        plt.show()


def base64img():
    """
    返回刚刚保存的图片的base64字符串
    :return: base64
    """
    with open(image_path, "rb") as f:
        # b64encode是编码，b64decode是解码
        base64_data = base64.b64encode(f.read())
        # base64.b64decode(base64data)
        # print(base64_data)
        return base64_data


def run():
    """
    执行脚本，并返回图片的base64字符串
    :return: base64图片字符串
    """
    # print("用户时间行为偏好聚类分析...开始")

    # Person集合
    personList = initPersonData()
    # print(personList)

    # PersonAccessTime集合
    personAccessTimeList = initAccessTimeData(personList=personList)
    # print(personAccessTimeList)

    # print("数据获取成功，开始分析...")

    # 初始化数据集
    timeEntitySet = initEntitySet(personAccessTimeList)

    # 聚类分析
    y_pred = kmeansClustering(timeEntitySet, 3)

    # 可视化结果并保存图片
    showAndSave(timeEntitySet, y_pred, show=0)

    # print("用户时间行为偏好聚类分析...结束")

    # base64
    base64 = base64img()
    print(base64)
    return base64


# Java runtime invoke
run()
