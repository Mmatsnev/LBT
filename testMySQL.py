#!usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

# 连接数据库
db = pymysql.connect(host = "localhost", user = "root", password = "wang19950624", database = "test", charset = "utf8")

# 得到一个可以执行SQL语句的光标对象
cursor = db.cursor()

# 定义要执行的SQL语句
sql = """
SELECT
    *
FROM
    students;
"""

# 执行SQL语句
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print(data)
data = cursor.fetchone()
print(data)

# 关闭光标对象
cursor.close()
# 关闭数据库
db.close()