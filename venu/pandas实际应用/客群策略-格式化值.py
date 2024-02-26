#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd

def resort_str(str):
    list = str.split(';')
    list.sort()
    my_string = ';'.join(list)
    return my_string

df = pd.read_excel(r"D:\0刘宇\日报\0814\阅读数据明细-自用.xlsx", sheet_name="日活动汇总")
df = df.loc[df['客群策略'].notnull(),['子策划编码','客群策略']]
df['客群策略'] = df['客群策略'].apply(resort_str)
df['子策划编码'].astype(str)
df['客群策略'].astype(str)
df.to_csv(r"C:\Users\宇\Desktop\客群策略格式化值.csv",index=False,encoding='utf-8_sig')