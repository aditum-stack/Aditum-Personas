"""
基于设备按天访问热度[DAY访问热度]的一维聚类分析
"""
import random

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import base64
import os
from api import BackRemoteApi

# 保存的临时分析图片的名字
image_path = os.getcwd() + '\\deviceCountClustering.png'

# 聚类中心
clustering = 4

# 1展示图片 0不展示
show = 0


def initDeviceCountData():
    """
    获取T+1的所有DeviceCount数据
    """
    deviceCountList = BackRemoteApi.getForYesterdayDeviceCount()
    return deviceCountList


def initEntitySet(deviceCountList):
    """
    初始化聚类数据集
    :param deviceCountList: 设备按天热度数据
    :return: 一维矩阵 [访问量,访问量...]
    """
    countEntitySet = []
    # 数据集
    for deviceCount in deviceCountList:
        # 当天访问量
        accessCount = deviceCount.accessCount
        countEntity = [accessCount + random.random(), accessCount + random.random()]
        countEntitySet.append(countEntity)
    return countEntitySet


def kmeansClustering(entitySet, n_clusters=3):
    """
    对一维矩阵进行K-means聚类
    """
    # 聚类算法，参数n_clusters=x，聚成x类
    clf = KMeans(n_clusters=n_clusters)
    # 直接对数据进行聚类，聚类不需要进行预测
    y_pred = clf.fit_predict(entitySet)
    return y_pred


def showAndSave(entitySet, y_pred, show=0):
    """
    根据聚类结果展示散点图
    :param entitySet: 一维聚类数据
    :param y_pred: 聚类结果
    :return: 图片
    """
    xData = [n[0] for n in entitySet]
    yData = [n[1] for n in entitySet]
    plt.scatter(xData, yData, c=y_pred, marker='x')
    plt.title("device day count clustering")
    plt.xlabel("day count")
    plt.ylabel("day count")
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
    # print("设备T+1访问热度聚类分析...开始")

    deviceCountList = initDeviceCountData()
    # print(deviceCountList)

    # print("数据获取成功，开始分析...")

    # 初始化数据集
    countEntitySet = initEntitySet(deviceCountList)

    # 聚类分析
    y_pred = kmeansClustering(countEntitySet, clustering)

    # 可视化结果并保存图片
    showAndSave(countEntitySet, y_pred, show=show)

    # print("设备T+1访问热度聚类分析...结束")

    # base64
    base64 = base64img()
    print(base64)
    return base64


# Java runtime invoke
run()
