# -*- coding: utf-8 -*-     
#mysqldb    
import time, MySQLdb    

#连接    
conn=MySQLdb.connect(host="localhost",user="root",passwd="klxqzg",db="CloudDB",charset="utf8")  
cursor = conn.cursor()    

#写入    
sql = "insert into try2 (id,msg) values('3','哈哈')"      
n = cursor.execute(sql)    
conn.commit()
print n    

cursor.close()    

#关闭    
conn.close()   