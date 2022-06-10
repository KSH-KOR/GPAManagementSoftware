#!/usr/bin/env python
# coding: utf-8

import sys
from HGUCrawler import Crawler

id = sys.argv[1]
pw = sys.argv[2]
c = Crawler()
driver = c.login(id= id, pw= pw)
print(c.getCourseInfo(driver))

