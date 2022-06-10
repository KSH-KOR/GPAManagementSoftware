#!/usr/bin/env python
# coding: utf-8

import sys
print(sys.argv[0]) # prints python_script.py
print(sys.argv[1]) # prints var1
print(sys.argv[2]) # prints var2


from HGUCrawler import Crawler

id = sys.argv[1]
pw = sys.argv[2]
c = Crawler()
driver = c.login(id= id, pw= pw)
print(c.getCourseInfo(driver))

