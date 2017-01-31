# -*- coding: utf-8 -*-
from math import *
from Struct import *


# 初始化若干个lte基站
lte = [0] * 150000  # 给数组赋初值
for i in range(150000):  # 将已经赋初值的数组变为数组类
    lte[i] = Lte()


##计算n-1圈基站总和：
def sum1(n): # 输入圈数
    i = 1
    s = 0
    while i < n:
        s += 6 * i
        i += 1
    return s


##判断有几圈：
def num(n): # 基站数目
    i = 1
    s = 1
    while i <= 150000:
        if (n > sum1(i)) and (n <= sum1(i + 1)):
            s = i
            break
        else:
            i += 1
    return s


##定义计算方法：
def rightup(i, s):  ##右上角坐标计算
    lte[sum1(i)].x = 1.5 * i
    lte[sum1(i)].y = sqrt(3) / 2 * i  ##找出基准点坐标
    j = 1
    while j < s:
        lte[sum1(i) + j].x = lte[sum1(i)].x - 1.5 * j
        lte[sum1(i) + j].y = lte[sum1(i)].y + sqrt(3) / 2 * j
        j += 1


def leftup(i, s):  ##左上角坐标计算
    rightup(i, i + 1)
    j = 1
    while j <= (s - (i + 1)):
        lte[sum1(i) + i + j].x = lte[sum1(i) + i].x - 1.5 * j
        lte[sum1(i) + i + j].y = lte[sum1(i) + i].y - sqrt(3) / 2 * j
        j += 1


def leftcen(i, s):  ##左中角坐标计算
    leftup(i, 2 * i + 1)
    j = 1
    while j <= (s - (2 * i + 1)):
        lte[sum1(i) + 2 * i + j].x = lte[sum1(i) + 2 * i].x
        lte[sum1(i) + 2 * i + j].y = lte[sum1(i) + 2 * i].y - sqrt(3) * j
        j += 1


def leftdown(i, s):  ##左下角坐标计算
    leftcen(i, 3 * i + 1)
    j = 1
    while j <= (s - (3 * i + 1)):
        lte[sum1(i) + 3 * i + j].x = lte[sum1(i) + 3 * i].x + 1.5 * j
        lte[sum1(i) + 3 * i + j].y = lte[sum1(i) + 3 * i].y - sqrt(3) / 2 * j
        j += 1


def rightdown(i, s):  ##右下角坐标计算
    leftdown(i, 4 * i + 1)
    j = 1
    while j <= (s - (4 * i + 1)):
        lte[sum1(i) + 4 * i + j].x = lte[sum1(i) + 4 * i].x + 1.5 * j
        lte[sum1(i) + 4 * i + j].y = lte[sum1(i) + 4 * i].y + sqrt(3) / 2 * j
        j += 1


def rightcen(i, s):  ##右中角坐标计算
    rightdown(i, 5 * i + 1)
    j = 1
    while j <= (s - (5 * i + 1)):
        lte[sum1(i) + 5 * i + j].x = lte[sum1(i) + 5 * i].x
        lte[sum1(i) + 5 * i + j].y = lte[sum1(i) + 5 * i].y + sqrt(3) * j
        j += 1


##给第一圈坐标赋值：
def fir(n):
    def c1():
        lte[0].x = 1.5
        lte[0].y = sqrt(3) / 2

    def c2():
        c1()
        lte[1].x = 0
        lte[1].y = sqrt(3)

    def c3():
        c2()
        lte[2].x = -1.5
        lte[2].y = sqrt(3) / 2

    def c4():
        c3()
        lte[3].x = -1.5
        lte[3].y = -sqrt(3) / 2

    def c5():
        c4()
        lte[4].x = 0
        lte[4].y = -sqrt(3)

    def c6():
        c5()
        lte[5].x = 1.5
        lte[5].y = -sqrt(3) / 2

    if n == 1:
        c1()
    elif n == 2:
        c2()
    elif n == 3:
        c3()
    elif n == 4:
        c4()
    elif n == 5:
        c5()
    else:
        c6()


