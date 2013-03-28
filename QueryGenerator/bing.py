#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib2
import requests

from Responses import Response



# note the single quotes surrounding the query 
URL = "https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/Web?Query='%(query)s'&$top=10&$format=json"
chuj = "\u015bl\u0119czy"
query = u"\u015bl\u0119czy".encode('utf-8')

# query == 'affirmative%2Baction'
r = requests.get(URL % {'query': urllib2.quote(query)}, auth=('', 'ffCq52T+iRuKYD5P6rgbQDwDivKj6H0bBSqlmecl4AA='))

#print r.json()['d']['results']

response = Response()

count = 0
'''
while (count<10):
	print str(r.json()['d']['results'].encode('utf-8', 'ignore'))
	count = count + 1
'''
results = []
#for result in r.results:
for i in r.json()['d']['results']:
	response = Response()
	response.url = str(i['Url'].encode('utf-8'))
	response.url_title = str(i['Title'].encode('utf-8'))
	results.append(response)

for result in results:
	i = result.url
	j = result.url_title
	print i
	print j
'''
#while(count<10):
for i in r.json()['d']['results']:
	#response.url = str(i['Url'].encode('utf-8'))
	#response.url_title = str(i['Title'].encode('utf-8'))
	print str(i['Url'].encode('utf-8', 'ignore')) + '\\' + str(i['Title'].encode('utf-8', 'ignore'))
		#count = count + 1
	
'''
#print response.url
#print response.url_title