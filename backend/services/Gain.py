# -*- coding: utf-8 -*-
from math import *

# 将弧度制转化为角度制
def radian_convert_angle(radian):  ## radian表示输入的弧度制角度
    return (radian * 180 / pi)


## 将初始角度转化为-179--180的整数
def convert_int(initial_angle):  ## initial_angle为初始角度
    if (initial_angle > -180) and (initial_angle < -179) == True:  ## 预先给无法判断的角度赋值
        c = -179
    else:
        i = -179
        while i <= 180:
            if abs(i - initial_angle) <= 0.5:  ## 四舍五入判断
                b = i
                if abs(b - initial_angle) == 0.5:  ## 中间值取进位
                    c = b + 1
                else:
                    c = b
                break  ## 退出循环
            i += 1
    return c  ## 返回整数角度


# 由节点坐标计算节点、雷达的水平方向角（结果为角度制，-179~180）
def calcu_x_direction_angle(x, y):  # x、y代表节点的横纵坐标
    if x > 0:
        if y >= 0:
            angr = atan(y / x)  ## angr为雷达水平方向角
            angn = -pi + atan(y / x)  ## angn为基站水平方向角
        else:
            angr = atan(y / x)
            angn = atan(y / x) + pi
    elif x == 0:
        if y > 0:
            angr = pi / 2
            angn = -pi / 2
        elif y < 0:
            angr = -pi / 2
            angn = pi / 2
    elif x < 0:
        if y >= 0:
            angr = atan(y / x) + pi
            angn = atan(y / x)
        else:
            angr = -pi + atan(y / x)
            angn = atan(y / x)
    angr = radian_convert_angle(angr)  # 弧度制转为角度制
    angn = radian_convert_angle(angn)
    angr = convert_int(angr)  # 角度整数化
    angn = convert_int(angn)
    return angr, angn


# 由节点到雷达的距离、节点高度、雷达高度计算节点、雷达的垂直方向角（结果为角度制，-90~90）
def calcu_y_direction_angle(d, height_nodexx, height_radarxx,
                            elevation):  # d、height_node、height_radar分别代表距离、节点高度、雷达高度、雷达仰角

    height_node = height_nodexx / 1000  # m转化为km
    height_radar = height_radarxx / 1000

    if height_node > height_radar:
        angr = atan((height_node - height_radar) / d)
        angn = -angr

    elif height_node == height_radar:
        angr = 0
        angn = 0

    elif height_node < height_radar:
        angn = atan((height_radar - height_node) / d)
        angr = -angn
    angr = radian_convert_angle(angr)  # 弧度制转为角度制
    angn = radian_convert_angle(angn)
    angr = convert_int(angr)  # 角度整数化
    angn = convert_int(angn)
    angr -= elevation  # 加入天线仰角的计算
    return angr, angn  ## angr为雷达垂直方向角,angn为基站垂直方向角


# 查表得到对应lte二维方向角的二维方向系数
def lte_calcu_direction_factor(x_angle, y_angle, lte_direction_factor):  # 参数分别代表水平方向角，垂直方向角，方向图
    for i in range(181):
        for j in range(360):
            if (y_angle + 90 == i) and (x_angle + 179 == j):
                return (lte_direction_factor[i][j])  # 返回方向系数


# 查表得到对应user二维方向角的二维方向系数
def user_calcu_direction_factor(x_angle, y_angle, user_direction_factor):  # 参数分别代表水平方向角，垂直方向角，方向图
    for i in range(181):
        for j in range(360):
            if (y_angle + 90 == i) and (x_angle + 179 == j):
                return user_direction_factor[i][j]  # 返回方向系数


# 查表得到对应radar二维方向角的二维方向系数
def radar_calcu_direction_factor(x_angle, y_angle, radar_direction_factor):  # 参数分别代表水平方向角，垂直方向角，方向图
    for i in range(181):
        for j in range(360):
            if (y_angle + 90 == i) and (x_angle + 179 == j):
                return radar_direction_factor[i][j]  # 返回方向系数


# 计算lte增益汇总函数G=D*loss_factor
def lte_gain(x, y, d, node_height, radar_height, node_loss_factor, radar_loss_factor, lte_direction_factor,
             radar_direction_factor, lte_antenna_gain, radar_antenna_gain, elevation, lte_feederline_factor,
             radar_feederline_factor):
    radar_x_angle, node_x_angle = calcu_x_direction_angle(x, y)  # 计算雷达、节点的水平方向角
    radar_y_angle, node_y_angle = calcu_y_direction_angle(d, node_height, radar_height, elevation)
    # 计算雷达、节点的垂直方向角
    radar_d_f = radar_calcu_direction_factor(radar_x_angle, radar_y_angle,
                                             radar_direction_factor)  # 计算雷达二维方向系数（db）
    node_d_f = lte_calcu_direction_factor(node_x_angle, node_y_angle,
                                          lte_direction_factor)  # 计算节点二维方向系数（db）
    final_gain = 10 * log10(
        node_loss_factor * radar_loss_factor) + radar_d_f + node_d_f + lte_antenna_gain + radar_antenna_gain \
                 - lte_feederline_factor - radar_feederline_factor
    # 总增益=最大方向增益+各角度相对增益+损耗因素
    return final_gain


# 计算user增益汇总函数G=D*loss_factor
def user_gain(x, y, d, node_height, radar_height, node_loss_factor, radar_loss_factor, user_direction_factor,
              radar_direction_factor, user_antenna_gain, radar_antenna_gain, elevation, radar_feederline_factor):
    # 参数分别为坐标、节点高度、雷达高度、节点损耗因子、雷达损耗因子、两个方向图，两个天线增益
    radar_x_angle, node_x_angle = calcu_x_direction_angle(x, y)  # 计算雷达、节点的水平方向角
    radar_y_angle, node_y_angle = calcu_y_direction_angle(d, node_height, radar_height, elevation)
    # 计算雷达、节点的垂直方向角
    radar_d_f = radar_calcu_direction_factor(radar_x_angle, radar_y_angle,
                                             radar_direction_factor)  # 计算雷达二维方向系数（db）
    node_d_f = user_calcu_direction_factor(node_x_angle, node_y_angle,
                                           user_direction_factor)  # 计算节点二维方向系数（db）
    final_gain = 10 * log10(
        node_loss_factor * radar_loss_factor) + radar_d_f + node_d_f + user_antenna_gain + radar_antenna_gain \
                 - radar_feederline_factor
    # 总增益=最大方向增益+各角度相对增益+损耗因素
    return final_gain
