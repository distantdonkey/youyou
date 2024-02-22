#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://creator.xiaohongshu.com/')
with open('15861805215.txt', 'r', encoding='utf8') as f:
    listCookies = json.loads(f.read())
    for cookie in listCookies:
        cookie_dict = {
            'domain': '.xiaohongshu.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expiry": cookie.get('expiry'),
            'path': '/',
            'httpOnly': cookie.get('httpOnly'),
            'secure': cookie.get('secure')
        }
        driver.add_cookie(cookie_dict)
time.sleep(3)
driver.refresh()
time.sleep(6)
# driver.find_element(By.XPATH, '//*[@id="page"]/div/main/div[1]/div/div[2]/div/div[6]/div/div').click()
# time.sleep(6)
# # 获取账户名称
# max_page_text = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div[1]/div').text
# max_page_text_obj = re.search(r'，.*?(\d+).*?页', max_page_text)
# max_page = max_page_text_obj.group(1)
# time.sleep(3)
# print(max_page_text)
# print(max_page_text_obj)
# print(max_page)
