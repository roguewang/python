#!/usr/bin/env python
# Author:rogue
import pycurl
import os,sys
import time
import sys

URL = "http://www.baidu.com"

c = pycurl.Curl()

c.setopt(pycurl.URL,URL)

c.setopt(pycurl.CONNECTTIMEOUT, 5)

c.setopt(pycurl.TIMEOUT,5)
c.setopt(pycurl.NOPROGRESS,0)
c.setopt(pycurl.FORBID_REUSE,1)
c.setopt(pycurl.MAXREDIRS,1)

c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)

indexfile = open("/tmp/content.txt","wb")

c.setopt(pycurl.WRITEHEADER,indexfile)

c.setopt(pycurl.WRITEDATA,indexfile)

c.perform()

print(c.getinfo(c.NAMELOOKUP_TIME))
print(c.getinfo(c.CONNECT_TIME))
print(c.getinfo(c.PRETRANSFER_TIME))
print(c.getinfo(c.HEADER_SIZE))
c.close()