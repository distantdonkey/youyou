#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
import urllib
from urllib import parse
import pandas as pd
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}


def get_pageid_text(url):
    response = requests.head(url, headers=headers)
    urlstr = response.headers.get('location')
    if re.search('page_id=(\d+)', urlstr):
        result = re.search('page_id=(\d+)', urlstr).group(1)
    else:
        result = "无编码"
    return result


def get_jumpstr_text(url):
    response = requests.get(url, headers=headers)
    urlstr = urllib.parse.unquote(response.url)
    if re.search('https://plus.migu.cn/c/(.{6})', urlstr):
        result = re.search('https://plus.migu.cn/c/(.{6})', urlstr).group(0)
    else:
        result = "无编码"
    return result


def get_assighNo_text(url):
    response = requests.get(url, headers=headers)
    urlstr = urllib.parse.unquote(response.url)
    if re.search('assignNo=(\d+)', urlstr):
        result = re.search('assignNo=(\d+)', urlstr).group(1)
    else:
        result = "无编码"
    return result


df = pd.read_excel(r"C:\Users\宇\Desktop\子策划页面id.xlsx")


for url in df['URL']:
    if get_jumpstr_text(url) == '无编码':
        page_id = get_assighNo_text(url)
    else:
        page_id = get_pageid_text(get_jumpstr_text(url))
    print(page_id)

