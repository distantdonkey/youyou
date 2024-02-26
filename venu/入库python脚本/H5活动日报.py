#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_excel(r"D:\亚信\7入数据库\源表\H5活动日报.xlsx", sheet_name="表格0")
df['数据日期'] = pd.to_datetime(df['数据日期'], format='%Y%m%d')
df['开始日期'] = pd.to_datetime(df['开始日期'], format='%Y%m%d')
df['渠道ID'] = df['渠道ID'].replace('未知', '')

writer = pd.ExcelWriter(r'D:\亚信\7入数据库\结果表\h5活动日报.xlsx', engine='xlsxwriter', datetime_format='yyyy/m/d')

df.to_excel(writer, sheet_name='Sheet1', index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

writer.save()