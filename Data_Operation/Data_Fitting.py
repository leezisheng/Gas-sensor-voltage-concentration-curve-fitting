# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：Data_Fitting.py 数据曲线拟合
@Author  ：leeqingshui
@Date    ：2022/6/12 17:31 
'''

import numpy as np

from Read_txt_data import openreadtxt,opendirtxt
from Data_Analysis import Data_Split,RetTempList,RetHumiList,RetVerifyList,RetCCList
import matplotlib.pyplot as plt

# 测试txt文件夹路径
test_dir_path = "C:\\Users\\lee\\Desktop\\ADC_CO2\\项目工程\\数据处理\\data\\06"






if __name__=="__main__":

    temp_temp_list = []
    temp_humi_list = []
    temp_verify_list = []
    temp_cc_list = []

    # 读取文件夹下每一个子文件中txt路径
    # 保存到列表txt_path中
    txt_dir_path = opendirtxt(test_dir_path)

    # 遍历txt文件路径读取
    for file_path in txt_dir_path:
        data_list = openreadtxt(file_path)
        Data_Split(data_list)

    temp_temp_list = RetTempList()
    temp_humi_list = RetHumiList()
    temp_verify_list = RetVerifyList()
    temp_cc_list = RetCCList()

    print("=====================================数据显示=========================================")
    print("显示后四个数据")
    print("temp:", temp_temp_list[-5:-1])
    print("humi:", temp_humi_list[-5:-1])
    print("V", temp_verify_list[-5:-1])
    print("cc:", temp_cc_list[-5:-1])

    print("=====================================数据数量=========================================")
    print("显示温度、湿度、电压和浓度数据个数")
    print("temp len:", len(temp_temp_list))
    print("humi len:", len(temp_humi_list))
    print("V len:", len(temp_verify_list))
    print("cc len:", len(temp_cc_list))

