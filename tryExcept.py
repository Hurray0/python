#!/usr/bin/python     
#-*-coding:utf-8-*-       
      
import urllib
import urllib2
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 

url = "http://hurraydb.sinaapp.com/ip.php" #网页地址

i=0
while 1:
	i += 1
	try:
		wp = urllib.urlopen(url) #打开连接
		content = wp.read() #获取页面内容
		print(content)

		
		if content.strip()!='':
			print '\n程序连接成功，程序退出！'
			break
		else:
			time.sleep(i)
			print '第'+i+'次尝试失败！'
	except:
		print '额，没联网，待会再试\n'
		time.sleep(i)