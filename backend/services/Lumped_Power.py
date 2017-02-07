# -*- coding: utf-8 -*-
from Gain import *
from Radar_Generation import *
from User_Power_Control import *
from Direction_Map import *

# 单位dbm转w
def dbm_convert_w(x_dbm):
    x_w = (10 ** (x_dbm / 10)) / 1000
    return x_w


# 单位w转dbm
def w_convert_dbm(x_w):
    x_dbm = 10 * log10(1000 * x_w)
    return x_dbm


# 计算单个lte的功率传递过程
# 参数依次为发射功率、坐标、距离、节点高度、雷达高度、节点损耗因子、雷达损耗因子、频率
def lte_single_impact(pt, x, y, d, node_height, radar_height, node_loss_factor, radar_loss_factor, frequency,
                      lte_direction_factor, radar_direction_factor, lte_antenna_gain, radar_antenna_gain, environment1,
                      environment2, elevation, lte_feederline_factor, radar_feederline_factor):
    impact = pt + lte_gain(x, y, d, node_height, radar_height, node_loss_factor,
                           radar_loss_factor, lte_direction_factor, radar_direction_factor, lte_antenna_gain,
                           radar_antenna_gain, elevation, lte_feederline_factor, radar_feederline_factor) - attenuation(
        radar_height, node_height, frequency, d,
        environment1,
        environment2)  # 结果为dB的单位
    impact = dbm_convert_w(impact)  # dbm转w
    return impact

# 计算单个user的功率传递过程
# 参数依次为发射功率、坐标、距离、节点高度、雷达高度、节点损耗因子、雷达损耗因子、频率
def user_single_impact(pt, x, y, d, node_height, radar_height, node_loss_factor, radar_loss_factor, frequency,
                       user_direction_factor, radar_direction_factor, user_antenna_gain, radar_antenna_gain,
                       environment1,
                       environment2, elevation, radar_feederline_factor):
    impact = pt + user_gain(x, y, d, node_height, radar_height, node_loss_factor, radar_loss_factor,
                            user_direction_factor,
                            radar_direction_factor, user_antenna_gain, radar_antenna_gain, elevation,
                            radar_feederline_factor) - attenuation(radar_height, node_height, frequency, d,
                                                                   environment1, environment2)  # 结果为dB的形式
    impact = dbm_convert_w(impact)  # dbm转w
    return impact


# 计算全部lte及user的功率集总
def sum_impact(legal_lte_numbers, user_numbers, lte_direction_factor, user_direction_factor, radar_direction_factor,
               environment1, environment2, elevation, branch):
    impact = 0
    if branch == 2:  # 下行链路，只有基站
        for i in range(legal_lte_numbers):
            impact += lte_single_impact(lte[i].trans_power, lte[i].x, lte[i].y, lte[i].distance, lte[i].height,
                                        radar1.height,
                                        lte[i].loss_factor, radar1.loss_factor, lte[i].frequency, lte_direction_factor,
                                        radar_direction_factor,
                                        lte[i].antenna_gain, radar1.antenna_gain, environment1, environment2, elevation,
                                        lte[i].feederline_factor, radar1.feederline_factor)  # 外功率集总干扰
    elif branch == 1:  # 上行链路，只有终端
        for i in range(user_numbers):
            impact += user_single_impact(user[i].trans_power, user[i].x, user[i].y, user[i].distance_of_radar,
                                         user[i].height,
                                         radar1.height,
                                         user[i].loss_factor, radar1.loss_factor, user[i].frequency,
                                         user_direction_factor,
                                         radar_direction_factor,
                                         user[i].antenna_gain, radar1.antenna_gain, environment1, environment2,
                                         elevation,
                                         radar1.feederline_factor)
    impact = w_convert_dbm(impact)
    return impact


# lte节点生成、类赋值
def gathering1(antenna_flag, lte_min_d, sR, lR, lP, lH, lF, uH, uF, lte_bindwidth, rH, lte_antenna_gain, user_antenna_gain,
               radar_antenna_gain, lte_loss_factor, user_loss_factor, radar_loss_factor, resource_block,
               lte_feederline_factor, radar_feederline_factor, lte_NF, user_NF, radar_NF):
    # 系统载入部分
    cell_radius, hexagon_length, legal_lte_numbers = lte_node_generation(sR, lR, antenna_flag,
                                                                         lte_min_d)  # 得到小区半径、六边形长度、有效基站数目
    # LTE载入部分
    for i in range(legal_lte_numbers):
        lte[i].trans_power = lP  # 功率赋值
        lte[i].height = lH  # 高度赋值
        lte[i].frequency = lF  # 频率赋值
        lte[i].feederline_factor = lte_feederline_factor  # 馈线损耗赋值
        lte[i].noise_factor = lte_NF  # 噪声系数赋值
        lte[i].loss_factor = lte_loss_factor  # 损耗因子赋值
        lte[i].antenna_gain = lte_antenna_gain  # 天线增益赋值

    # RADAR载入部分
    radar1.height = rH  # 高度赋值
    radar1.feederline_factor = radar_feederline_factor  # 馈线损耗赋值
    radar1.noise_factor = radar_NF  # 噪声系数赋值
    radar1.loss_factor = radar_loss_factor  # 损耗因子赋值
    radar1.antenna_gain = radar_antenna_gain  # 天线增益赋值

    # USER载入部分
    single_users = acp_celluser_numbers(lte_bindwidth, resource_block)  # 根据带宽确定每个小区的用户数目
    user_numbers = single_users * legal_lte_numbers  # 计算所有用户数目
    for i in range(user_numbers):
        user[i].height = uH  # 高度赋值
        user[i].frequency = uF  # 频率赋值
        user[i].noise_factor = user_NF  # 噪声系数赋值
        user[i].loss_factor = user_loss_factor  # 损耗因子赋值
        user[i].antenna_gain = user_antenna_gain  # 天线增益赋值

    return cell_radius, legal_lte_numbers, single_users, user_numbers
    # 返回小区半径、有效基站数目、单个小区用户数目、总用户数目


