# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：data_show.py ， 展示数据
@Author  ：leeqingshui
@Date    ：2022/6/18 20:51 
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

'''
@ 函数功能                          ：绘出三维可视化散点图
@ 入口参数 {list}  temp_temp_list   ：自变量，存放温度数据的列表
@ 入口参数 {list}  temp_verify_list ：自变量，存放ADC电压数据的列表
@ 入口参数 {list}  temp_cc_list     ：因变量，存放CO2浓度数据的列表
@ 返回参数 {bool}  operation_status ：操作状态，如果成功返回True,否则返回False
'''
def show_scatter(temp_temp_list,temp_verify_list,temp_cc_list):

    operation_status = True

    # 创建一个图框
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    x = temp_temp_list
    y = temp_verify_list
    z = temp_cc_list

    ax.set_xlabel('Temp(℃)')
    ax.set_ylabel('Verify(V)')
    ax.set_zlabel('CO2 CC(ppm)')

    ax.scatter(x, y, z, c='r', label='Scatter plot of CO2 concentration')
    ax.legend()
    plt.show()

    return operation_status



