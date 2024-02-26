#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os
import re
import pandas as pd

# 爬取所有文章的标题和连接信息，形成df
title_df = pd.DataFrame(columns=['标题', '标题链接', '发布日期'])
url = 'http://www.sino-agri-sal.com/pnlist.php?cid=28&page=%d'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
for i in range(1, 9):
    new_url = url % i
    page_text = requests.get(url=new_url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="newslist mt30"]/li')
    for li in li_list:
        title_url = 'http://www.sino-agri-sal.com/' + li.xpath('./a/@href')[0]
        title = li.xpath('./a/text()')[0]
        date = li.xpath('./i/text()')[0]
        title_df.loc[len(title_df)] = [title, title_url, date]
title_df =  title_df[title_df['标题'].str.contains('中农立华原药价格指数')]
title_df.to_excel(r"C:\Users\宇\Desktop\中农立华原药价格指数.xlsx", index=False)
