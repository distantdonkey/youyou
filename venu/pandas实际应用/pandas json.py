import pandas as pd
import json


# 使用 Python JSON 模块载入数据
with open(r'C:\Users\宇\Desktop\nested_list.json','r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)