import pandas as pd
import numpy as np

df = pd.read_excel(r'D:\亚信\7入数据库\源表\基于MGBA指标数据累计报表.xlsx')
df2 = pd.read_excel(r'D:\亚信\7入数据库\参照表\基于MGBA指标数据累计报表参照.xlsx')


df['手机号码累计进端转化率'] = df['手机号码累计进端转化率'].str.rstrip('%').astype('float') / 100.0
df['手机号码累计拉新转化率'] = df['手机号码累计拉新转化率'].str.rstrip('%').astype('float') / 100.0
#df['手机号码进端新增用户日均次日留存率'] = df['手机号码进端新增用户日均次日留存率'].str.rstrip('%').astype('float') / 100.0
#df['手机号码进端新增用户日均第3日留存率'] = df['手机号码进端新增用户日均第3日留存率'].str.rstrip('%').astype('float') / 100.0


df['手机号码进端新增用户日均第7日留存率'] = None
df['手机号码新增用户核心功能累计使用次数'] = None

cols = df2.columns.tolist()
df = df[cols]
df['数据日期'] = pd.to_datetime(df['数据日期'], format='%Y%m%d')
df['任务开始时间'] = pd.to_datetime(df['任务开始时间'], format='%Y%m%d')
df['任务结束时间'] = pd.to_datetime(df['任务结束时间'], format='%Y%m%d')
df['任务创建时间'] = pd.to_datetime(df['任务创建时间'], format='%Y%m%d')


df['运营位ID'] = df['运营位ID'].astype(str)
df['去重规则'] = df['去重规则'].astype(str)
df['账户组id'] = df['账户组id'].astype(str)
df = df.drop_duplicates(subset=['数据日期', '子策划编码']) 

writer = pd.ExcelWriter(r'D:\亚信\7入数据库\结果表\基于MGBA指标数据累计报表.xlsx', engine='xlsxwriter',
                        datetime_format='yyyy/m/d')

df.to_excel(writer, sheet_name='Sheet1', index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

percent_format = workbook.add_format({'num_format': "0.00%"})
worksheet.set_column(15, 15, None, percent_format)
worksheet.set_column(17, 17, None, percent_format)
#worksheet.set_column(30, 30, None, percent_format)
#worksheet.set_column(31, 31, None, percent_format)

writer.close()


print(df.dtypes)
print(df)