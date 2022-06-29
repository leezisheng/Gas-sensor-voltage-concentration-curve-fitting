# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：Data_Analysis.py
@Author  ：leeqingshui
@Date    ：2022/6/11 18:34 
'''

from Read_txt_data import openreadtxt,opendirtxt

# 测试txt文件夹路径
test_dir_path = "F:\\ADC_CO2\\项目工程\\数据处理\\data\\07"

# 温度列表
temp_list = []
# 湿度列表
humi_list = []
# 电压列表
verify_list = []
# 浓度列表
concentration_list = []

'''
@ 函数功能                  ：将txt文件中数据根据其前缀进行拆分
@ 入口参数 {str}  data_list ：原始数据
@ 返回参数 {bool}           ：操作状态，true操作成功，false操作失败
'''
def Data_Split(data_list):
    operation_status = True

    temp_temp = 0
    temp_humi = 0
    temp_verify = 0
    temp_concentration = 0

    # data和data_list均为列表
    for data in data_list:
        # 将列表中元素提取，提取后data为字符串
        data = data[0]

        # 跳过空格
        if data == " ":
            continue

        if '温度' in data:
            temp_temp = (int(''.join([x for x in data if x.isdigit()])))/1000000
            temp_list.append(temp_temp)

        if '湿度' in data:
            temp_humi = (int(''.join([x for x in data if x.isdigit()])))/1000000
            humi_list.append(temp_humi)

        if 'A' in data:
            temp_verify = (int(''.join([x for x in data if x.isdigit()])))/1
            verify_list.append(temp_verify)

        if 'C' in data:
            temp_concentration = (int(''.join([x for x in data if x.isdigit()])))*100
            concentration_list.append(temp_concentration)

    return operation_status

'''
@ 函数功能                  ：返回存放温度值的列表
@ 返回参数 {list} temp_list ：存放温度值的列表
'''
def RetTempList():
    return temp_list

'''
@ 函数功能                  ：返回存放湿度值的列表
@ 返回参数 {list} humi_list ：存放湿度值的列表
'''
def RetHumiList():
    return humi_list

'''
@ 函数功能                    ：返回存放ADC采集电压值的列表
@ 返回参数 {list} verify_list ：存放电压值的列表
'''
def RetVerifyList():
    return verify_list

'''
@ 函数功能                           ：返回存放CO2浓度值的列表
@ 返回参数 {list} concentration_list ：存放CO2浓度值的列表
'''
def RetCCList():
    return concentration_list

if __name__=="__main__":

    # 为0时测试读取单个txt文件中数据；
    # 为1时测试读取文件夹下多个txt文件中数据。
    flag = 1

    if flag == 0:
        # 读取txt文件中数据
        data_list = openreadtxt(test_txt_path)
        if(Data_Split(data_list)!=False):
            print(RetTempList())
            print(RetHumiList())
            print(RetVerifyList())
            print(RetCCList())
    else:
        temp_temp_list   = []
        temp_humi_list   = []
        temp_verify_list = []
        temp_cc_list     = []

        # 读取文件夹下每一个子文件中txt路径
        # 保存到列表txt_path中
        txt_dir_path = opendirtxt(test_dir_path)

        # 遍历txt文件路径读取
        for file_path in txt_dir_path:
            data_list = openreadtxt(file_path)
            Data_Split(data_list)

        temp_temp_list   = RetTempList()
        temp_humi_list   = RetHumiList()
        temp_verify_list = RetVerifyList()
        temp_cc_list     = RetCCList()

        print("=====================================数据显示=========================================")
        print("显示后四个数据")
        print("temp:",temp_temp_list[-5:-1])
        print("humi:",temp_humi_list[-5:-1])
        print("V",temp_verify_list[-5:-1])
        print("cc:",temp_cc_list[-5:-1])

        print("=====================================数据数量=========================================")
        print("显示温度、湿度、电压和浓度数据个数")
        print("temp len:",len(temp_temp_list))
        print("humi len:", len(temp_humi_list))
        print("V len:", len(temp_verify_list))
        print("cc len:", len(temp_cc_list))






