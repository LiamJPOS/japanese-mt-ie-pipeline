#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:31:42 2020

@author: liam
"""

import json, os


articles_path = '/home/liam/Dissertation/data_people' #Change to directory with new articles in and it will only write the new files
articles =[file.strip('.txt') for file in os.listdir(articles_path) if file.endswith('.txt')]
    
links_infile = open('/home/liam/Dissertation/ja_en_langlinks.json')
links  = [line for line in links_infile]

ja_ids = []
for link in links:
    ja_ids.append(str(json.loads(link)['destination']['pageid']))

matches = []
no_match = []        
m_file = open('articles_with_en.txt', 'w')
nm_file = open('articles_without_en.txt', 'w')


for article in articles:
    if article in ja_ids:
        print('match')
        matches.append(article + '.txt')
        m_file.write(article + '.txt' + '\n')
    else:
        print('no match')
        no_match.append(article + '.txt')
        nm_file.write(article + '.txt' + '\n')

links_infile.close()
m_file.close()
nm_file.close()













