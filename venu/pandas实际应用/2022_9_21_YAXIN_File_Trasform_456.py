import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\admin\Desktop\运营指标监控报表.xlsx')
df2 = pd.read_excel(r'D:\资料\亚信\作业\冬奥\日\456.xlsx')

df['手机号码进端转化率'] = df['手机号码进端转化率'].str.rstrip('%').astype('float') / 100.0
df['手机号码拉新转化率'] = df['手机号码拉新转化率'].str.rstrip('%').astype('float') / 100.0
df['次日留存率'] = df['次日留存率'].str.rstrip('%').astype('float') / 100.0
df['第3日留存率'] = df['第3日留存率'].str.rstrip('%').astype('float') / 100.0

df = df.rename(columns={'去重后人群数量': '去重后人群数量(最大值)', '发送成功用户数': '发送成功用户数(最大值)',
                        '手机号码进端量': '日累计手机号码进端量',
                        '手机号码拉新量': '日累计手机号码拉新量',
                        '次日留存率':'手机号码进端新增用户次日留存率',
                        '第3日留存率': '手机号码进端新增用户日均第3日留存率',
                        '核心功能平均使用时长': '手机号码进端新增用户核心功能人均单日使用时长（s）',
                        '核心功能使用用户数': '手机号码进端新增用户核心功能使用用户数',
                        '新增用户订购用户数': '手机号码进端新增用户订购用户数',
                        '新增用户付费金额(元)': '手机号码进端新增用户付费金额(元)'
                        })

df['手机号码进端新增用户日均第7日留存率'] = None
df['手机号码进端新增用户核心功能使用次数'] = None

cols = df2.columns.tolist()
df = df[cols]
df['数据日期'] = pd.to_datetime(df['数据日期'], format='%Y%m%d')
df['任务开始时间'] = pd.to_datetime(df['任务开始时间'], format='%Y%m%d')
df['任务结束时间'] = pd.to_datetime(df['任务结束时间'], format='%Y%m%d')
df['任务创建时间'] = pd.to_datetime(df['任务创建时间'], format='%Y%m%d')

df['页面URL(短链)'] = df['页面URL(短链)'].astype(str)
df['触点ID'] = df['触点ID'].astype(str)
df['运营位ID'] = df['运营位ID'].astype(str)
df['去重规则'] = df['去重规则'].astype(str)
df['账户组id'] = df['账户组id'].astype(str)


writer = pd.ExcelWriter(r'C:\Users\admin\Desktop\456.xlsx', engine='xlsxwriter',
                        datetime_format='yyyy/m/d', options={'strings_to_urls': False})

df.to_excel(writer, sheet_name='Sheet1', index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

percent_format = workbook.add_format({'num_format': "0.00%"})
worksheet.set_column(28, 28, None, percent_format)
worksheet.set_column(30, 30, None, percent_format)
worksheet.set_column(31, 31, None, percent_format)
worksheet.set_column(32, 32, None, percent_format)

writer.save()


print(df.dtypes)
print(df)