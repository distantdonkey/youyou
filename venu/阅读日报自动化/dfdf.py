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

url = 'https://plus.migu.cn/c/0f4m9z'

response = requests.get(url, headers=headers)
urlstr = urllib.parse.unquote(response.url)
response2 = requests.get(urlstr, headers=headers)
urlstr2 = urllib.parse.unquote(response2.url)

# jump_url = re.search(r'.*?jump=(.*)', urlstr).group(1)
# r = requests.head(jump_url, headers=headers)
# result = r.headers.get('location')
# r = requests.get(jump_url, headers=headers)
# result = urllib.parse.unquote(r.url)
print(urlstr2)
