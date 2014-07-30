#!/usr/bin/python     
#-*-coding:utf-8-*-    
#Python 2.7.5 Author: Hurray Time: 2014.07.09   
#mysqldb   
from pyDes import *
import time
import pymysql 
import binascii  
import getpass
import hashlib

conn=pymysql.connect(host="【】",user="【】",passwd="【】",db="【】",charset="utf8")  
cursor = conn.cursor()  
conn2=pymysql.connect(host="【】",user="【】",passwd="【】",db="【】",charset="utf8")  
cursor2 = conn2.cursor() 
k = des("【】", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
while 1:
	myinput = getpass.getpass('输入管理密码:')
	myinput2 = hashlib.md5(myinput.encode('utf-8')).hexdigest()
	myinput3 = hashlib.md5(myinput2.encode('utf-8')).hexdigest()
	
	sql = "select code from code where domain='codeOfCloudDB';"
	n = cursor2.execute(sql)
	for each in cursor2:
		t = each[0]
	if cmp(myinput3,t)==0:
		print "输入正确！进入密码管理系统！"
		break;
	else:
		print "密码输入错误！"
while 1:
	choice = raw_input('i:insert s:select s2:select from Cloud\n')
	if choice == 'i':
		domain = raw_input('please input domain:\n')
		username = raw_input('please input username:\n')
		code1 = raw_input('please input code:\n')	
		d = k.encrypt(code1)
		code2 = binascii.hexlify(d)
		sql = "insert into code (domain,username,code) values('"+domain+"','"+username+"','"+code2+"');"      
		n = cursor.execute(sql)    
		conn.commit()
		if n:
			print "导入成功！"

	elif choice == 's':
		domain = raw_input('plz input the doamin:\n')
		username= raw_input('plz input the username:\n')
		selectuser = ""
		if username:
			selectuser="and username='"+username+"'"
		sql = "select * from code where domain like'%"+ domain +"%' and state=1 "+ selectuser+" and id!=1 order by id desc;"
		n = cursor2.execute(sql)

		i=0
		for each in cursor2:
			i+=1
			t = k.decrypt(binascii.unhexlify(each[3]))
			print("【"+str(i)+"】domain:"+each[1] + " username:"+each[2]+" code:"+ repr(t) )

	elif choice == 's2':
		domain = raw_input('plz input the doamin:\n')
		username= raw_input('plz input the username:\n')
		selectuser = ""
		if username:
			selectuser="and username='"+username+"'"
		sql = "select * from code where domain like'%"+ domain +"%' and state=1 "+ selectuser+" and id!=1 order by id desc;"
		n = cursor.execute(sql)

		i=0
		for each in cursor:
			i+=1
			t = k.decrypt(binascii.unhexlify(each[3]))
			print("【"+str(i)+"】domain:"+str(each[1]) + " username:"+str(each[2])+" code:"+ repr(t) )

	else:
		print "系统退出！"
		break
