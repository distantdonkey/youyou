import pandas as pd
import numpy as np
import re

df = pd.read_excel(r'D:\亚信\7入数据库\源表\触点页面数据.xlsx')

df['数据日期'] = pd.to_datetime(df['数据日期'], format='%Y%m%d')

list = ['amber页面进端转化率', 'amber页面拉新转化率', '页面进端转化率', '页面拉新转化率']
for i in list:
    df['{}'.format(i)] = df['{}'.format(i)].str.rstrip('%').astype('float') / 100.0

writer = pd.ExcelWriter(r'D:\亚信\7入数据库\结果表\触点页面数据.xlsx', engine='xlsxwriter',
                        datetime_format='yyyy/m/d')

df.to_excel(writer, sheet_name='Sheet1', index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

percent_format = workbook.add_format({'num_format': "0.00%"})

worksheet.set_column(10, 10, None, percent_format)
worksheet.set_column(12, 12, None, percent_format)
worksheet.set_column(21, 21, None, percent_format)
worksheet.set_column(23, 23, None, percent_format)
writer.close()


print(df.dtypes)
print(df)