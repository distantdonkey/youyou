#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import re
from collections import Counter

#定义函数，提取客群中的标签名称，形成列表返回
def rule2namelist(a):
    return re.findall(r'{(.*?)[=≠].*?}', a)

#定义函数，列表嵌套列表转成一个列表
def list2platlist(l):
    return [item for sublist in l for item in sublist]

# start_date = input('请输入开始日期(例2023-01-01)')
# end_date = input('请输入结束日期(例2023-01-02)')
#读取并筛选出符合条件的
df = pd.read_excel(r"C:\Users\宇\Desktop\拆分.xlsx", sheet_name="Sheet2")
#利用正则转化客群成名称列表
df['标签圈选用户群']=df['标签圈选用户群'].map(rule2namelist)
result = []
for i in df['标签圈选用户群']:
    for k in i:
        result.append(k)
for x in Counter(result).most_common():
    print(x)



# print(Counter(df['标签圈选用户群']).most_common())