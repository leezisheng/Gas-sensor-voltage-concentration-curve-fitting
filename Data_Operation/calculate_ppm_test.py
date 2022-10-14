# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File    ：calculate_ppm_test.py
@Author  ：leeqingshui
@Date    ：2022/8/16 12:44 
'''

x_coef = 2753
y_coef = -3568

x2_coef = 13
xy_coef = -8.45
y2_coef = 5.06

intercept = 613997

x = 28
y = 277

ppm = (x*x_coef + y*y_coef )+\
      (x*x*x2_coef + y*y*y2_coef + x*y*xy_coef ) +\
      intercept
print(ppm)








