# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:32:06 2021

@author: Romain
"""

import scrapy
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from requests_html import HTML
from requests_html import HTMLSession

DOMAINNAME = 'www.incidence-deco.com'

URL = 'https://www.google.com/search?q=Belle maison traditionnelle de la Bretagne avec un toit en ardoise en pente et des murs en granit'

session = HTMLSession()
response = session.get(URL).text
x = True
sourcetext = BeautifulSoup(response,'lxml') #parse the html text


substr = 'google'
substr2 = 'https'
#superlist = []
count = 0


Storethem = []
for link in sourcetext.find_all('a'): #find all links in search rzlt page
    data = link.get('href')
    datastr = str(data)
    
    if substr in datastr:
        x = False
    elif substr2 in datastr:
        #print(datastr)
        Storethem.append(datastr)
    #superlist.append(data)
    
print(Storethem[1:10])

for EACHLINK in Storethem[1:10]:
    if DOMAINNAME in EACHLINK:
        print('we found a match!')
 
    
    

#reqs = requests.get(URL).text
#print(reqs)

#Ls = BeautifulSoup(reqs)
#Ls1 = Ls.findALL('div', class_= 'rc')