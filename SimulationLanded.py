import HTMLParser
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re

#登陆的主页面
hosturl = 'http://www.renren.com/SysHome.do'
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = ''