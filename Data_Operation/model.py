# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：model.py , 曲线拟合算法模型
@Author  ：leeqingshui
@Date    ：2022/6/18 21:22 
'''

import numpy as np
import sklearn.pipeline as pl
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pickle
from sklearn.metrics import mean_squared_error


# ======================================多元多项式拟合算法=====================================================
# 使用多项式函数来拟合生成的数据，然后使用均方误差作为误差函数对拟合出的多项式进行评估
# 
# （1）原理：
#     拟合数据的目的即为最小化误差函数，因为误差函数是多项式系数W的二次函数，所以存在唯一最小值，且在导数为零处取得
#     可以通过矩阵运算或者梯度下降方法得到系数矩阵W
# 
# （2）方法：通过Python中的sklearn函数库的PolynomialFeatures进行函数拟合
#      这里使用线性模型来拟合非线性数据，即将每一个特征的幂次方添加为一个新特征，然后在此扩展数据集上进行训练一个
#      线性模型，该技术就是多项式回归算法      
# 
# （3）评估：使用均方误差MSE作为模型好坏评价标准，其值越小越好
# ===========================================================================================================
class Polynomial:

    '''
    @ 函数作用                    ：初始化
    @ 输入参数 {list} temp_list   : 温度列表
    @ 输入参数 {list} verify_list : 电压列表
    @ 输入参数 {list} cc_list     : 浓度列表
    @ 输入参数 {int}  poly_degree : 拟合曲线系数
    '''
    def __init__(self, temp_list ,  verify_list , cc_list ,  poly_model = '', poly_degree = 4 ):

        # 温度列表
        self.temp_list      = temp_list
        # 电压列表
        self.verify_list    = verify_list
        # 浓度列表
        self.cc_list        = cc_list
        # 拟合曲线系数
        self.poly_degree    = poly_degree
        # 模型
        self.poly_model    = poly_model

    '''
    @ 函数作用                      ：模型训练
    @ 输入参数 {str} save_model_dir : 模型保存位置
    @ 返回参数 {pkl} poly_model     : 训练好的模型
    '''
    def train_model(self , save_model_dir = ''):

        print("==============================================开始训练==============================================")

        # 将温度列表、电压列表合并为一个自变量列表
        # x_list = list(zip(self.temp_list,self.verify_list))
        x_list = [list(t) for t in zip(self.temp_list, self.verify_list)]

        # 因变量列表赋值
        y_list = self.cc_list

        # 构造多项式回归特征扩展器
        poly_reg =PolynomialFeatures(self.poly_degree)
        x_poly = poly_reg.fit_transform(x_list)

        # 构造线性回归模型训练对象
        self.poly_model = LinearRegression()   # 线性回归器

        # 训练拟合曲线模型
        self.poly_model.fit(x_poly , y_list)

        print("==============================================训练结果==============================================")

        print("偏置项："+str(self.poly_model.intercept_))
        print("系数项："+str(self.poly_model.coef_))

        print("==============================================保存模型==============================================")

        try :
            output = open(save_model_dir+'poly_reg_model.pkl', 'wb')
            pickle.dump(self.poly_model, output)
            print("保存模型成功，保存位置："+save_model_dir+'poly_reg_model.pkl')
        except:
            print("保存模型失败")
        
        return self.poly_model
    
    '''
    @ 函数作用                         : 模型加载和模型预测
    @ 输入参数 {list} test_temp_list   : 测试温度列表
    @ 输入参数 {list} test_verify_list : 测试电压列表
    @ 输入参数 {pkl}  poly_model       : 预测模型，从本文件中读入，默认为''
    @ 输入参数 {str}  predict_cc_list  : 预测模型保存路径，从其他保存的文件中读入，默认为''
    @ 返回参数 {list} predict_cc_list  : 预测浓度列表
    '''
    def predict_model(self , test_temp_list, test_verify_list, load_model_dir = ''):
        # 预测浓度列表
        predict_cc_list = []

        # 临时变量，二维自变量列表
        temp_x_list = [list(t) for t in zip(test_temp_list, test_verify_list)]
        print(test_temp_list,test_verify_list)

        # 构造多项式回归特征扩展器
        poly_reg =PolynomialFeatures(self.poly_degree)
        x_poly = poly_reg.fit_transform(temp_x_list)

        if load_model_dir != '':
            print("==========================================加载模型==========================================")
            try:
                poly_model_file = open(str(load_model_dir)+'\\'+'poly_reg_model.pkl', 'rb')
                self.poly_model = pickle.load(poly_model_file)
                print("==========================================加载模型成功==========================================")
                predict_cc_list = self.poly_model.predict(x_poly)
            except:
                print("==========================================加载模型失败==========================================")

        else:
            print("==========================================使用文件模型==========================================")
            try:
                predict_cc_list = self.poly_model.predict(x_poly)
            except:
                print("==========================================文件模型错误==========================================")

        return predict_cc_list
    
    '''
    @ 函数作用                          : 评估模型: 使用MSE作为评价标准
    @ 输入参数 {list}  test_cc_list     : 实际浓度列表
    @ 输入参数 {list}  predict_cc_list  : 预测浓度列表
    @ 返回参数 {float} mse              : 均方误差
    '''
    def evaluate_model(self , test_cc_list , predict_cc_list):
        # 测试数据浓度列表
        cc_test_list = test_cc_list
        # 预测数据浓度列表
        cc_predict_list = predict_cc_list

        print('MSE为:',mean_squared_error(cc_test_list,cc_predict_list))
        mse = mean_squared_error(cc_test_list,cc_predict_list)
        return mse

