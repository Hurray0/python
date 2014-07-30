# -*- coding: utf-8 -*-
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 

url = "http://www.zzfls.net" #网页地址

wp = urllib.request.urlopen(url) #打开连接

content = wp.read() #获取页面内容

print(content.decode("utf-8").encode(type))