from Path_Loss import *
from User_Generation import *


# 对用户发射功率进行控制
def user_power_control(bw, user_numbers, environment1, environment2):  # 带宽
    # 根据带宽大小确定上行功控的预设路损值，超过它，用户以最大功率发射
    if bw == 5:
        Pld = 115
    elif bw == 10:
        Pld = 112
    elif bw == 15:
        Pld = 110
    elif bw == 20:
        Pld = 109
        # 确定user发射功率
    for i in range(user_numbers):
        pl = attenuation(lte[user[i].access_lte].height, user[i].height, user[i].frequency, user[i].distance_of_lte,
                         environment1, environment2)  # 对于所有的用户，计算到接入基站的路损
        if 0.75 < (pl / Pld) < 1:
            user[i].trans_power = 23 * pl / Pld
        elif (pl / Pld) < 0.75:
            user[i].trans_power = 14
        elif (pl / Pld) > 1:
            user[i].trans_power = 23
