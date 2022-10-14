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

# ========================================全局变量==========================================

device_id = '08'

# 测试txt文件夹路径
test_dir_path = "F:\\ADC_CO2\\项目工程\\数据处理\\test_data_02\\"+device_id
# 测试得到实际值
temp_temp_list   = []
temp_humi_list   = []
temp_verify_list = []
# 预测值
predict_cc_list  = []
# 实际值
true_cc_list = []

# ========================================读取数据==========================================

print("=====================================数据读取=========================================")
# 读取文件夹下每一个子文件中txt路径
# 保存到列表txt_path中
txt_dir_path = opendirtxt(test_dir_path)

# 遍历txt文件路径读取
for file_path in txt_dir_path:
    # 文件命名原则 : test-传感器编号-测定浓度（ppm）//10000-温度
    # 示例 : F:\ADC_CO2\项目工程\数据处理\test_data\07\test-7-1-25.txt
    # 含义 ： 七号传感器在10000ppm、25摄氏度时输出数据
    data_list = openreadtxt(file_path)
    Data_Split(data_list)

    # 数据长度
    list_len = int(len(data_list)/4)

    if '-1-' in file_path :
        temp_true_cc_list = [10000]*list_len
        true_cc_list.extend(temp_true_cc_list)
        print(' file_path : ' , file_path)
        print(' length of temp_true_cc_list : ' , list_len)

    elif '-2-' in file_path :
        temp_true_cc_list = [20000]*list_len
        true_cc_list.extend(temp_true_cc_list)
        print(' file_path : ' , file_path)
        print(' length of temp_true_cc_list : ' , list_len)

    elif '-2.5-' in file_path :
        temp_true_cc_list = [25000]*list_len
        true_cc_list.extend(temp_true_cc_list)
        print(' file_path : ' , file_path)
        print(' length of temp_true_cc_list : ' , list_len)

    elif '-3-' in file_path :
        temp_true_cc_list = [30000]*list_len
        true_cc_list.extend(temp_true_cc_list)
        print(' file_path : ' , file_path)
        print(' length of temp_true_cc_list : ' , list_len)

    elif '-4-' in file_path :
        temp_true_cc_list = [40000]*list_len
        true_cc_list.extend(temp_true_cc_list)
        print(' file_path : ' , file_path)
        print(' length of temp_true_cc_list : ' , list_len)

    elif '-5-' in file_path :
        temp_true_cc_list = [50000]*list_len
        true_cc_list.extend(temp_true_cc_list)
        print(' file_path : ' , file_path)
        print(' length of temp_true_cc_list : ' , list_len)

# print(true_cc_list)
print("true cc len :",len(true_cc_list))

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
                         poly_degree = 2                  # 多项式次数
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

x  = temp_temp_list
y  = temp_verify_list
z  = predict_cc_list
zz = true_cc_list

# print(z)
print(len(z))

ax.set_xlabel('Temp(℃)')
ax.set_ylabel('Verify(V)')
ax.set_zlabel('CO2 CC(ppm)')

ax.scatter(x, y, z,  c='r',label='scatter plot of predict CO2 concentration')
ax.scatter(x, y, zz, c='b',label='Scatter plot of true CO2 concentration')

ax.legend()

plt.show()

# ======================================评估模型========================================
# 计算MSE
MSE , RMSE = train_model.evaluate_model(true_cc_list , predict_cc_list)

