#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:05:03 2020

@author: liam
"""
#Takes Japanese aritcle titles and maps the Q codes needed to query Wikidata

import os
from wikimapper import WikiMapper
import pandas as pd

target_dir = "/home/liam/ds/data_people"
mapper = WikiMapper("/home/liam/ds/wikimapper_data/index_jawiki-latest.db")

files = [file for file in os.listdir(target_dir)]


query_info = []

i = -1
for file in files:
    i += 1
    
    #grab wiki_id
    wiki_id = file.strip("_processed.txt")
    
    #grab title
    infile = open(f"{target_dir}/{files[i]}").read()
    start = infile.index("wgPageName")+13
    end = infile.index('","wgTitle') 
    title = infile[start : end]

    #grab Q code
    Q_code = mapper.title_to_id(title)
    
    #append to query_info
    query_info.append((wiki_id, title, Q_code))
   
df = pd.DataFrame(query_info)





