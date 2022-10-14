# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：Read_txt_data.py ， 读取文件夹下txt文件中数据
@Author  ：leeqingshui
@Date    ：2022/6/11 17:19 
'''

import os
import chardet

# 测试txt文件夹路径
test_dir_path = "F:\\ADC_CO2\\项目工程\\数据处理\\data\\07"

'''
@ 函数功能                  ：读取txt文件中每一行的数据
@ 入口参数 {str}  file_name ：txt文件路径
@ 返回参数 {list} data      ：存放每一行数据的列表
'''
def openreadtxt(file_name):
    data = []
    # 默认编码方式为utf-8
    encoding = 'utf-8'

    # 二进制方式读取，获取字节数据，检测类型
    with open(file_name, 'rb') as f:
        encoding = chardet.detect(f.read())['encoding']

    # 打开文件
    file = open(file_name,'r',encoding = encoding)
    # 读取所有行
    file_data = file.readlines()
    for row in file_data:
        # 去掉列表中每一个元素的换行符
        row = row.strip('\n')
        # 按‘，’切分每行的数据
        tmp_list = row.split(' ')
        # 将每行数据插入data列表中
        data.append(tmp_list)
    return data

'''
@ 函数功能                  ：读取根文件夹下面每一个文件夹中的txt文件
@ 入口参数 {str}  dir_path  ：文件夹路径
@ 返回参数 {list} txt_path  ：存放每一个txt文件路径的列表
'''
def opendirtxt(dir_path):
    txt_path = []

    # 遍历文件夹
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for file in filenames:
            if os.path.splitext(file)[1] == '.txt':
                txt_path.append(os.path.join(dirpath,file))
    return txt_path

if __name__=="__main__":
    # 读取文件夹下每一个子文件中txt路径
    # 保存到列表txt_path中
    txt_path = opendirtxt(test_dir_path)

    # 遍历txt文件路径读取
    for file_path in txt_path:
        data = openreadtxt(file_path)
        print(data)


