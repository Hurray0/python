#!/usr/bin/python     
#-*-coding:utf-8-*-  
import hashlib


print hashlib.md5('123456'.encode('utf-8')).hexdigest()