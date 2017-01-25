# -*- coding: utf-8 -*-
def resort120(x,antenna_flagx):
    d_f_copy3 = [[0 for x in range(360)] for x in range(181)]  # 对三扇区天线水平方向系数重新排序
    ## 对三扇区天线水平方向系数重新排序
    if antenna_flagx == 1:  ## 120度天线
        for j in range(120):
            for i in range(181):
                d_f_copy3[i][j] = x[i][j + 120]  ## 右偏扇区赋值
        for j in range(120, 240):
            for i in range(181):
                d_f_copy3[i][j] = x[i][j]  ## 中间偏扇区赋值
        for j in range(240, 360):
            for i in range(181):
                d_f_copy3[i][j] = x[i][j - 120]  ## 左偏扇区赋值
    elif antenna_flagx == 2:  ## 全向天线
        d_f_copy3 = x[:][:]
    return d_f_copy3

# 借用数字电视方向图简易改至空间站天线方向图
def resort_satellite_dir_m(x):
    d_f_copy = [[0 for x in range(360)] for x in range(91)]
    for i in range(91):
        for j in range(360):
            d_f_copy[i][j]=x[i+90][j]  # 取数字电视方向图垂直方向角的主瓣的一半赋值给偏轴角
    return d_f_copy
