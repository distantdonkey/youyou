from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
import datetime
import json
import html

def str2int_wan(str):
    if str[-1] == '万':
        return int(float(str[0:-1]) * 10000)
    else:
        return int(str)

def smin2int(str):
    if str[-3:] == 'min':
        return int(str[:-3]) * 60
    else:
        return int(str[:-1])

#建立最终输出的excel模板
all_df = pd.DataFrame(columns=['账号名称', '视频标题', '发布时间', '观看量', '人均观看时长', '点赞量', '收藏数', '评论数', '弹幕数', '分享数', '直接涨粉数'])
#账号cookies文件列表
filenames = [
    # '19201838394.txt',      # 小空电竞
    '19201809318.txt',      # 嗑老师在线
    # '19201895220.txt',      # 咕咕篮球      #该账号无人均观看时长及直接涨粉数据
    # '19201835272.txt',      # 科技观测君
    # '19201852067.txt',      # 掼蛋小辣椒
    # '19201867172.txt'       # 大咪也看球
]

#实现用户登录并跳转笔记数据页面
for filename in filenames:
    driver = webdriver.Chrome()
    # 设置全局隐性等待时间，单位秒, 如查找元素时
    driver.implicitly_wait(50)
    driver.get('https://creator.xiaohongshu.com/')
    time.sleep(5)
    with open(filename, 'r', encoding='utf8') as f:
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
    time.sleep(5)

    #点击"笔记数据"
    driver.find_element(By.XPATH, '//*[@id="page"]/div/main/div[1]/div/div[2]/div/div[6]/div/div').click()
    # time.sleep(15)
    # 获取账户名称
    account_name = driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div[2]/div/span').text
    #点击“视频”笔记
    # time.sleep(15)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/button[2]/span').click()
    # time.sleep(10)

    #每页显示条数调整为48/页
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[4]/div[1]/div/div/div/div/div[2]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[contains(@id,"beer-portal-container")]/div/div/div/div[4]').click()
    time.sleep(5)
    #获取最大页码
    max_page_text = driver.find_element(By.CSS_SELECTOR, '.page-settings').text
    max_page_text_obj = re.search(r'，.*?(\d+).*?页' ,max_page_text)
    max_page = max_page_text_obj.group(1)
    if int(max_page) > 3:
        max_page = 3
    else:
        max_page = int(max_page)
    time.sleep(5)

    #获取第一页页面元素html编码
    page_text = driver.find_element(By.ID, 'app').get_attribute('innerHTML')
    #提取第一页数据
    title_list = re.findall(r'class="title">(.*?)</span>',page_text,re.S)
    publish_time_list = re.findall(r'class="publish-time">发布.*?(\d{4}-\d{2}-\d{2})</span>',page_text,re.S)
    watch_list = re.findall(r'观看量.*?class="align-text">(.*?)</b>',page_text,re.S)
    watch_time_list = re.findall(r'人均观看时长.*?<b.*?>(.*?)</b>',page_text,re.S)
    like_list = re.findall(r'点赞量.*?class="align-text">(.*?)</b>',page_text,re.S)
    collect_list = re.findall(r'收藏数.*?class="align-text">(.*?)</b>',page_text,re.S)
    comment_list = re.findall(r'评论数.*?<b.*?>(.*?)</b>',page_text,re.S)
    barrage_list = re.findall(r'弹幕数.*?<b.*?>(.*?)</b>',page_text,re.S)
    share_list = re.findall(r'分享数.*?<b.*?>(.*?)</b>',page_text,re.S)
    powder_raise_list = re.findall(r'直接涨粉数.*?<b.*?>(.*?)</b>',page_text,re.S)
    time.sleep(3)

    #利用循环，翻页抓取
    n = 2
    while n <= max_page:
        n += 1
        #点击下一页箭头
        driver.find_element(By.CSS_SELECTOR, '.page-actions > button:nth-last-of-type(1) ').click()
        time.sleep(5)
        #获取下一页页面元素html编码
        page_text = driver.find_element(By.ID, 'app').get_attribute('innerHTML')
        #提取下一页数据
        title_list += re.findall(r'class="title">(.*?)</span>',page_text,re.S)
        publish_time_list += re.findall(r'class="publish-time">发布.*?(\d{4}-\d{2}-\d{2})</span>',page_text,re.S)
        watch_list += re.findall(r'观看量.*?class="align-text">(.*?)</b>',page_text,re.S)
        watch_time_list += re.findall(r'人均观看时长.*?<b.*?>(.*?)</b>',page_text,re.S)
        like_list += re.findall(r'点赞量.*?class="align-text">(.*?)</b>',page_text,re.S)
        collect_list += re.findall(r'收藏数.*?class="align-text">(.*?)</b>',page_text,re.S)
        comment_list += re.findall(r'评论数.*?<b.*?>(.*?)</b>',page_text,re.S)
        barrage_list += re.findall(r'弹幕数.*?<b.*?>(.*?)</b>',page_text,re.S)
        share_list += re.findall(r'分享数.*?<b.*?>(.*?)</b>',page_text,re.S)
        powder_raise_list += re.findall(r'直接涨粉数.*?<b.*?>(.*?)</b>',page_text,re.S)
        time.sleep(3)

    # 退出浏览器
    driver.quit()
# """
    df = pd.DataFrame({'视频标题':title_list,
                       '发布时间':publish_time_list,
                       '观看量':watch_list,
                       '人均观看时长':watch_time_list,
                       '点赞量':like_list,
                       '收藏数':collect_list,
                       '评论数':comment_list,
                       '弹幕数':barrage_list,
                       '分享数':share_list,
                       '直接涨粉数':powder_raise_list})
    df.insert(loc=0, column='账号名称', value=account_name)
    df['视频标题'] = df['视频标题'].apply(html.unescape)
    df['观看量'] = df['观看量'].apply(str2int_wan)
    df['人均观看时长'] = df['人均观看时长'].apply(smin2int)
    df['点赞量'] = df['点赞量'].apply(str2int_wan)
    df['收藏数'] = df['收藏数'].apply(str2int_wan)
    df['评论数'] = df['评论数'].apply(str2int_wan)
    df['弹幕数'] = df['弹幕数'].apply(str2int_wan)
    df['分享数'] = df['分享数'].apply(str2int_wan)
    df['直接涨粉数'] = df['直接涨粉数'].apply(str2int_wan)
    all_df = all_df.append(df, ignore_index=True)

#添加“数据日期”列
yesterday = datetime.datetime.now()
yesterday_str = yesterday.strftime("%Y-%m-%d")
all_df.insert(loc=0, column='数据日期', value=yesterday_str)
#添加“平台名称”列
all_df.insert(loc=1, column='平台名称', value='小红书')

#转成excel
all_df.to_excel('C:/Users/宇/Desktop/小红书.xlsx', index=False)
print(all_df)
# """

# print(title_list)
# print(publish_time_list)
# print(watch_list)
# print(watch_time_list)
# print(like_list)
# print(collect_list)
# print(comment_list)
# print(barrage_list)
# print(share_list)
# print(powder_raise_list)



