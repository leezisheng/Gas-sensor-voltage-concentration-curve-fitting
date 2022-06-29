# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：predict.py 模型预测
@Author  ：leeqingshui
@Date    ：2022/6/29 20:06 
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from Read_txt_data import openreadtxt,opendirtxt
from Data_Analysis import Data_Split,RetTempList,RetHumiList,RetVerifyList,RetCCList
from model import Polynomial
from data_preproccess import Data_Preprocess
from sklearn.model_selection import train_test_split

# ========================================全局变量==========================================

device_id = '09'

# 测试txt文件夹路径
test_dir_path = "F:\\ADC_CO2\\项目工程\\数据处理\\data\\"+device_id

temp_temp_list = []
temp_humi_list = []
temp_verify_list = []
temp_cc_list = []

# ========================================读取数据==========================================










