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

start_date = input('请输入开始日期(例2023-01-01)')
end_date = input('请输入结束日期(例2023-01-02)')
#读取并筛选出符合条件的
df = pd.read_excel(r"D:\0刘宇\日报\0323\阅读数据明细-自用.xlsx", sheet_name="明细表")
df = df.loc[(df['数据日期'] >= '2023/01/01') & ((df['渠道'] == "运营门户短信") | (df['渠道'] == "运营门户彩信")) & (df['是否智能推荐'] != '是'), ['数据日期','标签圈选用户群']]
#利用正则转化客群成名称列表
df['标签圈选用户群']=df['标签圈选用户群'].map(rule2namelist)
# 分组，合并标签名称列表为列表嵌套列表，并且通过自建函数再予以处理
df = df.groupby(df['数据日期']).agg(标签=('标签圈选用户群', lambda x : x.append([])))
df['标签']=df['标签'].map(list2platlist)
result = []
for x in df['标签'][start_date : end_date]:
    result.extend(x)
print(Counter(result).most_common())

