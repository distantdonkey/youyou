import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://creator.xiaohongshu.com/')
time.sleep(120)
dictCookies = driver.get_cookies()
jsonCookies = json.dumps(dictCookies)
with open('15861805215.txt', 'w') as f:
    f.write(jsonCookies)
print('cookies保存成功！')
