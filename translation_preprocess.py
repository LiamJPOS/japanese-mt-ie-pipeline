#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:58:11 2020

@author: liam
"""
#Strip unecessary info from articles
#Remove whitespace from lines and prepare each article for translation
#Write processed lines to new text files to run through mstranslate.py line by line


import os 

source_path = '/home/liam/Dissertation/data_people'
dest_path = '/home/liam/Dissertation/data_processed'

files = [file for file in os.listdir(source_path)]

for file in files:
    source_file = open(source_path + '/' + file)
    
    lines_to_write = [line for line in source_file 
        if line.strip()
        and 'document.document' not in line
        and '(window' not in line
        and 'mw.' not in line ]
    
    write_file = open(dest_path + '/' + file.strip('.txt') + '_processed' + '.txt', 'w')
    
    for line in lines_to_write:
        write_file.write(line)
        
    source_file.close()
    write_file.close()
    
    
    
    
    



	



