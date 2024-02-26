#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import re

def rule2namelist(a):
    return re.findall(r'{省份[=≠].*?}', a)

def rule2namelist2(a):
    return re.findall(r'{省份[=≠](.*?)}', a)

def len_sf(b):
    try:
        return len(b[0].split(','))
    except:
        return '空'


df = pd.read_excel(r"C:\Users\宇\Desktop\融合报表 -0718.xlsx", sheet_name="活动明细")
df = df[['子策划编码','目标群体']]
df['目标群体']=df['目标群体'].astype(str)
df['客群'] = df['目标群体'].map(rule2namelist)
df['省份'] = df['目标群体'].map(rule2namelist2)
df['数量'] = df['省份'].map(len_sf)

df.to_excel(r"C:\Users\宇\Desktop\123.xlsx")