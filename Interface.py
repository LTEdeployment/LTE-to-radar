import win32ui
import matplotlib.pyplot as plt
import scipy.io as scio  # 引入scipy库，用于导入mat文件中方向图数据
from Lumped_Power import *
from tkinter import *

root = Tk()
root.title("LTE干扰雷达模型")

frame1 = Frame(root)
frame1.pack(side=LEFT, padx=10, pady=10)
frame2 = Frame(root)
frame2.pack(side=RIGHT, padx=10, pady=10)

##判断是否为浮点数
def jud1(char):
    try:
        float(char)
        return True
    except(ValueError):
        return False

##判断是否是空白
def jud2(char):
    if char == '':
        return True
    else:
        return False

# 判断是否大于0
def jud3(char):
    if float(char) > 0:
        return True
    else:
        return False

# 判断是否小于等于1
def jud4(char):
    if float(char) <= 1:
        return True
    else:
        return False

# 判断是否为负号
def jud5(char):
    if char == '-':
        return True
    else:
        return False

# 判断是否为整数
def jud6(char):
    try:
        int(char)
        return True
    except(ValueError):
        return False

##判断是否为大于0的浮点数
def test(content):
    if (jud2(content) or (jud1(content) and jud3(content))) == True:
        return True
    else:
        return False


testCMD = frame1.register(test)  ##包装test函数

# 判断是否为大于0小于等于1的浮点数
def test1(content):
    if (jud2(content) or (jud1(content) and jud3(content) and jud4(content))) == True:
        return True
    else:
        return False


test1CMD = frame1.register(test1)  ##包装test1函数

# 判断是否为浮点数
def test2(content):
    if (jud2(content) or jud1(content) or jud5(content)) == True:
        return True
    else:
        return False


test2CMD = frame1.register(test2)  ##包装test2函数

##判断是否为大于0的浮点数
def test3(content):
    if (jud2(content) or (jud6(content) and jud3(content))) == True:
        return True
    else:
        return False


test3CMD = frame1.register(test3)  ##包装test函数


def test_error():
    master1 = Tk()
    master1.geometry('500x100+375+350')
    Label(master1, text="输入错误!!!" + '\n' + "此输入框只允许输入大于0的浮点数，请重新输入~").pack(padx=10, pady=10)
    return True


def test1_error():
    master2 = Tk()
    master2.geometry('500x100+375+350')
    Label(master2, text="输入错误!!!" + '\n' + "此输入框只允许输入大于0小于等于1的浮点数，请重新输入~").pack(padx=10, pady=10)
    return True


def test2_error():
    master3 = Tk()
    master3.geometry('500x100+375+350')
    Label(master3, text="输入错误!!!" + '\n' + "此输入框只允许浮点数，请重新输入~").pack(padx=10, pady=10)
    return True


def test3_error():
    master4 = Tk()
    master4.geometry('500x100+375+350')
    Label(master4, text="输入错误!!!" + '\n' + "此输入框只允许正整数，请重新输入~").pack(padx=10, pady=10)
    return True


# 仿真场景部分
Label(frame1, text="仿真场景参数部分-----", justify=LEFT).grid(row=0, column=0, padx=10, pady=5)

v1 = StringVar()
Label(frame1, text="基站间最近间距", justify=LEFT).grid(row=1, column=0, padx=10, pady=5)
e1 = Entry(frame1, width=10, textvariable=v1, validate="focusout", validatecommand=(testCMD, '%P'),
           invalidcommand=test_error)
e1.grid(row=1, column=1, padx=10, pady=5)
Label(frame1, text="（m）", justify=LEFT).grid(row=1, column=2, padx=10, pady=5)

v2 = StringVar()
Label(frame1, text="隔离距离", justify=LEFT).grid(row=2, column=0, padx=10, pady=5)
e2 = Entry(frame1, width=10, textvariable=v2, validate="focusout", validatecommand=(testCMD, '%P'),
           invalidcommand=test_error)
