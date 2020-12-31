#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:50:39 2020

@author: liam
"""

import requests, uuid, json
import mstranslate_keys as keys

subscription_key = keys.subscription_key
endpoint = keys.endpoint


#Takes line of text as input and outputs translated text
#Language defined in function parameters - e.g 'en' for lang_to translates input text into English
def ms_translate (input_line, lang_to, lang_from, subscription_key, endpoint):
    
    path = '/translate?api-version=3.0'
    params = '&to=' + lang_to + '&from=' + lang_from
    constructed_url = endpoint + path + params
    
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region' : 'westeurope',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    body = [{
        'text': input_line
    }]
    
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    translated_text = response[0]["translations"][0]["text"]
    
    #return json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))
    return translated_text


