#!/usr/bin/python     
#-*-coding:utf-8-*-       
      
import urllib
import urllib2
url = 'http://hurraydb.sinaapp.com/try.php'
values = {'msg':'hahatry'}
data = urllib.urlencode(values)
print data
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page