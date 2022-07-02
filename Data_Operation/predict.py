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
from data_preproccess import Data_Preprocess , Average_Filter
from sklearn.model_selection import train_test_split

# ========================================全局变量==========================================

device_id = '09'

# 测试txt文件夹路径
test_dir_path = "F:\\ADC_CO2\\项目工程\\数据处理\\test_data\\"+device_id

temp_temp_list   = []
temp_humi_list   = []
temp_verify_list = []
predict_cc_list  = []

# ========================================读取数据==========================================

print("=====================================数据读取=========================================")
# 读取文件夹下每一个子文件中txt路径
# 保存到列表txt_path中
txt_dir_path = opendirtxt(test_dir_path)

# 遍历txt文件路径读取
for file_path in txt_dir_path:
    data_list = openreadtxt(file_path)
    # print(data_list)
    Data_Split(data_list)

temp_temp_list = RetTempList()
temp_humi_list = RetHumiList()
temp_verify_list = RetVerifyList()
# 对采集电压值进行均值滤波
temp_verify_list = Average_Filter(temp_verify_list,10)

print(temp_temp_list)
print(temp_humi_list)
print(temp_verify_list)

print("=====================================数据显示=========================================")
print("显示后四个数据")
print("temp:", temp_temp_list[-5:-1])
print("humi:", temp_humi_list[-5:-1])
print("V", temp_verify_list[-5:-1])

print("=====================================数据数量=========================================")
print("显示温度、湿度、电压和浓度数据个数")
print("temp len:", len(temp_temp_list))
print("humi len:", len(temp_humi_list))
print("V len:", len(temp_verify_list))

# ======================================绘制三维可视化图表========================================

train_model = Polynomial(
                         temp_list = temp_temp_list,      # 温度数据列表
                         verify_list = temp_verify_list,  # 电压数据列表
                         poly_degree = 4                  # 多项式次数
                         )

predict_cc_list = train_model.predict_model(
                                            test_temp_list   = temp_temp_list, # 温度数据列表
                                            test_verify_list = temp_verify_list, # 电压数据列表
                                            load_model_dir   = "F:\\ADC_CO2\\项目工程\\数据处理\\code\\Data_Operation\\save_model\\"+device_id
                                            )
# 取绝对值， 滤去负值
for data in predict_cc_list:
    data = abs(data)

print(max(predict_cc_list))
print(min(predict_cc_list))

# 创建一个图框
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = temp_temp_list
y = temp_verify_list
z = predict_cc_list
print(z)

ax.set_xlabel('Temp(℃)')
ax.set_ylabel('Verify(V)')
ax.set_zlabel('CO2 CC(ppm)')

ax.scatter(x, y, z, c='r',label='Scatter plot of CO2 concentration')

ax.legend()

plt.show()

