#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import re

#定义函数，提取客群中的标签名称，形成列表返回
def rule2namelist(a):
    return re.findall(r'\[.*?\]|65\+', a)

df = pd.read_excel(r"C:\Users\宇\Desktop\媒介.xlsx",sheet_name='Sheet1')
# df = df[['年龄段', '成功发送用户数', 'UV']]
# df['年龄段']=df['年龄段'].map(rule2namelist)
df=df.explode('媒介')
df=df.groupby('媒介').sum()
# df.sort_values(by=['年龄段'])
df.to_excel(r"C:\Users\宇\Desktop\est.xlsx")
print(df)