#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
from textwrap import fill


def laxin():
    # 中文及负数显示
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 创建画布
    fig, ax = plt.subplots(figsize=(14, 10), dpi=400)

    # mysql数据库连接配置
    con = pymysql.connect(
        host="10.11.24.182",
        port=3306,
        user='migu',  # 在这里输入用户名
        password='migu123',  # 在这里输入密码
        charset='utf8',
        database='migu'
    )

    # 读取sql文件并生成dateframe
    with open('./音乐T-2拉新.sql', encoding='utf-8') as f:
        laxin_sql = f.read()
    df = pd.read_sql(laxin_sql, con)

    # 人工限制plt.table的表格高度和换行的长度，从而实现自适应表格变换
    table_dict = {
        1: [100, 0.12],
        2: [50, 0.15],
        3: [21, 0.15],
        4: [15, 0.2],
        5: [12, 0.3],
        6: [8, 0.4],
        7: [7, 0.45],
        8: [6, 0.55]
    }

    # 柱状图
    plt.bar(df['专题名称(活动名称）'], df['覆盖量(万)'], width=0.4, color='#5B9BD5')
    # 给柱状图添加数据标签
    for a, b in zip(df['专题名称(活动名称）'], df['覆盖量(万)']):
        plt.text(a, b, round(b/10000, 1), ha='center', va='bottom', fontsize=16)
    plt.ylim(0, max(df['覆盖量(万)'])+50000)
    # 不显示坐标轴
    plt.axis('off')
    # 共享横坐标轴
    plt.twinx()

    # 折线图
    plt.plot(df['专题名称(活动名称）'], df['拉新率'], color='coral', marker='o', linewidth=3)

    # 给折线图添加数据标签
    for a, b in zip(df['专题名称(活动名称）'], df['拉新率']):
        plt.text(a, b, '{:.3%}'.format(b), ha='left', va='baseline', fontsize=16)
    plt.ylim(0)
    plt.axis('off')

    # 设置标题
    ax.set_title("音乐T-2各活动拉新效果", loc='center', fontweight='bold',  fontdict={'size': 25})

    plt.subplots_adjust(bottom=0.2)

    # table图表
    celltext = [df['覆盖量(万)'].map(lambda x: round(x/10000, 1)).values.tolist(),
                df['拉新率'].map(lambda x: '{:.3%}'.format(x)).values.tolist()]
    rowlabels = ['覆盖量(万)', '拉新率']
    cols = df['专题名称(活动名称）'].values.tolist()
    collabels = list(map(lambda x: fill(x, table_dict[len(df['专题名称(活动名称）'])][0]), cols))
    the_table = plt.table(cellText=celltext, cellLoc="center", rowLabels=rowlabels, colLabels=collabels,
                          rowLoc="center", colLoc="center", loc="bottom")

    # 设置单元格高度
    celldict = the_table.get_celld()
    for i in range(0, len(collabels)):
        celldict[(0, i)].set_height(table_dict[len(df['专题名称(活动名称）'])][1])
        for j in range(1, len(rowlabels) + 1):
            celldict[(j, i)].set_height(0.1)

    # 设置图表table中行名单元格的高度
    celldict[(1, -1)].set_height(0.1)
    celldict[(2, -1)].set_height(0.1)

    # 设置图表table单元格文本字体
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(16)

    # 设置图表table单元格边框
    for key, cell in the_table.get_celld().items():
        cell.set_linewidth(0.4)
        cell.set_text_props(multialignment='center', wrap=True)

    # 边框隐藏
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.tight_layout()

    plt.savefig("./拉新.jpg")

    print("拉新图已保存")

    # 返回最佳拉新相关字段
    best_laxin_name = df['专题名称(活动名称）'][0]
    best_laxin_rate = df['拉新率'][0]
    return best_laxin_name, best_laxin_rate