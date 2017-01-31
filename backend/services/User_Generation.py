# -*- coding: utf-8 -*-
import random as r

from Lte_Node_Generation import *

user = [0] * 10000000  # 初始化所有用户
for i in range(10000000):
    user[i] = User()  # 实例化每一个用户


# 根据带宽得到每个小区接入的用户数目
def acp_celluser_numbers(bw, resource_block):  # bw代表带宽
    if bw == 1.4:
        bb = 6 / resource_block
    elif bw == 3:
        bb = 15 / resource_block
    elif bw == 5:
        bb = 25 / resource_block
    elif bw == 10:
        bb = 50 / resource_block
    elif bw == 15:
        bb = 75 / resource_block
    elif bw == 20:
        bb = 100 / resource_block
    bbx = int(bb)
    return bbx


# 生成用户节点，给其属性赋值
def usergenerated(r1, r2, single_users, legal_lte_numbers,
                  cell_radius):  # legal_lte_numbers为lte基站数目，cell_radius为小区半径，r1为干扰半径，r2为仿真半径

    global user

    for i in range(legal_lte_numbers):  # 循环操作之前清零
        lte[i].servingusers = 0

    user_numbers = single_users * legal_lte_numbers  # 所有用户个数等于小区数目乘每个小区接入的基站数目

    for i in range(user_numbers):  # 每个基站最多接入legal_lte_numbers个用户，即满负载

        while True:
            x = r.uniform(-r2 - cell_radius, r2 + cell_radius)  # 随机生成用户坐标
            y = r.uniform(-r2 - cell_radius, r2 + cell_radius)
            if ((sqrt(x ** 2 + y ** 2) <= (r2 + cell_radius)) and (sqrt(x ** 2 + y ** 2) >= (r1 - cell_radius))):
                user[i].x = x
                user[i].y = y
                break  # 帅选用户坐标点

        user[i].distance_of_radar = sqrt((user[i].x) ** 2 + (user[i].y) ** 2)  # 到雷达距离

        distance_of_lte = []  # 定义用户到LTE基站的距离数组
        j = 0
        for j in range(legal_lte_numbers):  # 生成用户到每一个LTE基站的距离数组
            distance_of_lte.append(sqrt((user[i].x - lte[j].x) ** 2 + (user[i].y - lte[j].y) ** 2))
        distance_lte_copy = distance_of_lte[:]  # 复制距离数组
        distance_lte_copy.sort()  # 将复制的距离数组从小到大排序
        j = 0
        for j in range(legal_lte_numbers):
            min = distance_lte_copy[j]
            flag = distance_of_lte.index(min)  ##标志最小值在到lte基站距离列表中的位置
            if lte[flag].servingusers < single_users:
                user[i].access_lte = flag
                user[i].distance_of_lte = distance_of_lte[flag]
                lte[flag].servingusers += 1  # 基站接入数目加1
                break

    return user_numbers  # 返回所有用户数目
