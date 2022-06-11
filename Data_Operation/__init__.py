# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：__init__.py ，提供对外函数接口
@Author  ：leeqingshui
@Date    ：2022/6/11 18:01 
'''

from Read_txt_data import openreadtxt,opendirtxt
from Data_Analysis import Data_Split,RetTempList,RetHumiList,RetVerifyList,RetCCList

# 测试txt文件夹路径
test_dir_path = "C:\\Users\\lee\\Desktop\\ADC_CO2\\项目工程\\数据处理\\data"

'''
@ 函数功能                 ：读取目标文件夹中所有子文件夹下txt文件中每一行的数据
@ 入口参数 {str}  dir_path ：目标文件夹路径
@ 返回参数 {list} data     ：存放每一行数据的列表
'''
def ReadData(dir_path):
    # 读取文件夹下每一个子文件中txt路径
    # 保存到列表txt_path中
    txt_path = opendirtxt(dir_path)

    # 遍历txt文件路径读取
    for file_path in txt_path:
        data = openreadtxt(file_path)
    return data

if __name__=="__main__":
    data = ReadData(test_dir_path)
    print(data)

