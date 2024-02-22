#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import pandas as pd
import datetime
import time
import math

def get_cookies_dict(fp):
    """返回不同账号对应的cookies字典"""
    cookies_dict = dict()
    with open(fp, 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
        for cookie in listCookies:
            cookies_dict[cookie['name']] = cookie['value']
    return cookies_dict

def get_notes_json(url,cookies_dict):
    """返回笔记数据的json"""
    notes_json = requests.get(url=url, headers=headers, cookies=cookies_dict).json()
    return notes_json

def get_max_page(cookies_dict):
    """返回笔记数据的最大页码"""
    url = 'https://creator.xiaohongshu.com/api/galaxy/creator/data/note_stats/new?page=1&page_size=48&sort_by=time&note_type=2&time=30&is_recent=false'
    notes_json = requests.get(url=url, headers=headers, cookies=cookies_dict).json()
    return math.ceil(notes_json['data']['total']/48)

def get_account_name(cookies_dict):
    """获取账号名称"""
    personal_info = requests.get(url='https://creator.xiaohongshu.com/api/galaxy/creator/home/personal_info', headers=headers, cookies=cookies_dict).json()
    account_name = personal_info['data']['name']
    return personal_info,account_name

#账号cookies文件列表
filenames = [
    # '19201838394.txt',      # 小空电竞
    # '19201809318.txt'     # 嗑老师在线
    # '19201895220.txt',      # 咕咕篮球      #该账号无人均观看时长及直接涨粉数据
    # '19201835272.txt',      # 科技观测君
    # '19201852067.txt',      # 掼蛋小辣椒
    # '19201867172.txt'       # 大咪也看球
    '15861805215.txt'
]

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'referer':'https://creator.xiaohongshu.com/creator/home'
    }

name_list=[]
title_list=[]
publish_time_list=[]
watch_list=[]
watch_time_list=[]
like_list=[]
collect_list=[]
comment_list=[]
barrage_list=[]
share_list=[]
powder_raise_list=[]

for fp in filenames:
    cookies_dict = get_cookies_dict(fp)
    account_name = get_account_name(cookies_dict)
    max_page = get_max_page(cookies_dict)
    for page in range(1, max_page+1):
        page_url = 'https://creator.xiaohongshu.com/api/galaxy/creator/data/note_stats/new?page=%d&page_size=48&sort_by=time&note_type=2&time=30&is_recent=false'
        notes_json = get_notes_json(page_url%page, cookies_dict)
        for note in notes_json['data']['note_infos']:
            name_list.append(account_name)
            title_list.append(note['title'])
            publish_time_list.append(time.strftime('%Y-%m-%d', time.localtime(note['post_time']/1000)))
            watch_list.append(note['read'])
            watch_time_list.append(note['view_time_avg'])
            like_list.append(note['like'])
            collect_list.append(note['fav'])
            comment_list.append(note['comment'])
            barrage_list.append(note['danmaku_count'])
            share_list.append(note['share'])
            powder_raise_list.append(note['follow'])

df = pd.DataFrame({
    '账号名称':name_list,
    '视频标题':title_list,
    '发布时间':publish_time_list,
    '观看量':watch_list,
    '人均观看时长':watch_time_list,
    '点赞量':like_list,
    '收藏数':collect_list,
    '评论数':comment_list,
    '弹幕数':barrage_list,
    '分享数':share_list,
    '直接涨粉数':powder_raise_list})

#添加“数据日期”列
yesterday = datetime.datetime.now()
yesterday_str = yesterday.strftime("%Y-%m-%d")
df.insert(loc=0, column='数据日期', value=yesterday_str)
#添加“平台名称”列
df.insert(loc=1, column='平台名称', value='小红书')

df.to_excel(r"C:\Users\宇\Desktop\小红书.xlsx",index=False)