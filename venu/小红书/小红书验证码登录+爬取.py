from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
import datetime

#建立最终输出的excel模板
all_df = pd.DataFrame(columns=['账户名称', '视频标题', '发布时间', '观看量', '人均观看时长', '点赞量', '收藏数', '评论数', '弹幕数', '分享数', '直接涨粉数'])
#账号集合
phone_nums_dict = {
    '小空电竞':'19201838394',
    '磕老师在线':'19201809318',
    '咪咕篮球':'19201895220',
    '科技观测君':'19201835272',
    '掼蛋小辣椒':'19201852067',
    '大咪也看球':'19201867172'
}

#chrome浏览器
#设置无头浏览器
option = webdriver.ChromeOptions()
option.add_argument("--headless")
# 无头浏览器需要添加user-agent来隐藏特征
option.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')

#实现用户登录并跳转笔记数据页面
for i,j in phone_nums_dict.items():
    driver = webdriver.Chrome(options=option)
    driver.get('https://creator.xiaohongshu.com/creator/notes?source=official')
    time.sleep(5)
    #输入手机号
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/input").send_keys(j)
    #点击获取验证码
    driver.find_element(By.CLASS_NAME, 'css-13or2dr').click()
    time.sleep(3)
    #人工接收填写验证码
    code = input(f"请输入{i}{j}手机短信验证码：")
    #填入手机短信验证码
    driver.find_element(By.XPATH, '//*[@id="page"]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/input').send_keys(code)
    time.sleep(1)
    #点击登录
    driver.find_element(By.XPATH, '//*[@id="page"]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/button').click()
    #此处加载时间一般较长，可以延长强行等待时间
    time.sleep(10)
    # 获取账户名称
    account_name = driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div[2]/div/span').text
    #点击“视频”笔记
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[1]/div/button[2]/span').click()
    time.sleep(10)

    #每页显示条数调整为48/页
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[4]/div[1]/div/div/div/div/div[2]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[contains(@id,"beer-portal-container")]/div/div/div/div[4]').click()
    time.sleep(5)
    #获取最大页码
    max_page = driver.find_element(By.CSS_SELECTOR, '.page-actions > button:nth-last-of-type(2) > span').text

    #获取第一页页面元素html编码
    page_text = driver.find_element(By.ID, 'app').get_attribute('innerHTML')
    #提取第一页数据
    account_name_list = [account_name]
    title_list = re.findall(r'class="title">(.*?)</span>',page_text,re.S)
    publish_time_list = re.findall(r'class="publish-time">发布.*?(\d{4}-\d{2}-\d{2})</span>',page_text,re.S)
    watch_list = re.findall(r'观看量.*?class="align-text">(\d+)</b>',page_text,re.S)
    watch_time_list = re.findall(r'人均观看时长.*?<b.*?>(\w+)</b>',page_text,re.S)
    like_list = re.findall(r'点赞量.*?class="align-text">(\d+)</b>',page_text,re.S)
    collect_list = re.findall(r'收藏数.*?class="align-text">(\d+)</b>',page_text,re.S)
    comment_list = re.findall(r'评论数.*?<b.*?>(\d+)</b>',page_text,re.S)
    barrage_list = re.findall(r'弹幕数.*?<b.*?>(\d+)</b>',page_text,re.S)
    share_list = re.findall(r'分享数.*?<b.*?>(\d+)</b>',page_text,re.S)
    powder_raise_list = re.findall(r'直接涨粉数.*?<b.*?>(\d+)</b>',page_text,re.S)
    time.sleep(3)

    #利用循环，翻页抓取
    n = 2
    while n <= int(max_page):
        n += 1
        #点击下一页箭头
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div[2]/button[5]').click()
        time.sleep(5)
        #获取下一页页面元素html编码
        page_text = driver.find_element(By.ID, 'app').get_attribute('innerHTML')
        #提取下一页数据
        account_name_list.append(account_name)
        title_list += re.findall(r'class="title">(.*?)</span>',page_text,re.S)
        publish_time_list += re.findall(r'class="publish-time">发布.*?(\d{4}-\d{2}-\d{2})</span>',page_text,re.S)
        watch_list += re.findall(r'观看量.*?class="align-text">(\d+)</b>',page_text,re.S)
        watch_time_list += re.findall(r'人均观看时长.*?<b.*?>(\w+)</b>',page_text,re.S)
        like_list += re.findall(r'点赞量.*?class="align-text">(\d+)</b>',page_text,re.S)
        collect_list += re.findall(r'收藏数.*?class="align-text">(\d+)</b>',page_text,re.S)
        comment_list += re.findall(r'评论数.*?<b.*?>(\d+)</b>',page_text,re.S)
        barrage_list += re.findall(r'弹幕数.*?<b.*?>(\d+)</b>',page_text,re.S)
        share_list += re.findall(r'分享数.*?<b.*?>(\d+)</b>',page_text,re.S)
        powder_raise_list += re.findall(r'直接涨粉数.*?<b.*?>(\d+)</b>',page_text,re.S)
        time.sleep(3)

    # 退出浏览器
    driver.quit()

    df = pd.DataFrame({'账户名称':account_name_list,
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
    all_df = all_df.append(df, ignore_index=True)

#添加“数据日期”列
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")
all_df.insert(loc=0, column='数据日期', value=yesterday_str)
#添加“平台名称”列
all_df.insert(loc=1, column='平台名称', value='小红书')
# #添加“账户名称”列
# df.insert(loc=2, column='账户名称', value=account_name)
#转成excel
all_df.to_excel('C:/Users/宇/Desktop/xiaohongshu.xlsx', index=False)
print(all_df)

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

