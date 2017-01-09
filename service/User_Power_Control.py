# -*- coding: utf-8 -*-
from Path_Loss import *
from User_Generation import *
import random


# 对用户发射功率进行控制
def user_power_control(transpmax, compensation_factor, resource_block, user_numbers, environment1,
                       environment2):  # 路径损耗补偿因子,每用户占用RB数目，用户数目，环境1，2

    for i in range(user_numbers):
        pl = attenuation(lte[user[i].access_lte].height, user[i].height, user[i].frequency, user[i].distance_of_lte,
                         environment1, environment2)  # 对于所有的用户，计算到接入基站的路损
        sinr = random.randint(0, 25)  ##目标信噪比
        I_serv = random.randint(-134, 0)  ##相邻小区的干扰
        if compensation_factor == 1:
            p = sinr + I_serv + pl + 10 * log10(resource_block)  ##开环发射功率
            if p >= transpmax:  ##transpmax为最大发射功率
                user[i].trans_power = transpmax
            else:
                user[i].trans_power = p
        else:
            sinr = sinr - (1 - compensation_factor) * pl
            p = sinr + I_serv + compensation_factor * pl + 10 * log10(resource_block)
            if p >= transpmax:
                user[i].trans_power = transpmax
            else:
                user[i].trans_power = p
