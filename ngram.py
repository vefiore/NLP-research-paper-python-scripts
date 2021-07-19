#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:36:33 2019

@author: vefiore
"""


t = "put intended text or file here"

import re
import operator
from collections import Counter


def ngram(t, n):

    count =[]
    # Convert to lowercases
    t = t.lower()
    
    # clean unwanted characters and replace w space
    t = re.sub(r'[^a-zA-Z0-9\s]', ' ', t)
    
    # break into token, remove empty tokens
    tokens = [token for token in t.split(" ") if token != ""]
    
    # concatentate  tokens into ngrams 
    ngrams = zip(*[tokens[i:] for i in range(n)])
    output = [" ".join(ngram) for ngram in ngrams]
    
    # getting counts for each ngram
    return Counter(output)

