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

    '''
        @ 函数作用                    ：初始化
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



