#!/usr/bin/env python
# Author:rogue
import pymysql

# get
conn = pymysql.connect(host="localhost",user="root",password="123",db="db1")

cur = conn.cursor()

cur.execute("select * from person3")

# data = cur.fetchall()
#
# print(data)

cur.description

for row in cur:
    print(row)

cur.close()

conn.close()

# insert

conn = pymysql.connect(host="localhost",user="root",password="123",db="db1")
cur = conn.cursor()
cur.execute("insert into person3 values(null,'rogue3')")

conn.commit()

print(cur.lastrowid)
cur.close()
conn.close()


"""
truncate table table_name   可以清空序列,重置表
"""

# con = pymysql.connect(host="localhost",user="root",password="123",db="db1")
#
# cur = conn.cursor()
#
# cur.execute("truncate table person2")
#
# conn.commit()
#
# cur.close()
#
# conn.close()
#

# fetchone()

"""
print("分隔".center(40,"="))
conn = pymysql.connect(host="localhost",user="root",password="123",db="db1")

cur = conn.cursor()

cur.execute("select * from person3")

print(cur.fetchone())   # 单取当前行,把游标指到下行

cur.scroll(1)   # 正1,表示游标相对的往后移一位,原来娵的第一行,下一个fetchone取的就是第三行了.
                # 另外默认为relative,即相对的,以当前游标位置计算,如果增加修改为absolute,就会以绝对位置来定位游标
                # 游标从0开始

print(cur.fetchone())

cur.scroll(0,"absolute")

print(cur.fetchone())   # 取游标为0的数据

cur.scroll(0,"absolute")

print(cur.fetchmany(3))     # fatchmany(),根据参数选择N条数据,同样会改变游标

cur.close()

conn.close()

"""
