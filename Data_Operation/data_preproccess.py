# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：data_preproccess.py , 包括数据预处理方法
@Author  ：leeqingshui
@Date    ：2022/6/22 6:07 
'''

import numpy as np
import sklearn.preprocessing as sp

# =============================================数据预处理=====================================================
# （1）目的：
#       1.去除无效数据、不规范数据、错误数据
#       2.补齐缺失值
#       3.对数据范围、量纲、格式、类型进行统一化处理，更容易进行后续计算
#
# （2）方法：
#      标准化：对不同特征维度的伸缩变换使其不同度量之间的特征具有可比性 ，不改变原始数据的分布，保持各个特征维度对目标函数的影响权重
#      归一化：将数据集中某一列数值特征的值缩放到0-1区间内 ， 改变原始数据的分布，使得各个特征维度对目标函数的影响权重归于一致；
#      正则化：将数据集中某一个样本缩放成单位标准 ， 主要应用于文本分类和聚类中
#
# ===========================================================================================================
class Data_Preprocess:

    '''
        @ 函数作用                    ：初始化
        @ 输入参数 {list} temp_list   : 温度列表
        @ 输入参数 {list} verify_list : 电压列表
        @ 输入参数 {list} cc_list     : 浓度列表
    '''
    def __init__(self, temp_list, verify_list, cc_list):
        # 温度列表
        self.temp_list   = np.array(temp_list).reshape(1,-1)
        # 电压列表
        self.verify_list = np.array(verify_list).reshape(1,-1)
        # 浓度列表
        self.cc_list     = np.array(cc_list).reshape(1,-1)

        # 标准化器
        self.temp_scaler   = sp.MinMaxScaler()
        self.verify_scaler = sp.MinMaxScaler()
        self.cc_scaler     = sp.MinMaxScaler()

    '''
        @ 函数作用                    ：正则化, 将缩放单个样本至单位范数的过程
        @ 输入参数 {list} temp_list   : 温度列表
        @ 输入参数 {list} verify_list : 电压列表
        @ 输入参数 {list} cc_list     : 浓度列表
        @ 输入参数 {list} norm        : 正则化范数
        @                               'l1': l1范数，除以向量中各元素绝对值之和 
        @                               'l2': l2范数，除以向量中各元素平方之和 
        @ 输出参数 {list}             : 正则化后数据列表
    '''
    def data_normalization(self , norm = 'l1'):

        norm_temp_list   = sp.normalize(self.temp_list, norm = norm)
        norm_verify_list = sp.normalize(self.verify_list, norm = norm)
        norm_cc_list     = sp.normalize(self.cc_list, norm = norm)

        return norm_temp_list , norm_verify_list , norm_cc_list

    '''
        @ 函数作用                    ：标准化 ，将特征值缩放到给定的最小值和最大值之间，通常介于零和一之间
        @                              包括对特征极小标准偏差的稳健性以及在稀疏数据中保留零元素
        @                              对不同特征维度的伸缩变换使其不同度量之间的特征具有可比性；
        @                              不改变原始数据的分布，保持各个特征维度对目标函数的影响权重；
        @                              对目标函数的影响体现在几何分布上。
        @ 输入参数 {list} temp_list   : 温度列表
        @ 输入参数 {list} verify_list : 电压列表
        @ 输入参数 {list} cc_list     : 浓度列表
        @ 输入参数 {list} scaler      : 标准化器
        @ 输出参数 {list}             : 标准化后数据列表
    '''
    def data_standardization(self):

        # 标准化温度列表
        self.temp_scaler.fit(self.temp_list)
        standard_temp_list = self.temp_scaler.transform(self.temp_list)

        # 标准化电压列表
        self.verify_scaler.fit(self.verify_list)
        standard_verify_list = self.verify_scaler.transform(self.verify_list)

        # 标准化浓度列表
        self.cc_scaler.fit(self.cc_list)
        standard_cc_list = self.cc_scaler.transform(self.cc_list)

        return standard_temp_list , standard_verify_list , standard_cc_list

'''
        @ 函数作用                        ：均值滤波
        @ 输入参数 {list} x               : 初始预测浓度列表
        @ 输入参数 {list} filt_length     : 均值滤波宽度
        @ 输出参数 {list} cc_list         : 滤波后列表
'''
def Average_Filter(x, filt_length):
    N = len(x)
    res = []
    for i in range(N):
        if i <= filt_length // 2 or i >= N - (filt_length // 2):
            temp = x[i]
        else:
            sum = 0
            for j in range(filt_length):
                sum += x[i - filt_length // 2 + j]
            temp = sum * 1.0 / filt_length
        res.append(temp)
    return res









