# -*- coding: utf-8 -*-
from tkinter import *
from User_Generation import *



##将下标为num的六边形的6个顶点连在一起
def paint_vertex(num,down_scale,plotting_scale,w):
    # 将六边形右顶点从左上角移到画布中心
    lte[num].vertex_x_right += down_scale
    lte[num].vertex_y_right += down_scale
    # 将六边形右上顶点从左上角移到画布中心
    lte[num].vertex_x_rightup += down_scale
    lte[num].vertex_y_rightup += down_scale
    # 将六边形左上顶点从左上角移到画布中心
    lte[num].vertex_x_leftup += down_scale
    lte[num].vertex_y_leftup += down_scale
    # 将六边形左顶点从左上角移到画布中心
    lte[num].vertex_x_left += down_scale
    lte[num].vertex_y_left += down_scale
    # 将六边形左下顶点从左上角移到画布中心
    lte[num].vertex_x_leftdown += down_scale
    lte[num].vertex_y_leftdown += down_scale
    # 将六边形右下顶点从左上角移到画布中心
    lte[num].vertex_x_rightdown += down_scale
    lte[num].vertex_y_rightdown += down_scale
    # 将右顶点与右上顶点连在一起
    w.create_line(lte[num].vertex_x_right * plotting_scale, lte[num].vertex_y_right * plotting_scale,
                  lte[num].vertex_x_rightup * plotting_scale,
                  lte[num].vertex_y_rightup * plotting_scale, fill="black")
    # 将右上顶点与左上顶点连在一起
    w.create_line(lte[num].vertex_x_rightup * plotting_scale, lte[num].vertex_y_rightup * plotting_scale,
                  lte[num].vertex_x_leftup * plotting_scale,
                  lte[num].vertex_y_leftup * plotting_scale, fill="black")
    # 将左上顶点与左顶点连在一起
    w.create_line(lte[num].vertex_x_leftup * plotting_scale, lte[num].vertex_y_leftup * plotting_scale,
                  lte[num].vertex_x_left * plotting_scale,
                  lte[num].vertex_y_left * plotting_scale, fill="black")
    # 将左顶点与左下顶点连在一起
    w.create_line(lte[num].vertex_x_left * plotting_scale, lte[num].vertex_y_left * plotting_scale,
                  lte[num].vertex_x_leftdown * plotting_scale,
                  lte[num].vertex_y_leftdown * plotting_scale, fill="black")
    # 将左下顶点与右下顶点连在一起
    w.create_line(lte[num].vertex_x_leftdown * plotting_scale, lte[num].vertex_y_leftdown * plotting_scale,
                  lte[num].vertex_x_rightdown * plotting_scale,
                  lte[num].vertex_y_rightdown * plotting_scale, fill="black")
    # 将右下顶点与右顶点连在一起
    w.create_line(lte[num].vertex_x_rightdown * plotting_scale, lte[num].vertex_y_rightdown * plotting_scale,
                  lte[num].vertex_x_right * plotting_scale,
                  lte[num].vertex_y_right * plotting_scale, fill="black")


def paint_center(num,hexagon_length,down_scale,plotting_scale,w):  ##将下标为num的基站位置标注
    # 将六边形中心从左上角移到画布中心
    lte[num].x += down_scale
    lte[num].y += down_scale
    # 画出小正方形标注基站
    w.create_rectangle(lte[num].x * plotting_scale - hexagon_length * 0.1 * plotting_scale,
                       lte[num].y * plotting_scale - hexagon_length * 0.1 * plotting_scale,
                       lte[num].x * plotting_scale + hexagon_length * 0.1 * plotting_scale,
                       lte[num].y * plotting_scale + hexagon_length * 0.1 * plotting_scale, fill="blue")


def paint_user(num,hexagon_length,down_scale,plotting_scale,w):  ##将下标为num的user位置标注
    # 将六边形中心从左上角移到画布中心
    user[num].x += down_scale
    user[num].y += down_scale
    # 画出小正方形标注基站
    w.create_rectangle(user[num].x * plotting_scale - hexagon_length * 0.01 * plotting_scale,
                       user[num].y * plotting_scale - hexagon_length * 0.01 * plotting_scale,
                       user[num].x * plotting_scale + hexagon_length * 0.01* plotting_scale,
                       user[num].y * plotting_scale + hexagon_length * 0.01* plotting_scale, fill="red")


# 画图汇总函数
def paint(hexagon_length,legal_lte_numbers,user_numbers):
    root1 = Tk()  ##创建窗口
    w = Canvas(root1, width=1500, height=1000)  ##生成画图区域
    w.pack()
    plotting_scale = 2 / hexagon_length  # 关于六边形大小比例尺
    down_scale = 80  # 关于六边形整体平移位置比例尺
    acquire_coordinate(legal_lte_numbers,hexagon_length)  # 获取筛选后基站的顶点坐标
    for i in range(legal_lte_numbers):
        paint_vertex(i,down_scale,plotting_scale,w)  # 画边
        paint_center(i,hexagon_length,down_scale,plotting_scale,w)  # 画中心点
    for i in range(user_numbers):
        paint_user(i,hexagon_length,down_scale,plotting_scale,w)  # 画user
    mainloop()
