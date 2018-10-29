#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
import yaml

xmlcontent = etree.parse("bigmem.xml")
for a in xmlcontent.xpath('//clock'):
	print a.text
	for b in a.xpath('/timer'):
		print b.text


f = open('1.yml')  
dataMap = yaml.load(f)  
f.close() 
print dataMap
print type(dataMap)
