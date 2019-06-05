# Aditum Personas

> Personas Server for Aditum. 基于机器学习算法建立用户画像. 

## 技术栈

K-means聚类分析

## 运行流程

通过HTTP从Back服务获取数据，基于K-means算法进行聚类分析，将分析结果对应的标签通过API发送到Back进行用户画像的修改

## 结果展示

![用户访问频率聚类分析](com.ten.aditum/personas/accessFrequencyClustering.png)

![用户时间行为偏好聚类分析](com.ten.aditum/personas/accessTimeClustering.png)

![用户使用天数聚类分析](com.ten.aditum/personas/deviceCountClustering.png)