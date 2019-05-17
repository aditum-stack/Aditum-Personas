import numpy as np


def distance1(vecA, vecB):
    """
    一维向量欧氏距离

    :return: dist
    """
    return np.sqrt(np.power(vecA[0] - vecB[0], 2))


def distance2(vecA, vecB):
    """
    二维向量欧氏距离

    :return: dist
    """
    return np.sqrt(np.power(vecA[0] - vecB[0], 2) + np.power(vecA[1] - vecB[1], 2))


def distance3(vecA, vecB):
    """
    三维向量欧氏距离

    :return: dist
    """
    return np.sqrt(np.power(vecA[0] - vecB[0], 2) + np.power(vecA[1] - vecB[1], 2) + np.power(vecA[2] - vecB[2], 2))
