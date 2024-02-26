#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd


df = pd.read_excel(r"C:\Users\宇\Desktop\666.xlsx",sheet_name='Sheet1')
df["行标签"] = df["行标签"].str.split(',')
df=df.explode('行标签')
df=df.groupby('行标签').sum()
df.to_excel(r"C:\Users\宇\Desktop\est.xlsx")
print(df)