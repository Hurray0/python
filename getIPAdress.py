#!/usr/bin/python     
#-*-coding:utf-8-*-    
#Python 2.7.5 Author: Hurray Time: 2014.07.09   
      
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
		#print(content)

		mynote = 'for test'

		values = {'code':'test','IP':content,'device':'Mac Book Pro (Shana)','note':mynote }
		data = urllib.urlencode(values)
		#print data
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		the_page = response.read()
		print the_page

		if content.strip()!='' and the_page!=content and the_page.strip()!='':
			print '\n程序连接成功，程序退出！'
			break
		else:
			time.sleep(i)
			print '第'+str(i)+'次尝试失败！'
	except:
		print "联网失败"+'第'+str(i)+'次尝试失败！'
		time.sleep(i)