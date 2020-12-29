# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:43:25 2020

@author: Lenovo
"""

def int_func(s):
    '''Преобразует первую букву строки s в заглавную'''
    return s[0].upper()+s[1:len(s)]

s=input('Введите английское слово:')
print(int_func(s))