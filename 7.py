# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:48:31 2020

@author: Lenovo
"""

def int_func(s):
    '''Преобразует первую букву строки s в заглавную'''
    return s[0].upper()+s[1:len(s)]

s=input('Введите несколько английских слов, разделенных пробелом:')
l=s.split(' ')
out_str=''
for ss in l:
    out_str=out_str+int_func(ss)+' '

print(out_str)