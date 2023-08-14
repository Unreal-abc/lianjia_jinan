import pymysql
import os
import csv
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, charset='utf8mb4')
cursor = db.cursor()
sql = "CREATE DATABASE IF NOT EXISTS lianjia"
# 执行创建数据库的sql
cursor.execute(sql)
cursor.execute("use lianjia")
sql = "CREATE TABLE IF NOT EXISTS guangzhou(名称 varchar(255),小区名 varchar(255),位置 varchar(255),房间类型 varchar(255),面积 varchar(255),朝向 varchar(255),装修 varchar(255),楼层 varchar(255),楼况 varchar(255),关注人数 varchar(255),发布时间 varchar(255),总价 varchar(255),单价 varchar(255),标签 varchar(255),区域 varchar(255))"
cursor.execute(sql)
# columns = ['名称', '小区名', '位置', '房间类型', '面积', '朝向', '装修', '楼层', '楼况', '关注人数', '发布时间', '总价', '单价','区域', '标签']
file_list=os.listdir('爬取结果')
for name in file_list:
    quyu=str(name).split('.')[0]
    with open('爬取结果/'+name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
        for one_row in rows:

            s1 = one_row[0]
            s2 = one_row[1]
            s3 = one_row[2]
            s4 = one_row[3]
            s5 = one_row[4]
            s6 = one_row[5]
            s7 = one_row[6]
            s8 = one_row[7]
            s9 = one_row[8]
            s10 = one_row[9]
            s11 = one_row[10]
            s12 = one_row[11]
            s13 = one_row[12]
            s14 = one_row[13]
            s15 = quyu
            sql = "insert into guangzhou() values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (s1, s2, s3, s4, s5, s6, s7, s8, s9 ,s10,s11,s12,s13,s14,s15)
            cursor.execute(sql)
    db.commit()
db.close()