e2.grid(row=2, column=1, padx=10, pady=5)
Label(frame1, text="（km）", justify=LEFT).grid(row=2, column=2, padx=10, pady=5)

v3 = StringVar()
Label(frame1, text="仿真区域半径", justify=LEFT).grid(row=3, column=0, padx=10, pady=5)
e3 = Entry(frame1, width=10, textvariable=v3, validate="focusout", validatecommand=(testCMD, '%P'),
           invalidcommand=test_error)
e3.grid(row=3, column=1, padx=10, pady=5)
Label(frame1, text="（km）", justify=LEFT).grid(row=3, column=2, padx=10, pady=5)

v5 = IntVar()
Label(frame1, text="是否选择三扇区", justify=LEFT).grid(row=4, column=0, padx=10, pady=5)
Radiobutton(frame1, text="是", variable=v5, value=1).grid(row=4, column=1)
Radiobutton(frame1, text="否", variable=v5, value=2).grid(row=4, column=2)

v19 = IntVar()
Label(frame1, text="选择仿真场景规模", justify=LEFT).grid(row=5, column=0, padx=10, pady=5)
Radiobutton(frame1, text="大城市", variable=v19, value=1).grid(row=5, column=1)
Radiobutton(frame1, text="中小城市", variable=v19, value=2).grid(row=5, column=2)

v20 = StringVar()
Label(frame1, text="具体场景选择", justify=LEFT).grid(row=6, column=0, padx=10, pady=5)
SB1 = Scrollbar(frame1)  # 滑动条
SB1.grid(row=6, column=2, padx=10, pady=5)
LB1 = Listbox(frame1, heigh=1, width=10, yscrollcommand=SB1.set)  # 选择栏
LB1.grid(row=6, column=1, padx=10, pady=5)
for item in ['城市场景', '郊区场景', '农村场景', '丘陵场景', '开阔区']:
    LB1.insert(END, item)
SB1.config(command=LB1.yview)


# 从选择栏得到选中场景的序号
def get_scene_index():
    result = LB1.curselection()
    pp = result[0]  # 得到选中的序号
    return pp + 1


# 载入选中的场景
def load_scene():
    result = float(get_scene_index())
    v20.set(str(result))


Button(frame1, text="载入具体场景", command=load_scene).grid(row=7, column=1, padx=10, pady=5)

v23 = IntVar()
Label(frame1, text="选择上行或者下行链路", justify=LEFT).grid(row=8, column=0, padx=10, pady=5)
Radiobutton(frame1, text="上行", variable=v23, value=1).grid(row=8, column=1)
Radiobutton(frame1, text="下行", variable=v23, value=2).grid(row=8, column=2)

v24 = StringVar()
Label(frame1, text="每个下行用户占用的资源块数", justify=LEFT).grid(row=11, column=0, padx=10, pady=5)
e24 = Entry(frame1, width=10, textvariable=v24, validate="focusout", validatecommand=(test3CMD, '%P'),
            invalidcommand=test3_error)
e24.grid(row=11, column=1, padx=10, pady=5)

v30 = IntVar()
Label(frame1, text="干扰类型", justify=LEFT).grid(row=12, column=0, padx=10, pady=5)
Radiobutton(frame1, text="多源", variable=v30, value=1).grid(row=12, column=1)
Radiobutton(frame1, text="单源", variable=v30, value=2).grid(row=12, column=2)

# 公共参数部分
Label(frame1, text="公共参数部分-----", justify=LEFT).grid(row=13, column=0, padx=10, pady=5)

