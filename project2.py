# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:21:57 2021

@author: Romain
"""
#def check( GEN_URL ):
    
""""this code takes a link, extracts n paragraphs <p> from the html.text of that link,
searches them on Googlech and stores the 10 first result links from source code 
NOT THE 10 first results!!"""
    
import random
import webbrowser
#from selenium import webdriver
import requests
from bs4 import BeautifulSoup
#import re
#prints text from url
from IPython import get_ipython
from requests_html import HTML
from requests_html import HTMLSession
from project2b import linkextractor
#from project2b import *
#get_ipython().magic('reset -sf')

#def parsetest(GEN_URL):
    
DOMNAME = 'https://www.incidence-deco.com'   

#URLS = linkextractor(DOMNAME)
GEN_URL = 'https://www.incidence-deco.com/la-maison-bretonne-accueillante-et-chaleureuse/'
#print(URLS)
#for GEN_URL in URLS:

html_text = requests.get(GEN_URL).text

soup = BeautifulSoup(html_text,'html.parser')

J = soup.find_all('p') #J is a vector with arrays J[i] is a paragraph, look for <p> divs s

#print 2 paragraphs, a is rand within len(J) turn the array j[a] into a string element
for i in range(1,3): #n 
    a = random.randint(10,len(J)-1) #a is some number between 1 and max[J]
    w = str(J[a]) #turn the arrays into str
    VAL = 0
    while VAL == 0:   #while len(w) is less 150 we change its size, we want enough words
         if len(w) < 150:
            p = random.randint(10,len(J)-1)
            w = str(J[p])
         else: 
             break #break the loop if len(w) has enough words
             VAL = 1
    w2 = w.replace('<p>','')   #get rid of <p and </p
    w3 = w2.replace('</p>','')
    w4 = w3.replace('<strong>','')
    w5 = w4.replace('<p','')
    w6 = w5.replace('</strong>','')
    
    print(w6 + '\n') 
    #webbrowser.open('https://www.google.com/search?q='+ w5)
    ##PART 3##
    URL = 'https://www.google.com/search?q='+ w6
    session = HTMLSession()
    response = session.get(URL).text
    x = True
    sourcetext = BeautifulSoup(response,'lxml') #parse the html text
    
    substr0 = 'wikipedia'
    substr = 'google'
    substr2 = 'https'
    
    Score = 0
    Storethem = [] #RECHEcK LOOP
    for link in sourcetext.find_all('a'): #find all links in search rzlt page
        data = link.get('href')
        datastr = str(data) #making sure its a str..
        
        if substr in datastr or substr0 in datastr:
            x = False
        elif substr2 in datastr:
            #print(datastr)
            Storethem.append(datastr)
        #superlist.append(data)
    print(Storethem[0:10])
    for EACHLINK in Storethem[1:10]:
        if DOMNAME in EACHLINK:
            Score +=1

ratio = Score / 2#lets append all the ratios in a vector !!!

        


    
   
