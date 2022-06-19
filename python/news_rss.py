#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: thejackal

""" https://pypi.org/project/feedparser/
    https://pypi.org/project/colorama/
    https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm
    https://www.pyblog.in/programming/print-formmating-in-python/
    https://www.tutorialstonight.com/python/for-loop-in-python.php
    https://www.pythoncollege.it/tutorial/if-python/
"""

""" install 
$ pip install feedparser
$ pip install colorama

"""
import feedparser
#from colorama import init, Fore, Back, Style


NewsFeed = feedparser.parse("https://larepublica.pe/noticiasfeed.xml?outputType=rss")

itemstotal = len(NewsFeed.entries)
items = 10 if itemstotal > 11 else 5

print (NewsFeed['channel']['title'])

for i in range(items):
	entry = NewsFeed.entries[i]
	print ('- %s' % entry.summary)
	
	## para saber los campos entry.keys()

print (NewsFeed['channel']['link'])
