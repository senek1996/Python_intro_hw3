# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:22:11 2020

@author: Lenovo
"""

def summa(l):
    '''Вычисление суммы чисел из списка l'''
    s=0
    for n in l:
        if n.find(';')==-1: #нет точки с запятой
            s=s+float(n)
        else:
            s=s+float(n[0:len(n)-1])
            break
        
    
    return s
    
s=''
sma=0
while s.find(';')==-1: #точка с запятой - спецсимвол
    s=input('Введите числа через пробел. Для завершения введите ";" ')
    l=s.split(' ')
    sma=sma+summa(l)

print('Сумма введенных до знака ";" чисел: {0}'.format(sma))