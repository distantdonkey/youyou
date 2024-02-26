# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
import pandas as pd
from datetime import datetime, timedelta
import calendar

now = datetime.now()
this_month_start = datetime(now.year, now.month, 1)
this_month_end = datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
yesterday = (now - timedelta(days=1)).strftime('%Y/%m/%d')
fppath = 'D:/0刘宇/日报/' + now.strftime('%m%d') + '/阅读数据表.xlsx'
# df = pd.read_excel(r"D:\0刘宇\日报\0308\阅读数据表.xlsx", sheet_name="pageid")
df = pd.read_excel(fppath, sheet_name="分类覆盖数")
# 当月累计活动数
print('当月H5累计活动数')
print(len(df.loc[(df['任务下发时间'] >= this_month_start) & (df['任务下发时间'] <= this_month_end)
            & (df['自制H5']=='自制H5'), ['page_id']]['page_id'].unique()))
# 昨日活动数
print('昨日H5活动数')
print(len(df.loc[(df['任务下发时间'] == yesterday) & (df['自制H5']=='自制H5'), ['page_id']]['page_id'].unique()))
print(yesterday,this_month_start,this_month_end)










