#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root', password='liuyu19951124', database='demo')
cursor = db.cursor()
update_sql = "drop table teacher"
try:
    cursor.execute(update_sql)
    db.commit()
    cursor.execute("select * from teacher")
    data = cursor.fetchall()
    print(data)
except:
    print("数据修改失败,请查检sql语句")
    db.rollback()
    raise

db.close()