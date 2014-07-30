# -*- coding: utf-8 -*-
import pymysql
conn = pymysql.connect(host='localhost', unix_socket='/tmp/mysql.sock', user='root', passwd='klxqzg', db='CloudDB',charset='utf8')
cur = conn.cursor()
sql = "insert into try2 (id,msg) values ('4','试一下')"
sta = cur.execute(sql)
conn.commit()
print sta

for each in cur:
	print(each[1]) 
	
cur.close()
conn.close()
