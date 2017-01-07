# -*- coding: utf-8 -*-
from math import *


# 将二维方向系数按0-180，0-359重新排序
def resort(x,antenna_flagx):
    d_f_copy1 = [[0 for x in range(360)] for x in range(181)]  # 对垂直方向系数重新排序时做中间变量
    d_f_copy2 = [[0 for x in range(360)] for x in range(181)]  # 对水平方向系数重新排序时做中间变量
    d_f_copy3 = [[0 for x in range(360)] for x in range(181)]  # 对三扇区天线水平方向系数重新排序
    ## 对三扇区天线水平方向系数重新排序
    if antenna_flagx==1: ## 120度天线
        for j in range(120):
            for i in range(181):
                d_f_copy3[i][j] = x[i][j+120] ## 右偏扇区赋值
        for j in range(120,240):
            for i in range(181):
                d_f_copy3[i][j] = x[i][j]  ## 中间偏扇区赋值
        for j in range(240, 360):
            for i in range(181):
                d_f_copy3[i][j] = x[i][j-120]  ## 左偏扇区赋值
    elif antenna_flagx==2: ## 全向天线
        d_f_copy3=x[:][:]
    # 对垂直方向系数重新排序，由-90~90转变为90~-90
    for i in range(181):
        for j in range(360):
            d_f_copy1[i][j] = d_f_copy3[180 - i][j]
    # 对水平方向系数重新排序，由-179~180转变为0到359
    j = 0
    while j <= 180:
        for i in range(181):
            d_f_copy2[i][j] = d_f_copy1[i][j + 179]
        j += 1
    j = 181
    while j <= 359:
        for i in range(181):
            d_f_copy2[i][j] = d_f_copy1[i][j - 181]
        j += 1
    return d_f_copy2
