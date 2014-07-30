# -*- coding: utf-8 -*-  
from pyDes import *
import binascii		
data = "hello"
k = des("12345678", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
eee = binascii.hexlify(d)
print "Encrypted: %r" % eee
asdf = binascii.unhexlify(eee)
#print "??=%s" % "hello".encode('gb18030').decode('gb18030')
print "Decrypted: %r" % k.decrypt(asdf)
assert k.decrypt(d, padmode=PAD_PKCS5) == data