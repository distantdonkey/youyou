#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import json
import pandas as pd
import datetime
import time
import math


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'referer':'https://creator.xiaohongshu.com/creator/home'
    }

cookies_dict = dict()
with open('15861805215.txt', 'r', encoding='utf8') as f:
    listCookies = json.loads(f.read())
    for cookie in listCookies:
        cookies_dict[cookie['name']] = cookie['value']
personal_info = requests.get(url='https://creator.xiaohongshu.com/api/galaxy/creator/home/personal_info', headers=headers, cookies=cookies_dict).json()
print(personal_info)
print(cookies_dict)
account_name = personal_info['data']['name']
print(personal_info)
print(account_name)