##计算第i圈所有点坐标：
def calcu1(i):
    if i == 1:  ##给第一圈所有点赋值
        fir(6)
    else:
        rightcen(i, 6 * i)  ##给其余圈所有点坐标赋值


##计算最后一圈的坐标：
def calcu2(n): # 输入基站数目
    if num(n) == 1:
        fir(n)
    else:
        i = 1
        s = 0
        while i < num(n):  ##求前n-1圈基站数目总和
            s += 6 * i
            i += 1
        supl = n - s  ##求剩余
        if (supl > 0) and (supl <= num(n) + 1):  ##右上角
            rightup(num(n), supl)

        if (supl > num(n) + 1) and (supl <= 2 * num(n) + 1):  ##左上角
            leftup(num(n), supl)

        if (supl > 2 * num(n) + 1) and (supl <= 3 * num(n) + 1):  ##左中角
            leftcen(num(n), supl)

        if (supl > 3 * num(n) + 1) and (supl <= 4 * num(n) + 1):  ##左下角
            leftdown(num(n), supl)

        if (supl > 4 * num(n) + 1) and (supl <= 5 * num(n) + 1):  ##右下角
            rightdown(num(n), supl)

        if (supl > 5 * num(n) + 1) and (supl < 6 * num(n) + 1):  ##右中角
            rightcen(num(n), supl)


            ##计算所有点坐标：

##点坐标整体乘边长：
def magnify(n, hexagon_length):  # 输入节点数目，六边形边长
    for a in range(0, n):
        lte[a].x = lte[a].x * hexagon_length
        lte[a].y = lte[a].y * hexagon_length


# 计算n个节点的坐标
def calcu(n,hexagon_length): # 输入节点数目、六边形边长
    i = 1
    while i < num(n):
        calcu1(i)
        i += 1
    calcu2(n)
    magnify(n,hexagon_length)


##获取lte基站到雷达的距离
def acqD(n):
    for i in range(n):
        lte[i].distance = sqrt((lte[i].x) ** 2 + (lte[i].y) ** 2)


# 筛选出符合条件的lte
def filtrate(r1, r2): # 输入干扰半径、仿真半径
    lte_copy = [0] * 150000  # 初始化一个新的数组
    for i in range(150000):  # 将其变为数组类
        lte_copy[i] = Lte()

    legal_lte_numbers = 0  # 将其初始化

    for i in range(150000):  # 筛选
        if (lte[i].distance >= r1) and (lte[i].distance <= r2):
            lte_copy[legal_lte_numbers] = lte[i]  # 如果lte[i]满足条件，将此节点添加至lte_copy中
            legal_lte_numbers += 1  # 有效节点数目加1
    for i in range(150000):  # 把lte_copy全部赋值给lte数组类
        lte[i] = lte_copy[i]
    return legal_lte_numbers # 返回有效基站数目


# 根据是否采用三扇区计算小区半径,六边形边长
def acq_cr_hl(antenna_flag,lte_min_d): # 输入天线模式、基站最近间距
    if antenna_flag == 2:  # 全向天线
        cell_radius = lte_min_d / sqrt(3) /1000 # 小区半径等于基站最近间距/sqrt(3)
        hexagon_length=cell_radius # 六边形边长等于小区半径
    elif antenna_flag==1:  # 120度天线
        cell_radius = lte_min_d / 1.5 /1000 # 小区半径等于基站最近间距/1.5
        hexagon_length = cell_radius*sqrt(3)/2  # 六边形边长等于小区半径乘sqrt(3)/2
    return cell_radius,hexagon_length # 返回小区半径，六边形边长


# 节点产生汇总函数
def lte_node_generation(r1_init, r2_init,antenna_flag,lte_min_d):  # 输入两个半径，天线模式，基站最近间距
    cell_radius, hexagon_length = acq_cr_hl(antenna_flag,lte_min_d)
    calcu(150000,hexagon_length)  # 获取150000个基站的坐标
    acqD(150000)  # 获取150000个基站的距离
    legal_lte_numbers=filtrate(r1_init, r2_init)  # 筛选出符合条件的基站
    return cell_radius, hexagon_length,legal_lte_numbers # 返回小区半径，六边形边长，有效基站数目
