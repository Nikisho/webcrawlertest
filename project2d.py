# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:05:10 2021

@author: Romain
"""
import random
from requests_html import HTMLSession
from project2b import linkextractor
import requests
from bs4 import BeautifulSoup
#import webbrowser
#from IPython import get_ipython
#from requests_html import HTML
#from project2b import *
#import re
#prints text from url
#get_ipython().magic('reset -sf')
#from selenium import webdriver
#def parsetest(GEN_URL):
    
DOMNAME = 'https://www.incidence-deco.com'
#DOMNAME = 'londonperfect'   

n = 3 #n paraghraps
URLZ = linkextractor('https://www.incidence-deco.com/travaux-bricolage/')
#URLZ = linkextractor('https://www.londonperfect.com/blog/2020/')

URLZ2 = [] #newlist to append
#GEN_URL = 'https://www.incidence-deco.com/la-maison-bretonne-accueillante-et-chaleureuse/'
#print(URLS)
for elem in URLZ: #if the domname is not in the link it's not worth inspecting, clear out
    if DOMNAME not  in elem:
       URLZ.remove(elem)
    else:
        URLZ2.append(elem)
        
#URLZ = ['https://www.incidence-deco.com/la-maison-bretonne-accueillante-et-chaleureuse/','https://www.incidence-deco.com/la-chambre-feng-shui-comment-reussir-lamenagement/']
for GEN_URL in URLZ2:  # we iterate through all the links extracted. 
    Score = 0         
    html_text = requests.get(GEN_URL).text
    
    soup = BeautifulSoup(html_text,'html.parser')
    
    J = soup.find_all('p') #J is a vector with arrays J[i] is a paragraph, look for <p> divs s
    if len(J) < 6: #if the page has no content, we skip it (contact form/login/etc..)
        continue
    else:
    #print 2 paragraphs, a is rand within len(J) turn the array j[a] into a string element
        for i in range(n): #n 
            cake = True
            a = random.randint(5,len(J)-1) #a is some number between 1 and max[J]
            w = str(J[a]) #turn the arrays into str
            #print(w)
            #print(i)
            breakit = 0 #introduce this to break while loop after 3 fails.
            while cake == True:
                if len(w) < 100 or '<a' in w or '</a>' in str(w) or 'id=' in str(w):
                    i = 0
                    b = random.randint(5,len(J)-1) 
                    w = str(J[b])
                    breakit +=1
                else:
                    cake = False #cake breaks and look for another paragraph
                    continue
                if breakit > 3: #break the loop 
                    break
                continue
            w2 = w.replace('<p>','')   #get rid of <p and </p
            w3 = w2.replace('</p>','')
            w4 = w3.replace('<strong>','')
            w5 = w4.replace('<p','')
            w6 = w5.replace('</strong>','')
            
            #print(w6 + '\n') 
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
            #print(Storethem[0:10])
            for EACHLINK in Storethem[0:10]:
                if DOMNAME in EACHLINK:
                    Score +=1
                    break
                    #print('the score is' + str(Score))
                    #break #break if link matches
        
        ratio = Score / n #lets append all the ratios in a vector !!!
        print(ratio)
        print(GEN_URL)

#briefing: Structure of code completed. If the site is well written it'll crawl through 
#pages and parse paragraphs (<p></p>). The while loop is there to avoid small paragraphs,
#we break the while loop via an increment (some page might only have small paragraphs)
#Must still improve extractor fn to give relevent links to crawl
#Must visualize a few more links to test
#Google blocked my IP with a captcha so tests are impossible atm so must bypass.. 