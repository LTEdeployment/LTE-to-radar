from math import *

def attenuation(hr,hb,frequency,distance,enviorment1,enviorment2):#参数分别为：接收方高度，发射方高度，双方距离，环境1分为大城市或中小城市，环境2分为城市，郊区，农村，丘陵，开阔区
    if frequency<300:#单位MHz
        if enviorment1==1:#大城市场景
            a=8.29*((log10(1.54*hb))**2)-1.1#a表示移动台天线修正因子
            L=69.55+26.16*log10(frequency)-13.82*log10(hr)-a+(44.9-6.55*log(hr))*log(distance)
            if enviorment2==1:#城市场景
                path_loss=L
            elif enviorment2==2:#郊区场景
                path_loss=L-2*(log10(frequency/28))**2-5.4
            elif enviorment2==3:#农村场景
                path_loss=L-4.78*(log10(frequency))**2-18.33*log10(frequency)+40.98
            elif enviorment2==4: #丘陵场景
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98-10
            elif enviorment2==5:#开阔区
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98-25

        elif enviorment1==2:##2表示中小城市
            a=(1.1*log10(frequency)-0.7)*hb-(1.56*log10(frequency)-0.8)
            L = 69.55 + 26.16 * log10(frequency) - 13.82 * log10(hr) - a + (44.9 - 6.55 * log(
                hr)) * log(distance)
            if enviorment2==1:#城市场景
                path_loss=L
            elif enviorment2==2:#郊区场景
                path_loss=L-2*(log10(frequency/28))**2-5.4
            elif enviorment2==3:#农村场景
                path_loss=L-4.78*(log10(frequency))**2-18.33*log10(frequency)+40.98
            elif enviorment2==4: #丘陵场景
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98-10
            elif enviorment2==5:#开阔区
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98-25
    elif 300<=frequency<=1500:
        if enviorment1 == 1:  # 大城市场景
            a = 3.2*(log10(11.75*hb))**2-4.97  # a表示移动台天线修正因子
            L = 69.55 + 26.16 * log10(frequency) - 13.82 * log10(hr) - a + (44.9 - 6.55 * log(
                hr)) * log(distance)
            if enviorment2 == 1:  # 城市场景
                path_loss = L
            elif enviorment2 == 2:  # 郊区场景
                path_loss = L - 2 * (log10(frequency / 28)) ** 2 - 5.4
            elif enviorment2 == 3:  # 农村场景
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98
            elif enviorment2 == 4:  # 丘陵场景
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98 - 10
            elif enviorment2 == 5:  # 开阔区
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98 - 25

        elif enviorment1 == 2:  ##2表示中小城市
            a = (1.1 * log10(frequency) - 0.7) * hb - (1.56 * log10(frequency) - 0.8)
            L = 69.55 + 26.16 * log10(frequency) - 13.82 * log10(hr) - a + (44.9 - 6.55 * log(
                hr)) * log(distance)
            if enviorment2 == 1:  # 城市场景
                path_loss = L
            elif enviorment2 == 2:  # 郊区场景
                path_loss = L - 2 * (log10(frequency / 28)) ** 2 - 5.4
            elif enviorment2 == 3:  # 农村场景
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98
            elif enviorment2 == 4:  # 丘陵场景
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98 - 10
            elif enviorment2 == 5:  # 开阔区
                path_loss = L - 4.78*(log10(frequency)) ** 2 - 18.33 * log10(frequency) + 40.98 - 25
    elif frequency>1500:
        if enviorment1==1:#大城市
            a = 3.2 * (log10(11.75 * hb)) ** 2 - 4.97  # a表示移动台天线修正因子
            path_loss=46.3+33.9*log10(frequency)-13.82*log(hr)-a+(44.9-6.55*log10(hr))*log10(distance)+3-20
        elif enviorment1==2:#中小城市
            a = (1.1 * log10(frequency) - 0.7) * hb - (1.56 * log10(frequency) - 0.8)
            path_loss = 46.3 + 33.9 * log10(frequency) - 13.82 * log(hr) - a + (44.9 - 6.55 * log10(
                hr)) * log10(distance) -20
    elif frequency > 2600:
        path_loss = 12.7 + 37.9 * log10(distance)
    elif frequency > 4900:
        path_loss = 21.9 + 35.5 * log10(distance)
    elif frequency > 5400:
        path_loss = 30.9 + 32.7 * log10(distance)
    return path_loss##返回衰减

