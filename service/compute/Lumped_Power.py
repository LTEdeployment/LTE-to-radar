from Lte_Node_Generation import *
from User_Generation import *
from Radar_Generation import *
from User_Power_Control import *
from Gain import *
from Paint import *


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
    impact = 0
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
    impact = 0
    impact = pt + user_gain(x, y, d, node_height, radar_height, node_loss_factor, radar_loss_factor,
                            user_direction_factor,
                            radar_direction_factor, user_antenna_gain, radar_antenna_gain, elevation,
                            radar_feederline_factor) - attenuation(radar_height, node_height, frequency, d,
                                                                   environment1, environment2)  # 结果为dB的形式
    impact = dbm_convert_w(impact)  # dbm转w
    return impact


# 计算全部lte及user的功率集总
def sum_impact(legal_lte_numbers, user_numbers, lte_direction_factor, user_direction_factor, radar_direction_factor,
               environment1, environment2, elevation, branch,
               bindwidth):
    impact = 0
    Kpm = 0
    if branch == 2:  # 下行链路，只有基站
        for i in range(legal_lte_numbers):
            impact += lte_single_impact(lte[i].trans_power, lte[i].x, lte[i].y, lte[i].distance, lte[i].height,
                                        radar1.height,
                                        lte[i].loss_factor, radar1.loss_factor, lte[i].frequency, lte_direction_factor,
                                        radar_direction_factor,
                                        lte[i].antenna_gain, radar1.antenna_gain, environment1, environment2, elevation,
                                        lte[i].feederline_factor, radar1.feederline_factor)  # 外功率集总干扰

            Kpm += gain_r(lte[i].x, lte[i].y, lte[i].distance, lte[i].height, radar1.height, radar1.loss_factor,
                          radar_direction_factor, elevation, radar1.feederline_factor, radar1.antenna_gain)  # 接收天线总增益
        node_numbers=legal_lte_numbers # 参与干扰的节点数目

    elif branch == 1:  # 上行链路，只有终端
        for i in range(user_numbers):
            impact += user_single_impact(user[i].trans_power, user[i].x, user[i].y, user[i].distance_of_radar,
                                         user[i].height,
                                         radar1.height,
                                         user[i].loss_factor, radar1.loss_factor, user[i].frequency, user_direction_factor,
                                         radar_direction_factor,
                                         user[i].antenna_gain, radar1.antenna_gain, environment1, environment2, elevation,
                                         radar1.feederline_factor)
            Kpm += gain_r(user[i].x, user[i].y, user[i].distance_of_radar, user[i].height, radar1.height, radar1.loss_factor,
                      radar_direction_factor, elevation, radar1.feederline_factor, radar1.antenna_gain)
        node_numbers = user_numbers
    Kpm = Kpm / node_numbers
    No = -144 + 10 * log10(bindwidth) + radar1.noise_factor + Kpm # 输出噪声功率，单位db
    Nox = 10 ** (No / 10) # 输出噪声功率，单位w
    impact += Nox # 总干扰等于外信号功率+噪声
    impact = w_convert_dbm(impact)
    return impact


