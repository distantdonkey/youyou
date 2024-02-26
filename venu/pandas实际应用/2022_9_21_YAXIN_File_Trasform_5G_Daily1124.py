


# 用这个，不要用其他的5G


import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\admin\Desktop\5G指标监控日报.xlsx')

col_name = ['5G发送占比', '手机号码进端转化率_总计', '手机号码进端转化率_5G',
            '手机号码进端转化率_回落', '手机号码拉新转化率_总计', '手机号码拉新转化率_5G',
            '手机号码拉新转化率_回落', '新增用户日均次日留存率', '新增用户第三日留存率',
            '新增用户第七日留存率', '新增用户核心功能使用率']

for i in col_name:
    df['{}'.format(i)] = df['{}'.format(i)].str.rstrip('%').astype('float') / 100.0


df['数据日期'] = pd.to_datetime(df['数据日期'], format='%Y%m%d')
df['创建时间'] = pd.to_datetime(df['创建时间'], format='%Y%m%d')
df['开始时间'] = pd.to_datetime(df['开始时间'], format='%Y%m%d')
df['结束时间'] = pd.to_datetime(df['结束时间'], format='%Y%m%d')
df['ChatbotID'] = df['ChatbotID'].astype(str)
df['账户组id'] = df['账户组id'].astype(str)



writer = pd.ExcelWriter(r'C:\Users\admin\Desktop\5G指标监控报表-日.xlsx', engine='xlsxwriter',
                        datetime_format='yyyy/m/d')

df.to_excel(writer, sheet_name='Sheet1', index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

# number_format = workbook.add_format({'num_format': "0"})
percent_format = workbook.add_format({'num_format': "0.00%"})
# worksheet.set_column(13, 13, None, number_format)
# worksheet.set_column(15, 15, None, number_format)
# worksheet.set_column(16, 16, None, number_format)
# worksheet.set_column(17, 17, None, number_format)

worksheet.set_column(20, 20, None, percent_format)
worksheet.set_column(24, 24, None, percent_format)
worksheet.set_column(25, 25, None, percent_format)
worksheet.set_column(26, 26, None, percent_format)
worksheet.set_column(30, 30, None, percent_format)
worksheet.set_column(31, 31, None, percent_format)
worksheet.set_column(32, 32, None, percent_format)
worksheet.set_column(34, 34, None, percent_format)
worksheet.set_column(35, 35, None, percent_format)
worksheet.set_column(36, 36, None, percent_format)
worksheet.set_column(38, 38, None, percent_format)

writer.save()


print(df.dtypes)
print(df)