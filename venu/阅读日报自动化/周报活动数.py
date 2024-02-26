#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
from datetime import datetime, timedelta
import calendar

now = datetime.now()
# 当月第一天
this_month_start = (datetime(now.year, now.month, 1)).strftime('%Y/%m/%d')
# 上周四
last_thur = (now - timedelta(days=now.weekday() + 4)).strftime('%Y/%m/%d')
# 本周三
this_wed = (now + timedelta(days=6 - now.weekday() - 4)).strftime('%Y/%m/%d')
# 7月1日
seven_one = (datetime(now.year, 7, 1)).strftime('%Y/%m/%d')

# 读取文件
fppath = 'D:/0刘宇/日报/' + now.strftime('%m%d') + '/阅读数据表.xlsx'
df = pd.read_excel(fppath, sheet_name="分类覆盖数")
print('月累计活动数')
print(len(df.loc[(df['任务下发时间'] >= this_month_start) & (df['任务下发时间'] <= this_wed), ['page_id']]['page_id'].unique()))
print('周活动数')
print(len(df.loc[(df['任务下发时间'] >= last_thur) & (df['任务下发时间'] <= this_wed), ['page_id']]['page_id'].unique()))
print('周智能推荐活动数')
print(len(df.loc[(df['任务下发时间'] >= last_thur) & (df['任务下发时间'] <= this_wed) & (df['智能推荐'] == '是'), ['page_id']][
              'page_id'].unique()))
print('四赛五全活动数')
print(len(df.loc[(df['任务下发时间'] >= seven_one) & (df['重点IP'].isin(['四赛', '常规体育', '日常', '暑期中秋', '亚运'])), ['page_id']][
              'page_id'].unique()))
print('四赛活动数')
print(len(df.loc[(df['任务下发时间'] >= seven_one) & (df['重点IP'] == '四赛'), ['page_id']]['page_id'].unique()))
print('常规亚运活动数')
print(len(df.loc[(df['任务下发时间'] >= seven_one) & (df['重点IP'] == '亚运'), ['page_id']]['page_id'].unique()))
print('常规文娱活动数')
print(len(df.loc[(df['任务下发时间'] >= seven_one) & (df['重点IP'] == '日常'), ['page_id']]['page_id'].unique()))
print('暑期中秋')
print(len(df.loc[(df['任务下发时间'] >= seven_one) & (df['重点IP'] == '暑期中秋'), ['page_id']]['page_id'].unique()))
