# -*-coding:utf-8 -*-
# !/usr/bin/env python
# __author__ = 'wenbin'
import re,urllib2
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def page(pg):
    url = 'https://www.pengfu.com/index_%s.html' %pg
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    #req = urllib2.Request(url, headers=headers)
    html = urllib.urlopen(url).read()
    #print html
    return html
def title(html):
    html = page(1)
    reg= re.compile(r'<h1 class="dp-b"><a href=".*?" target="_blank">(.*?)</a>')
    item = re.findall(reg,html)
    #print item
    return item
def content(html):
    reg = r'img src="(.*?)" width='
    item = re.findall(reg,html)
    #print item
    return item
def download(url,name):
    path = 'image\%s.jpg' %name.decode('utf-8').encode('gbk')
    urllib.urlretrieve(url,path)
for i in range(1,6):
    html = page(i)
    title_list = title(html)
    #print title_list
    content_list = content(html)
    #print content_list
    for i,z in zip(title_list,content_list):
        download(z,i)
        print i,z