v31 = StringVar()
Label(frame1, text="ACIR最小值", justify=LEFT).grid(row=14, column=0, padx=10, pady=5)
e31 = Entry(frame1, width=10, textvariable=v31, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e31.grid(row=14, column=1, padx=10, pady=5)
Label(frame1, text="（dB）", justify=LEFT).grid(row=14, column=2, padx=10, pady=5)

v32 = StringVar()
Label(frame1, text="ACIR最大值", justify=LEFT).grid(row=15, column=0, padx=10, pady=5)
e32 = Entry(frame1, width=10, textvariable=v32, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e32.grid(row=15, column=1, padx=10, pady=5)
Label(frame1, text="（dB）", justify=LEFT).grid(row=15, column=2, padx=10, pady=5)

v33 = StringVar()
Label(frame1, text="ACIR步长", justify=LEFT).grid(row=16, column=0, padx=10, pady=5)
e33 = Entry(frame1, width=10, textvariable=v33, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e33.grid(row=16, column=1, padx=10, pady=5)
Label(frame1, text="（dB）", justify=LEFT).grid(row=16, column=2, padx=10, pady=5)

v37 = StringVar()
Label(frame1, text="循环次数", justify=LEFT).grid(row=17, column=0, padx=10, pady=5)
e37 = Entry(frame1, width=10, textvariable=v37, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e37.grid(row=17, column=1, padx=10, pady=5)

# USER部分
Label(frame1, text="USER参数部分-----", justify=LEFT).grid(row=0, column=6, padx=10, pady=5)

v35 = StringVar()
Label(frame1, text="USER最大发射功率", justify=LEFT).grid(row=1, column=6, padx=10, pady=5)
e35 = Entry(frame1, width=10, textvariable=v35, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e35.grid(row=1, column=7, padx=10, pady=5)
Label(frame1, text="（dBm）", justify=LEFT).grid(row=1, column=8, padx=10, pady=5)

v6 = StringVar()
Label(frame1, text="USER高度", justify=LEFT).grid(row=2, column=6, padx=10, pady=5)
e6 = Entry(frame1, width=10, textvariable=v6, validate="focusout", validatecommand=(testCMD, '%P'),
           invalidcommand=test_error)
e6.grid(row=2, column=7, padx=10, pady=5)
Label(frame1, text="（m）", justify=LEFT).grid(row=2, column=8, padx=10, pady=5)

v7 = StringVar()
Label(frame1, text="USER发射频率", justify=LEFT).grid(row=3, column=6, padx=10, pady=5)
e7 = Entry(frame1, width=10, textvariable=v7, validate="focusout", validatecommand=(testCMD, '%P'),
           invalidcommand=test_error)
e7.grid(row=3, column=7, padx=10, pady=5)
Label(frame1, text="（MHZ）", justify=LEFT).grid(row=3, column=8, padx=10, pady=5)

v8 = StringVar()
Label(frame1, text="USER天线增益", justify=LEFT).grid(row=4, column=6, padx=10, pady=5)
e8 = Entry(frame1, width=10, textvariable=v8, validate="focusout", validatecommand=(test2CMD, '%P'),
           invalidcommand=test2_error)
e8.grid(row=4, column=7, padx=10, pady=5)
Label(frame1, text="（dBi）", justify=LEFT).grid(row=4, column=8, padx=10, pady=5)

v9 = StringVar()
Label(frame1, text="USER天线损耗因子", justify=LEFT).grid(row=5, column=6, padx=10, pady=5)
e9 = Entry(frame1, width=10, textvariable=v9, validate="focusout", validatecommand=(test1CMD, '%P'),
           invalidcommand=test1_error)
e9.grid(row=5, column=7, padx=10, pady=5)

v29 = StringVar()
Label(frame1, text="USER噪声系数", justify=LEFT).grid(row=6, column=6, padx=10, pady=5)
e29 = Entry(frame1, width=10, textvariable=v29, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e29.grid(row=6, column=7, padx=10, pady=5)
Label(frame1, text="（dB）", justify=LEFT).grid(row=6, column=8, padx=10, pady=5)


# 选取文件
def callback():
    dlg = win32ui.CreateFileDialog(1)
    dlg.DoModal()
    fileName = dlg.GetPathName()
    data = scio.loadmat(fileName)
    for key in data:
        if (key != '__globals__') and (key != '__header__') and (key != '__version__'):
            name = key
            break
    return data[name]


# 获取USER方向图
def get_u_d_m():
    global user_direction_factor
    user_direction_factor = callback()


# 显示USER垂直方向图
def show_u_d_m_y():
    ux1 = [0] * 181
    uy1 = [0] * 181
    for i in range(181):
        ux1[i] = i - 90
        uy1[i] = user_direction_factor[i][180]
    plt.plot(ux1, uy1)
    plt.show()


# 显示USER水平方向图
def show_u_d_m_x():
    ux2 = [0] * 360
    uy2 = [0] * 360
    for i in range(360):
        ux2[i] = i - 179
        uy2[i] = user_direction_factor[90][i]
    plt.plot(ux2, uy2)
    plt.show()


# LTE部分
Label(frame1, text="功控参数部分-----", justify=LEFT).grid(row=7, column=6, padx=10, pady=5)

v36 = StringVar()
Label(frame1, text="平衡因子", justify=LEFT).grid(row=8, column=6, padx=10, pady=5)
e36 = Entry(frame1, width=10, textvariable=v36, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e36.grid(row=8, column=7, padx=10, pady=5)

# LTE部分
Label(frame1, text="LTE参数部分-----", justify=LEFT).grid(row=0, column=3, padx=10, pady=5)

v10 = StringVar()
Label(frame1, text="LTE发射功率", justify=LEFT).grid(row=1, column=3, padx=10, pady=5)
e10 = Entry(frame1, width=10, textvariable=v10, validate="focusout", validatecommand=(testCMD, '%P'),
            invalidcommand=test_error)
e10.grid(row=1, column=4, padx=10, pady=5)
Label(frame1, text="（dBm）", justify=LEFT).grid(row=1, column=5, padx=10, pady=5)

v11 = StringVar()
Label(frame1, text="LTE天线高度", justify=LEFT).grid(row=2, column=3, padx=10, pady=5)
e11 = Entry(frame1, width=10, textvariable=v11, validate="focusout", validatecommand=(testCMD, '%P'),
            invalidcommand=test_error)
e11.grid(row=2, column=4, padx=10, pady=5)
Label(frame1, text="（m）", justify=LEFT).grid(row=2, column=5, padx=10, pady=5)

v12 = StringVar()
Label(frame1, text="LTE发射频率", justify=LEFT).grid(row=3, column=3, padx=10, pady=5)
e12 = Entry(frame1, width=10, textvariable=v12, validate="focusout", validatecommand=(testCMD, '%P'),
            invalidcommand=test_error)
e12.grid(row=3, column=4, padx=10, pady=5)
Label(frame1, text="（MHZ）", justify=LEFT).grid(row=3, column=5, padx=10, pady=5)

v13 = StringVar()
Label(frame1, text="LTE天线增益", justify=LEFT).grid(row=4, column=3, padx=10, pady=5)
e13 = Entry(frame1, width=10, textvariable=v13, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e13.grid(row=4, column=4, padx=10, pady=5)
Label(frame1, text="（dBi）", justify=LEFT).grid(row=4, column=5, padx=10, pady=5)

v14 = StringVar()
Label(frame1, text="LTE天线损耗因子", justify=LEFT).grid(row=5, column=3, padx=10, pady=5)
e14 = Entry(frame1, width=10, textvariable=v14, validate="focusout", validatecommand=(test1CMD, '%P'),
            invalidcommand=test1_error)
e14.grid(row=5, column=4, padx=10, pady=5)

v25 = StringVar()
Label(frame1, text="LTE噪声系数", justify=LEFT).grid(row=6, column=3, padx=10, pady=5)
e25 = Entry(frame1, width=10, textvariable=v25, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e25.grid(row=6, column=4, padx=10, pady=5)
Label(frame1, text="（dB）", justify=LEFT).grid(row=6, column=5, padx=10, pady=5)

v26 = StringVar()
Label(frame1, text="LTE馈线损耗", justify=LEFT).grid(row=7, column=3, padx=10, pady=5)
e26 = Entry(frame1, width=10, textvariable=v26, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e26.grid(row=7, column=4, padx=10, pady=5)
Label(frame1, text="（dB）", justify=LEFT).grid(row=7, column=5, padx=10, pady=5)

v4 = StringVar()
Label(frame1, text="lte带宽", justify=LEFT).grid(row=8, column=3, padx=10, pady=5)
SB = Scrollbar(frame1)  # 滑动条
SB.grid(row=8, column=4, padx=10, pady=5)
LB = Listbox(frame1, heigh=1, width=10, yscrollcommand=SB.set)  # 选择栏
LB.grid(row=8, column=5, padx=10, pady=5)
for item in ['5MHZ', '10MHZ', '15MHZ', '20MHZ']:
    LB.insert(END, item)
SB.config(command=LB.yview)


# 从选择栏得到选中带宽的序号
def get_bw_index():
    result = LB.curselection()
    pp = result[0]  # 得到选中的序号
    if pp == 0:
        return 5
    elif pp == 1:
        return 10
    elif pp == 2:
        return 15
    elif pp == 3:
        return 20


# 载入选中的带宽
def load_bw():
    result = float(get_bw_index())
    v4.set(str(result))


Button(frame1, text="载入lte带宽", command=load_bw).grid(row=9, column=4, padx=10, pady=5)


# 选取文件
def callback():
    dlg = win32ui.CreateFileDialog(1)
    dlg.DoModal()
    fileName = dlg.GetPathName()
    data = scio.loadmat(fileName)
    for key in data:
        if (key != '__globals__') and (key != '__header__') and (key != '__version__'):
            name = key
            break
    return data[name]


# 获取LTE方向图
def get_l_d_m():
    global lte_direction_factor
    lte_direction_factor = callback()


# 显示LTE垂直方向图
def show_l_d_m_y():
    lx1 = [0] * 181
    ly1 = [0] * 181
    for i in range(181):
        lx1[i] = i - 90
        ly1[i] = lte_direction_factor[i][180]
    plt.plot(lx1, ly1)
    plt.show()


# 显示LTE水平方向图
def show_l_d_m_x():
    lte_direction_factor_copy=resort120(lte_direction_factor, 1)
    lx2 = [0] * 360
    ly2 = [0] * 360
    for i in range(360):
        lx2[i] = i - 179
        ly2[i] = lte_direction_factor_copy[90][i]
    plt.plot(lx2, ly2)
    plt.show()


# RADAR部分
Label(frame1, text="RADAR参数部分-----", justify=LEFT).grid(row=10, column=3, padx=10, pady=5)

v15 = StringVar()
Label(frame1, text="RADAR高度", justify=LEFT).grid(row=11, column=3, padx=10, pady=5)
e15 = Entry(frame1, width=10, textvariable=v15, validate="focusout", validatecommand=(testCMD, '%P'),
            invalidcommand=test_error)
e15.grid(row=11, column=4, padx=10, pady=5)
Label(frame1, text="（m）", justify=LEFT).grid(row=11, column=5, padx=10, pady=5)

v16 = StringVar()
Label(frame1, text="RADAR天线增益", justify=LEFT).grid(row=12, column=3, padx=10, pady=5)
e16 = Entry(frame1, width=10, textvariable=v16, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e16.grid(row=12, column=4, padx=10, pady=5)
Label(frame1, text="（dBi）", justify=LEFT).grid(row=12, column=5, padx=10, pady=5)

v17 = StringVar()
Label(frame1, text="RADAR天线损耗因子", justify=LEFT).grid(row=13, column=3, padx=10, pady=5)
e17 = Entry(frame1, width=10, textvariable=v17, validate="focusout", validatecommand=(test1CMD, '%P'),
            invalidcommand=test1_error)
e17.grid(row=13, column=4, padx=10, pady=5)

v27 = StringVar()
Label(frame1, text="RADAR噪声系数", justify=LEFT).grid(row=14, column=3, padx=10, pady=5)
e27 = Entry(frame1, width=10, textvariable=v27, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e27.grid(row=14, column=4, padx=10, pady=5)
Label(frame1, text="（dB）", justify=LEFT).grid(row=14, column=5, padx=10, pady=5)

v28 = StringVar()
Label(frame1, text="RADAR馈线损耗", justify=LEFT).grid(row=15, column=3, padx=10, pady=5)
e28 = Entry(frame1, width=10, textvariable=v28, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e28.grid(row=15, column=4, padx=10, pady=5)
Label(frame1, text="（dB）", justify=LEFT).grid(row=15, column=5, padx=10, pady=5)

v21 = StringVar()
Label(frame1, text="RADAR带宽", justify=LEFT).grid(row=16, column=3, padx=10, pady=5)
e21 = Entry(frame1, width=10, textvariable=v21, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e21.grid(row=16, column=4, padx=10, pady=5)
Label(frame1, text="（MHZ）", justify=LEFT).grid(row=16, column=5, padx=10, pady=5)

v22 = StringVar()
Label(frame1, text="RADAR天线仰角", justify=LEFT).grid(row=17, column=3, padx=10, pady=5)
e22 = Entry(frame1, width=10, textvariable=v22, validate="focusout", validatecommand=(test2CMD, '%P'),
            invalidcommand=test2_error)
e22.grid(row=17, column=4, padx=10, pady=5)
Label(frame1, text="（度）", justify=LEFT).grid(row=17, column=5, padx=10, pady=5)


# 选取文件
def callback():
    dlg = win32ui.CreateFileDialog(1)
    dlg.DoModal()
    fileName = dlg.GetPathName()
    data = scio.loadmat(fileName)
    for key in data:
        if (key != '__globals__') and (key != '__header__') and (key != '__version__'):
            name = key
            break
    return data[name]


# 获取RADAR方向图
def get_r_d_m():
    global radar_direction_factor
    radar_direction_factor = callback()


# 显示RADAR垂直方向图
def show_r_d_m_y():
    rx1 = [0] * 181
    ry1 = [0] * 181
    for i in range(181):
        rx1[i] = i - 90
        ry1[i] = radar_direction_factor[i][180]
    plt.plot(rx1, ry1)
    plt.show()


# 显示RADAR水平方向图
def show_r_d_m_x():
    rx2 = [0] * 360
    ry2 = [0] * 360
    for i in range(360):
        rx2[i] = i - 179
        ry2[i] = radar_direction_factor[90][i]
    plt.plot(rx2, ry2)
    plt.show()


# 方向图部分
Label(frame1, text="方向图部分-----", justify=LEFT).grid(row=9, column=6, padx=10, pady=5)

Button(frame1, text="载入USER方向图", command=get_u_d_m).grid(row=10, column=6, padx=10, pady=5)
Button(frame1, text="显示USER垂直方向图", command=show_u_d_m_y).grid(row=10, column=7, padx=10, pady=5)
Button(frame1, text="显示USER水平方向图", command=show_u_d_m_x).grid(row=10, column=8, padx=10, pady=5)
Button(frame1, text="载入LTE方向图", command=get_l_d_m).grid(row=11, column=6, padx=10, pady=5)
Button(frame1, text="显示LTE垂直方向图", command=show_l_d_m_y).grid(row=11, column=7, padx=10, pady=5)
Button(frame1, text="显示LTE水平方向图", command=show_l_d_m_x).grid(row=11, column=8, padx=10, pady=5)
Button(frame1, text="载入RADAR方向图", command=get_r_d_m).grid(row=12, column=6, padx=10, pady=5)
Button(frame1, text="显示RADAR垂直方向图", command=show_r_d_m_y).grid(row=12, column=7, padx=10, pady=5)
Button(frame1, text="显示RADAR水平方向图", command=show_r_d_m_x).grid(row=12, column=8, padx=10, pady=5)

# 输出结果部分
Label(frame1, text="输出结果部分-----", justify=LEFT).grid(row=13, column=6, padx=10, pady=5)

v18 = StringVar()


# # 计算干扰概率
# def calcu_result():
#     result = calcu_probability(v5.get(), float(v1.get()), float(v2.get()), float(v3.get()), float(v10.get()),
#                                float(v11.get()),
#                                float(v12.get()),
#                                float(v6.get()),
#                                float(v7.get()), float(v4.get()), float(v15.get()), float(v13.get()), float(v8.get()),
#                                float(v16.get()), float(v14.get()), float(v9.get()), float(v17.get()), float(v21.get()),
#                                lte_direction_factor,
#                                user_direction_factor, radar_direction_factor, int(v19.get()), int(float(v20.get())),
#                                float(v22.get()), v23.get(), float(v24.get()), float(v26.get()), float(v28.get()),
#                                float(v25.get()), float(v29.get()), float(v27.get()), v30.get(), float(v36.get()),
#                                float(v35.get()), int(float(v37.get())))
#     v18.set(str(result))
#
#
# Button(frame2, text="计算干扰概率", justify=LEFT, command=calcu_result).grid(row=13, column=0, padx=10, pady=5)
# e18 = Entry(frame2, width=10, textvariable=v18, state="readonly").grid(row=13, column=1, padx=10, pady=5)


def system_main():
    result = exe_main(float(v31.get()), float(v32.get()), float(v33.get()), v5.get(), float(v1.get()), float(v2.get()),
                      float(v3.get()), float(v10.get()),
                      float(v11.get()),
                      float(v12.get()),
                      float(v6.get()),
                      float(v7.get()), float(v4.get()), float(v15.get()), float(v13.get()), float(v8.get()),
                      float(v16.get()), float(v14.get()), float(v9.get()), float(v17.get()), float(v21.get()),
                      lte_direction_factor,
                      user_direction_factor, radar_direction_factor, int(v19.get()), int(float(v20.get())),
                      float(v22.get()), v23.get(), float(v24.get()), float(v26.get()), float(v28.get()),
                      float(v25.get()), float(v29.get()), float(v27.get()), v30.get(), float(v36.get()),
                      float(v35.get()), int(float(v37.get())))
    v34.set(str(result))
    # 画坐标图部分
    acir_numbersx = int((float(v32.get()) - float(v31.get())) / float(v33.get()) + 1)  # 计算acir的个数
    acir_x = [0] * acir_numbersx  # 横坐标，表示acir
    probability_y = [0] * acir_numbersx  # 纵坐标，表示对应干扰概率
    for i in range(acir_numbersx):
        acir_x[i] = float(v31.get()) + i * float(v33.get())
    probability_y = result
    plt.plot(acir_x, probability_y)
    plt.show()


v34 = StringVar()
Button(frame1, text="计算结果并获取acir分析图", justify=LEFT, command=system_main).grid(row=14, column=6, padx=10, pady=5)
e34 = Entry(frame1, width=10, textvariable=v34, state="readonly").grid(row=14, column=7, padx=10, pady=5)


# 画出lte、user的分布图
# def call_paint():
#     final_paint(v5.get(), float(v1.get()), float(v2.get()), float(v3.get()), float(v4.get()), float(v24.get()))

def load():
    v1.set(str(1000))
    v2.set(str(120))
    v3.set(str(121))
    v7.set(str(3500))
    v6.set(str(1.5))
    v8.set(str(0))
    v9.set(str(0.9))
    v29.set(str(9))
    v10.set(str(43))
    v11.set(str(30))
    v12.set(str(3500))
    v13.set(str(15))
    v14.set(str(0.9))
    v25.set(str(5))
    v26.set(str(0))
    v15.set(str(8))
    v16.set(str(34))
    v17.set(str(0.9))
    v27.set(str(5))
    v28.set(str(0))
    v21.set(str(20))
    v22.set(str(0))
    v24.set(str(1))
    v31.set(str(6))
    v32.set(str(8))
    v33.set(str(0.4))
    v35.set(str(23))
    v36.set(str(0.8))
    v37.set(str(6))


# Button(frame2, text="获取LTE、USER分布图", justify=LEFT, command=call_paint).grid(row=15, column=1, padx=10, pady=5)
Button(frame1, text="载入", justify=LEFT, command=load).grid(row=15, column=6, padx=10, pady=5)
mainloop()
