# Experimenting with urllib and re
# Attempt to parse texts from my own website

import urllib.request
import urllib.parse
import re

# url = 'http://pythonprogramming.net'
url = 'http://kevintse.azurewebsites.net/papers'
# values = {'s':'basics', # parameters for specific websites
# 		  'submit':'search'}

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'

# values = {'_r' : '0'}
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url, data)
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
# resp = urllib.request.urlopen(url)
respData = resp.read()

#print(respData)
# Using regular expression to extract contents and converting respData to String
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData)) 

a = re.findall(r'<a[^>]* href="http[^>]*>(.*?)</a>', str(respData))
# a = re.findall(r'<a*>(.*?)</a>', str(respData))
head = re.findall(r'<h2>(.*?)</h2>', str(respData))
titles = re.findall(r'<li>(.*?)</li>', str(respData))
description = re.findall(r'</li>(.*?)<li>', str(respData))
last  = re.findall(r'Rabin</li>(.*?)</ul>', str(respData))
description.append((last[0]).split('Rabin</li>')[1])

for h in head:
	print (h)

for P in paragraphs:
	print (P)

titles = titles[6:]
description = description[6:]
i = 0
paper_summary = []
for item in titles:
	# filter out specific substrings
	item = item.split('>')[1] + item.split('a>')[1] 
	item = item.replace(" <","")
	item = item.replace("/a","")
	item = item.replace("\\","")
	item = item[1:]
	paper_summary.append(item)
	#print (item)

for d in description:
	
	d = d.replace("<br>", "")
	d = d.replace("\\n", "")
	d = d.replace("\\", "")
	paper_summary[i] += "\n" + d # Assembling descriptions with titles
	i += 1

for p in paper_summary:
	print (p)

