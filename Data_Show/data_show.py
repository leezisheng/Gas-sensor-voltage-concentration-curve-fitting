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

'''
@ 函数功能                          ：对比预测点和实际浓度点，绘制散点图
@ 入口参数 {list}  temp_temp_list   ：自变量，存放温度数据的列表
@ 入口参数 {list}  temp_verify_list ：自变量，存放ADC电压数据的列表
@ 入口参数 {list}  temp_cc_list     ：因变量，存放实际CO2浓度数据的列表
@ 入口参数 {list}  predict_cc_list  ：因变量，存放预测CO2浓度数据的列表
@ 返回参数 {bool}  operation_status ：操作状态，如果成功返回True,否则返回False
'''
def show_scatter_contrast(temp_temp_list,temp_verify_list,temp_cc_list,predict_cc_list):

    operation_status = True

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    x = temp_temp_list
    y = temp_verify_list
    z = temp_cc_list
    p = predict_cc_list

    ax.set_xlabel('Temp(℃)')
    ax.set_ylabel('Verify(MV)')
    ax.set_zlabel('CO2 CC(ppm)')

    ax.scatter(x, y, z, c='r', label='Scatter plot of true CO2 concentration')
    ax.scatter(x, y, p, c='b', label='Scatter plot of predict CO2 concentration')

    ax.legend()
    plt.show()

    return operation_status

'''
@ 函数功能                          ：显示预测曲线图和实际数据散点图
@ 入口参数 {list}  temp_temp_list   ：自变量，存放温度数据的列表
@ 入口参数 {list}  temp_verify_list ：自变量，存放ADC电压数据的列表
@ 入口参数 {list}  temp_cc_list     ：因变量，存放实际CO2浓度数据的列表
@ 入口参数 {list}  x_temp_list      ：曲线温度范围
@ 入口参数 {list}  y_verify_list    ：曲线电压范围
@ 入口参数 {list}  predict_cc_list  ：预测曲线
@ 返回参数 {bool}  operation_status ：操作状态，如果成功返回True,否则返回False
'''
def show_predict_plot(temp_temp_list, temp_verify_list, temp_cc_list, predict_cc_list, x_temp_list = np.linspace(0, 40, 1000), y_verify_list = np.linspace(285, 320, 1000)):

    operation_status = True

    # 创建一个图框
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    x = temp_temp_list
    y = temp_verify_list
    z = temp_cc_list

    ax.set_xlabel('Temp(℃)')
    ax.set_ylabel('Verify(MV)')
    ax.set_zlabel('CO2 CC(ppm)')

    ax.scatter(x, y, z, c='r', label='Scatter plot of true CO2 concentration')

    x_plot = x_temp_list
    y_plot = y_verify_list
    z_plot = predict_cc_list

    ax.plot(x_plot, y_plot, z_plot, label='graph plot of predict CO2 concentration')

    ax.legend()
    plt.show()

    return operation_status

