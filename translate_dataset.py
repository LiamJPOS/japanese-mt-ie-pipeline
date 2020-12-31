#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:16:35 2020

@author: liam
"""


import mstranslate_keys as keys 
import mstranslate as mst
import os, time, shutil, traceback

subscription_key = keys.subscription_key
endpoint = keys.endpoint

#source_path = '/home/liam/ds/test_dir'
source_path = '/home/liam/ds/data_processed'
dest_path = '/home/liam/ds/data_translated'


files = [file for file in os.listdir(source_path)] 


problem_files = []
for file in files:
    
    try:
        infile = open(source_path + '/' + file, 'r')
        text_to_translate = [line for line in infile]
        write_file = open(dest_path + '/' + file.strip('_processed.txt') + '_translated.txt', 'w')
        
        print('Currently translating', file, ' ')
        
        for line in text_to_translate:
            print(line)
            translated_line = mst.ms_translate(line, 'en', 'ja', subscription_key, endpoint)
            write_file.write(translated_line + '\n')
        
        
        infile.close()
        write_file.close()
        shutil.move(source_path + '/' + file, '/home/liam/ds/hold_dir' + '/' + file)
    
    except Exception:
        problem_files.append(file)
        traceback.print_exc()
        continue
    
    
        