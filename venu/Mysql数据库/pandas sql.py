#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd
import pymysql

con = pymysql.connect(
    host="10.11.24.182",
    port=3306,
    user='migu',    #在这里输入用户名
    password='migu123',     #在这里输入密码
    charset='utf8',
    database='migu'
    )
with open('./ceshi.sql',encoding='utf-8') as f:
    c = f.read()
# sql_cmd = "select 页面ID,渠道ID from 触点页面报表 limit 20;"

#
df = pd.read_sql(c, con)
print(df)