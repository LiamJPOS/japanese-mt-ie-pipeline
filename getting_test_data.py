import shutil 
import os
import random

dest = '/home/liam/Dissertation/data_people'
source = '/home/liam/Dissertation/Data/JP-5/plain/Person'

articles_grabbed = 0
counter = 0 

files = [file for file in os.listdir(source)]

while articles_grabbed < 1500:
        shutil.copy(source+'/'+files[random.randint(0, len(files) - 1)],
                    dest)
        articles_grabbed += 1
        

        
