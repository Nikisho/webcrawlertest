# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:26:38 2021

@author: Romain
"""
"""this code extracts all the links found on a page"""
from bs4 import BeautifulSoup
#from project2 import check
import requests
import requests.exceptions
#from urllib.parse import urlparse
#from collections import deque

def linkextractor(URLNAME):
    #URL = 'https://www.avantgardevegan.com/'
    
    """nextnew_urls = deque([URL])"""
    reqs = requests.get(URLNAME)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    URLS = [] #create empty arraty
    for link in soup.find_all('a'): 
        if 'pinterest' in link.get('href') or 'youtube' in link.get('href') or 'instagram' in link.get('href') or 'contact' in link.get('href') or 'facebook' in link.get('href') or 'twitter' in link.get('href'):
            print('Skip!')
            continue 
        elif 'https' in link.get('href'):
            #print(link.get('href')) #print the href = https://example.link
            data = link.get('href') 
            URLS.append(data) #store in array
            URLS = list(dict.fromkeys(URLS))
    return URLS    
#for i in range(10,13):
    #check(URLS[i])