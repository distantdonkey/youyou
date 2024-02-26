#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_excel(r"C:\Users\宇\Desktop\H5活动日报.xlsx", sheet_name="表格0")
df['数据日期'] = pd.to_datetime(df['数据日期'], format='%Y%m%d')
df['开始日期'] = pd.to_datetime(df['开始日期'], format='%Y%m%d')
df['渠道ID'] = df['渠道ID'].replace('未知', '')

writer = pd.ExcelWriter(r'C:\Users\宇\Desktop\测试\h5活动日报.xlsx', engine='xlsxwriter', datetime_format='yyyy/m/d')

df.to_excel(writer, sheet_name='Sheet1', index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

writer.save()