# 用户生成、链路生成、计算干扰
def gathering2(cell_radius, legal_lte_numbers, single_users, user_numbers, sR, lR,
               lte_direction_factor, user_direction_factor, radar_direction_factor, environment1,
               environment2, elevation, branch, resource_block, uti_or_multi, compensation_factor, transpmax):
    if branch==1: # 上行才产生用户
        usergenerated(sR, lR, single_users, legal_lte_numbers, cell_radius)  # 随机产生user
        user_power_control(transpmax, compensation_factor, resource_block, user_numbers, environment1, environment2)  # 功率控制
    if uti_or_multi == 1:  # 多源干扰
        # 集总干扰载入部分
        return sum_impact(legal_lte_numbers, user_numbers, lte_direction_factor, user_direction_factor,
                          radar_direction_factor,
                          environment1, environment2,
                          elevation, branch)  # 得到功率集总
    elif uti_or_multi == 2:  # 单源干扰
        single_impact = lte_single_impact(lte[0].trans_power, lte[0].x, lte[0].y, lte[0].distance, lte[0].height,
                                          radar1.height,
                                          lte[0].loss_factor, radar1.loss_factor, lte[0].frequency,
                                          lte_direction_factor,
                                          radar_direction_factor,
                                          lte[0].antenna_gain, radar1.antenna_gain, environment1, environment2,
                                          elevation,
                                          lte[0].feederline_factor, radar1.feederline_factor)  # W的形式
        single_impact = w_convert_dbm(single_impact)  # dBm的形式
        return single_impact


# 加入ACIR的main函数
def exe_main(acir_min, acir_max, acir_space, antenna_flag, lte_min_d, sR, lR, lP, lH, lF, uH, uF, lte_bindwidth, rH,
             lte_antenna_gain,
             user_antenna_gain, radar_antenna_gain, lte_loss_factor, user_loss_factor, radar_loss_factor,
             radar_bindwidth,
             lte_direction_factor, user_direction_factor, radar_direction_factor, environment1, environment2,
             elevation, branch, resource_block, lte_feederline_factor, radar_feederline_factor, lte_NF,
             user_NF, radar_NF, uti_or_multi, compensation_factor, transpmax, cycle_index):
    # lte节点生成、类赋值（只做一次即可）
    cell_radius, legal_lte_numbers, single_users, user_numbers = gathering1(antenna_flag, lte_min_d, sR,
                                                                            lR, lP, lH, lF, uH, uF,
                                                                            lte_bindwidth, rH,
                                                                            lte_antenna_gain,
                                                                            user_antenna_gain,
                                                                            radar_antenna_gain,
                                                                            lte_loss_factor,
                                                                            user_loss_factor,
                                                                            radar_loss_factor,
                                                                            resource_block,
                                                                            lte_feederline_factor,
                                                                            radar_feederline_factor,
                                                                            lte_NF, user_NF, radar_NF)
    lte_direction_factor = resort120(lte_direction_factor, antenna_flag) # 如果又需要的话，对lte方向图做三扇区修正
    # 干扰阈值
    threshold = -174 + 10 * log10(radar_bindwidth * 1000000) + radar1.noise_factor - 10
    # acir部分
    j = 0  # 记录数组序号
    acir = acir_min
    threshold += acir_min
    while acir <= acir_max:  # 在最大值与最小值之间循环调用函数
        # 计算干扰概率
        s = 0
        print('threshold: %s' % threshold)
        for i in range(cycle_index):  # 参数为循环次数
            sum_result = gathering2(cell_radius, legal_lte_numbers, single_users, user_numbers, sR, lR,
                                    lte_direction_factor, user_direction_factor, radar_direction_factor, environment1,
                                    environment2, elevation, branch, resource_block, uti_or_multi, compensation_factor,
                                    transpmax)  # 得到集总结果
            print('sum_result: %s' % sum_result)
            if sum_result > threshold:
                s += 1
        yield (float(s) / float(cycle_index))
        threshold += acir_space
        acir += acir_space
        j += 1
    return

