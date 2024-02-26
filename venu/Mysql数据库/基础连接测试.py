import pymysql

db = pymysql.connect(
    host="localhost",
    port=3306,
    user='root',    #在这里输入用户名
    password='liuyu19951124',     #在这里输入密码
    charset='utf8mb4'
    ) #连接数据库

cursor = db.cursor() #创建游标对象

sql = 'show databases' #sql语句

cursor.execute(sql)  #执行sql语句

# one = cursor.fetchone()  #获取一条数据
# print('one:',one)
#
# many = cursor.fetchmany(3) #获取指定条数的数据，不写默认为1
# print('many:',many)

all = cursor.fetchall() #获取全部数据
print('all:',all)

cursor.close()
db.close()  #关闭数据库的连接
