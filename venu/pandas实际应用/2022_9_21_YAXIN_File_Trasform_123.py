import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\宇\Desktop\运营分析报表.xlsx')  #压缩文件
df2 = pd.read_excel(r'C:\Users\宇\Desktop\1111.xlsx')   #123，只需要行名
df = df.rename(columns={'去重后人群数量': '去重后人群数量(最大值)', '发送成功用户数': '发送成功用户数(最大值)', 'PV': '页面访问量（PV）',
                        'UV': '页面访问用户数（UV）'})

df['页面按钮点击PV'] = None
df['页面按钮点击UV'] = None
df['拉端按钮点击PV'] = None
df['拉端按钮点击UV'] = None
df['页面视频播放量'] = None
df['页面音乐播放量'] = None
df['页面进端量'] = None
df['页面进端转化率'] = None
df['页面拉新量'] = None
df['页面拉新转化率'] = None
df['一人一码手机号码获取数量'] = None
df['一人一码页面进端量'] = None
df['一人一码页面进端转化率'] = None
df['一人一码页面拉新量'] = None
df['一人一码页面拉新转换率'] = None

cols = df2.columns.tolist()
df = df[cols]
df['数据日期'] = pd.to_datetime(df['数据日期'], format='%Y%m%d')
df['任务开始时间'] = pd.to_datetime(df['任务开始时间'], format='%Y%m%d')
df['任务结束时间'] = pd.to_datetime(df['任务结束时间'], format='%Y%m%d')
df['任务创建时间'] = pd.to_datetime(df['任务创建时间'], format='%Y%m%d')

df['amber页面进端转化率'] = df['amber页面进端转化率'].str.rstrip('%').astype('float') / 100.0
df['amber页面拉新转化率'] = df['amber页面拉新转化率'].str.rstrip('%').astype('float') / 100.0

df['触点ID'] = df['触点ID'].astype(str)
df['运营位编码'] = df['运营位编码'].astype(str)
df['去重规则'] = df['去重规则'].astype(str)
df['账户组id'] = df['账户组id'].astype(str)


writer = pd.ExcelWriter(r'C:\Users\宇\Desktop\est.xlsx', engine='xlsxwriter',
                        datetime_format='yyyy/m/d', options={'strings_to_urls': False})        #输出路径

df.to_excel(writer, sheet_name='Sheet1', index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

percent_format = workbook.add_format({'num_format': "0.00%"})
worksheet.set_column(30, 30, None, percent_format)
worksheet.set_column(32, 32, None, percent_format)

writer.close()


print(df.dtypes)
print(df)