# -*- coding: utf-8 -*-
# 定义lte基站类
class Lte:
    x = 0  # 横坐标
    y = 0  # 纵坐标

    height = 0  # 高度
    trans_power = 0  # 发射功率
    frequency = 0  # 频率
    distance = 0  # 距离
    loss_factor = 0  # 损耗因子
    feederline_factor=0 # 馈线损耗
    noise_factor=0 # 噪声系数
    antenna_gain=0 # 天线增益
    servingusers = 0  # lte已接入用户数目


# 定义radar雷达类
class Radar:
    height = 0  # 高度
    loss_factor = 0  # 损耗因子
    threshold = 0  # 干扰门限
    feederline_factor=0 # 馈线损耗
    noise_factor=0 # 噪声系数
    antenna_gain=0 # 天线增益


# 定义User类
class User:
    x = 0  # 横坐标
    y = 0  # 纵坐标
    access_lte = 0  # 接入的lte基站号
    trans_power = 0  # 发射功率
    height = 0  # 高度
    frequency = 0  # 频率
    distance_of_lte = 0  # 与选中的lte基站的距离
    distance_of_radar = 0  # 与雷达的距离
    noise_factor = 0  # 噪声系数
    antenna_gain = 0  # 天线增益
    loss_factor = 0  # 损耗因子