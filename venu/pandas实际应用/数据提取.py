#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import re

def rule2namelist(a):
    if a is np.NaN:
        return np.NaN
    else:
        return re.findall(r'{[^{}]*?在订.*?}|{[^{}]*?5G畅玩包库.*?}|{[^{}]*?会员.*?}', a)

df = pd.read_excel(r"C:\Users\宇\Desktop\数据提取.xlsx")
df = df[['举报时间','下发时间','客群规则']]
df['关键'] = df['客群规则'].apply(rule2namelist)
df.to_excel(r"C:\Users\宇\Desktop\kkkkk.xlsx")

