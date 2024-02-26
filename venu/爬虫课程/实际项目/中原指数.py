# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 13:19:45 2022

@author: 宇
"""

import requests
import re
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from lxml import etree

all_df = pd.DataFrame(columns=['标题','标题链接','图片名称','图片链接'])

def get_html_text(url):
    '''
    获取网页文本
    :param url: 网页链接or标题链接
    :return: r.text
    '''
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        return ""
    
def get_html_content(url):
    '''
    获取图片二进制文件
    :param url: 图片链接
    :return: r.content
    '''
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.content
    except:
        return ""
    
def judge_title_name(url):
    '''
    判断标题名称是否包含“中农立华原药价格指数”
    :param url: 网页链接
    :return: True/False(if条件判断是否下载标题链接文本)
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    match = re.match(r'中农立华原药价格指数', soup.title.string)
    if match:
        return True
    else:
        return False
    
def get_title_list(pageurl):
    '''
    标题链接页面采集，获取标题和标题链接
    :param pageurl: 页面链接
    :return: None
    '''
    html = re.findall(r'<div class="newslist mt30">.*?</div>', get_html_text(pageurl), re.S)
    soup = BeautifulSoup(html[0], "html.parser")
    li_list = soup.find_all("li")
    for li in li_list:
        title_url = "http://www.sino-agri-sal.com/" + li.a.attrs["href"]
        title = li.a.string
        get_imgurl_list(title,title_url)

def get_imgurl_list(title, title_url):
    '''
    根据详情页链接，解析所需页面数据，保存到全局变量all_df
    :title: 标题名称
    :title_url 标题链接
    :return: None
    '''
    if judge_title_name(url):
        html = re.findall(r'<h3>中农立华原药价格指数.*?</h3>.*?<li>上一篇', gethtmltext(titleurl), re.S)
        soup = BeautifulSoup(html[0], "html.parser")
        a = soup.find_all("img")
        for i in a:
            if i.attrs["src"][-3:] == "jpg":
                lst.append("http://www.sino-agri-sal.com"+i.attrs["src"])
        return lst

def main():
    pageurls=[
        "http://www.sino-agri-sal.com/pnlist.php?cid=28&page=1",
        "http://www.sino-agri-sal.com/pnlist.php?cid=28&page=2",
        "http://www.sino-agri-sal.com/pnlist.php?cid=28&page=3",
        "http://www.sino-agri-sal.com/pnlist.php?cid=28&page=4",
        "http://www.sino-agri-sal.com/pnlist.php?cid=28&page=5",
    ]
    titlelists = []
    imglists = []
    for pageurl in pageurls:
        gettitlelist(titlelists, pageurl)
    for titlelist in titlelists:
        getimgurllist(imglists, titlelist)
    for img in imglists:
        with open("C://Users//宇//Desktop//aaa//"+img.split('/')[-1], 'wb') as f:
            f.write(gethtmlcontent(img))
            f.close()
        
get_title_list("http://www.sino-agri-sal.com/pnlist.php?cid=28&page=1")