#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_excel(r"C:\Users\宇\Desktop\短彩信日报.xlsx", sheet_name="表格0")
df['数据日期'] = pd.to_datetime(df['数据日期'], format='%Y%m%d')
df['任务开始日期'] = pd.to_datetime(df['任务开始日期'], format='%Y%m%d')
df['新增用户数'] = df['新增用户数(非会员)'] + df['新增用户数(会员)']
df['触达发展用户数'] = df['发展用户数(会员)'] + df['新增用户数(非会员)']
df.rename(columns={'新增用户数(非会员)': '非会员新增用户数', '新增用户数(会员)': '会员新增用户', '发展用户数(会员)': '会员发展用户数'}, inplace = True)
writer = pd.ExcelWriter(r'C:\Users\宇\Desktop\用户运营中心短彩信明细数据.xlsx', engine='xlsxwriter', datetime_format='yyyy/m/d')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

