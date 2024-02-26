#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import re

def rule2namelist(a):
    return re.findall(r'{(.*?)[=≠].*?}', a)

df = pd.read_excel(r"D:\0刘宇\阅读需求\0509-0611单标签客群拉新分析.xlsx", sheet_name="活动明细单标签")
df = df[['任务下发时间','子策划编码','标签圈选用户群','成功发送用户数','拉新量']]
df['标签圈选用户群']=df['标签圈选用户群'].map(rule2namelist)
delete = ['运营商归属','省份', '免打扰用户', '低价值用户标签', '沉默用户标签', '阅读营销短信黑名单','防沉迷过滤', '7天已触达',
          '最后活跃日期']
df['标签圈选用户群']=df['标签圈选用户群'].map(lambda x: set(x)-set(delete))
df.to_excel(r"C:\Users\宇\Desktop\单标签.xlsx")
print(df['标签圈选用户群'])
