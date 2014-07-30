# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 

url = "http://hurraydb.sinaapp.com/try.php" #网页地址

values = {
          'msg' : 'postHurrayaaa'
         }
 
data = urllib.parse.urlencode(values).encode(encoding='UTF8')
req = urllib.request.Request(url, data, headers)
req.add_header('Referer', 'http://www.python.org/')
response = urllib.request.urlopen(req)
the_page = response.read()
 
print(the_page.decode("utf8"))