# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:34:23 2019

@author: james
"""

import pandas as pd
df = pd.read_csv('nhis.csv')
df.head()

height = df.height.values.tolist()
    # Check for even/odd and perform calculations accordingly - use if-else 


    # Check for even/odd and perform calculations accordingly - use if-else
    
def get_mode(data):
    freq_dict={}
    #freq_dict=dict.fromkeys(list(set(data)),0)
    
    for d in data:
        count=freq_dict.get(d,0)
        freq_dict[d]=count+1
        
    return freq_dict
    