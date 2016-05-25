# Google-Image-Scrapper


One Basic Example I used 

# -*- coding: utf-8 -*-
"""
Created on Tue May 24 22:35:12 2016

@author: ananab06
"""

import os

os.chdir("C:\Users\AnanAb06\Documents\Python Scripts")
from Google-Image-Scrapper import google
s=raw_input("Enter Your Query ")
results = google.search_images(s)
for i in results:
    p=str(i).split(',')
    f=p[len(p)-1][:-1][6:]
    print f