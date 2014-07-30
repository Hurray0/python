#!/usr/bin/python     
#-*-coding:utf-8-*-     

# 进行表单提交  小项  2008-10-09     
      
import httplib,urllib;  #加载模块     
      
#定义需要进行发送的数据     
params = urllib.urlencode({'msg':'have a try',      
                           });      
#定义一些文件头     
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
    
#与网站构建一个连接     
conn = httplib.HTTPConnection("http://hurraydb.sinaapp.com/try.php");      
#开始进行数据提交   同时也可以使用get进行     
conn.request(method="POST",url="http://hurraydb.sinaapp.com/try.php",body=params,headers=headers);      
#返回处理后的数据     
response = conn.getresponse();      
#判断是否提交成功     
if response.status == 302:      
    print "发布成功!^_^!";      
else:      
    print "发布失败\^0^/";      
#关闭连接     
conn.close();   