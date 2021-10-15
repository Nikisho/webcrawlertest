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
import requests
from bs4 import BeautifulSoup
from IPython import get_ipython
from requests_html import HTML
from requests_html import HTMLSession
from project2b import linkextractor
#from project2b import *
get_ipython().magic('reset -sf')
#import re
#from selenium import webdriver
#prints text from url
#def parsetest(GEN_URL):
 
    
DOMNAME = 'https://www.incidence-deco.com'   
#DOMNAME = 'londonperfect.com'
#DOMNAME = 'acefitness.org'
n = 3
Score = 0
MUSTBREAK = 0 #to break the while loop at some point 
x = True
#VAL = 0

#URLS = linkextractor(DOMNAME)
GEN_URL = 'https://www.incidence-deco.com/la-maison-bretonne-accueillante-et-chaleureuse/'
#GEN_URL = 'https://www.acefitness.org/education-and-resources/lifestyle/blog/7379/family-fitness-day-healthy-activities-for-the-whole-family/?topicScope=group-exercise'
#GEN_URL ='https://www.incidence-deco.com/actus-deco/'
#print(URLS)
#for GEN_URL in URLS:

html_text = requests.get(GEN_URL).text
soup = BeautifulSoup(html_text,'html.parser')
J = soup.find_all('p') #J is a vector with arrays J[i] is a paragraph, look for <p> divs s

#print 2 paragraphs, a is rand within len(J) turn the array j[a] into a string element
for i in range(n): #n
    cake = True
    a = random.randint(5,len(J)-1) #a is some number between 1 and max[J]
    w = str(J[a]) #turn the arrays into str
    print(i)
    
    while cake == True:
        if len(w) < 100 or '<a' in w or '</a>' in str(w) or 'id=' in str(w):
            i = 0
            b = random.randint(10,len(J)-1) 
            w = str(J[b])
        else:
            cake = False
            continue
       
    w2 = w.replace('<p>','')   #get rid of <p and </p
    w3 = w2.replace('</p>','')
    w4 = w3.replace('<strong>','')
    w5 = w4.replace('<p','')
    w6 = w5.replace('</strong>','')
    
    print(w6 + '\n') 
    #webbrowser.open('https://www.google.com/search?q='+ w5)
    ##PART 3##
    URL = 'https://www.google.com/search?q='+ w6 #our extracted paragraph searched on the browser
    session = HTMLSession()
    response = session.get(URL).text
    sourcetext = BeautifulSoup(response,'lxml') #parse the html text
    
    substr0 = 'wikipedia'
    substr = 'google'
    substr2 = 'https'
    
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
    for EACHLINK in Storethem[0:10]:
        if DOMNAME in EACHLINK:
            Score = Score + 1
            print('match!')
            break #break the loop, only need one match

ratio = Score / (n) #lets append all the ratios in a vector !!!
print(ratio)

#The while loop blocks pages which only contains title of othe articles, 
#must find a way to recognise those pages or skip the link when parsing
# ideas: break loop on <span divs, increase a variable and break loop after N iterations, 
        


    
   