# 赋值+集总
def gathering(antenna_flag, lte_min_d, sR, lR, lP, lH, lF, uH, uF, bindwidth, rH, lte_antenna_gain, user_antenna_gain,
              radar_antenna_gain, lte_loss_factor, user_loss_factor, radar_loss_factor, lte_direction_factor,
              user_direction_factor, radar_direction_factor, environment1, environment2, elevation, branch,
              resource_block, lte_feederline_factor, radar_feederline_factor, lte_NF, user_NF, radar_NF):
    # 系统载入部分
    cell_radius, hexagon_length, legal_lte_numbers = lte_node_generation(sR, lR, antenna_flag,
                                                                         lte_min_d)  # 得到小区半径、六边形长度、有效基站数目
    print(legal_lte_numbers)
    # LTE载入部分
    for i in range(legal_lte_numbers):
        lte[i].trans_power = lP  # 功率赋值
        lte[i].height = lH  # 高度赋值
        lte[i].frequency = lF  # 频率赋值
        lte[i].feederline_factor = lte_feederline_factor  # 馈线损耗赋值
        lte[i].noise_factor = lte_NF  # 噪声系数赋值
        lte[i].loss_factor = lte_loss_factor  # 损耗因子赋值
        lte[i].antenna_gain = lte_antenna_gain  # 天线增益赋值

    # USER载入部分
    single_users = acp_celluser_numbers(bindwidth, resource_block)  # 根据带宽确定每个小区的用户数目
    user_numbers = usergenerated(sR, lR, single_users, legal_lte_numbers, cell_radius)  # 返回所有用户数目，给user参数赋值

    for i in range(user_numbers):
        user[i].height = uH  # 高度赋值
        user[i].frequency = uF  # 频率赋值
        user[i].noise_factor = user_NF  # 噪声系数赋值
        user[i].loss_factor = user_loss_factor  # 损耗因子赋值
        user[i].antenna_gain = user_antenna_gain  # 天线增益赋值

    user_power_control(bindwidth, user_numbers, environment1, environment2)  # 功率控制

    # RADAR载入部分
    radar1.height = rH  # 高度赋值
    radar1.feederline_factor = radar_feederline_factor  # 馈线损耗赋值
    radar1.noise_factor = radar_NF  # 噪声系数赋值
    radar1.loss_factor = radar_loss_factor  # 损耗因子赋值
    radar1.antenna_gain = radar_antenna_gain  # 天线增益赋值

    # 集总干扰载入部分
    return sum_impact(legal_lte_numbers, user_numbers, lte_direction_factor, user_direction_factor,
                      radar_direction_factor,
                      environment1, environment2,
                      elevation, branch, bindwidth)  # 得到功率集总


# 判断是否对RADAR产生干扰
def judge_affect(antenna_flag, lte_min_d, sR, lR, lP, lH, lF, uH, uF, bindwidth, rH, lte_antenna_gain,
                 user_antenna_gain,
                 radar_antenna_gain, lte_loss_factor, user_loss_factor, radar_loss_factor, threshold,
                 lte_direction_factor, user_direction_factor, radar_direction_factor, environment1, environment2,
                 elevation, branch, resource_block, lte_feederline_factor, radar_feederline_factor, lte_NF, user_NF,
                 radar_NF):
    haha = gathering(antenna_flag, lte_min_d, sR, lR, lP, lH, lF, uH, uF, bindwidth, rH, lte_antenna_gain,
                     user_antenna_gain,
                     radar_antenna_gain, lte_loss_factor, user_loss_factor, radar_loss_factor, lte_direction_factor,
                     user_direction_factor, radar_direction_factor, environment1, environment2, elevation, branch,
                     resource_block, lte_feederline_factor, radar_feederline_factor, lte_NF, user_NF,
                     radar_NF)  # 计算功率集总
    print(haha)
    radar1.threshold = threshold
    if haha <= radar1.threshold:
        return False
    else:
        return True


# 计算干扰概率
def calcu_probability(antenna_flag, lte_min_d, sR, lR, lP, lH, lF, uH, uF, bindwidth, rH, lte_antenna_gain,
                      user_antenna_gain,
                      radar_antenna_gain, lte_loss_factor, user_loss_factor, radar_loss_factor, threshold,
                      lte_direction_factor, user_direction_factor, radar_direction_factor, environment1, environment2,
                      elevation, branch, resource_block, lte_feederline_factor, radar_feederline_factor, lte_NF,
                      user_NF, radar_NF):
    # 几次干扰
    s = 0
    #for i in range(10):
    for i in range(1):
        # boolean 干扰或者不干扰
        hahaha = judge_affect(antenna_flag, lte_min_d, sR, lR, lP, lH, lF, uH, uF, bindwidth, rH, lte_antenna_gain,
                              user_antenna_gain,
                              radar_antenna_gain, lte_loss_factor, user_loss_factor, radar_loss_factor,
                              threshold, lte_direction_factor, user_direction_factor, radar_direction_factor,
                              environment1, environment2, elevation, branch, resource_block, lte_feederline_factor,
                              radar_feederline_factor, lte_NF, user_NF, radar_NF)  # 判断是否干扰
        if hahaha:
            s += 1
    return s / 10


def final_paint(antenna_flag, lte_min_d, sR, lR, bindwidth):
    cell_radius, hexagon_length, legal_lte_numbers = lte_node_generation(sR, lR, antenna_flag,
                                                                         lte_min_d)
    single_users = acp_celluser_numbers(bindwidth)  # 根据带宽确定每个小区的用户数目
    user_numbers = usergenerated(sR, lR, single_users, legal_lte_numbers, cell_radius)  # 返回所有用户数目，给user参数赋值
    paint(hexagon_length, legal_lte_numbers, user_numbers)
