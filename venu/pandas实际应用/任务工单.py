import pandas as pd
import re

def province(x):
    try:
        return re.search(r'{省份[=≠].*?}', x).group(0)
    except:
        return None

def gender(x):
    try:
        return re.search(r'{性别[=≠].*?}', x).group(0)
    except:
        return None

def age(x):
    try:
        return re.search(r'{年龄[=≠].*?}', x).group(0)
    except:
        return None

df = pd.read_excel(r'C:\Users\宇\Desktop\任务工单(2023-07-28).xlsx')
df = df.drop(columns='客群规则.1')
df.rename(columns={"PUSH语&链接地址": "PUSH语链接地址"}, inplace=True)
df['省份'] = df['客群规则'].apply(province)
df['性别'] = df['客群规则'].apply(gender)
df['年龄'] = df['客群规则'].apply(age)
df.to_excel(r'C:\Users\宇\Desktop\任务工单.xlsx', sheet_name='任务工单', index=False)