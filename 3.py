# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:53:20 2020

@author: Lenovo
"""

def my_func(a,b,c):
    s=a+b
    if a+c>s:
        if a+c>b+c:
            return a+c
        else:
            return b+c
    elif b+c>s:
        return b+c
    
    return s

s=input('Введите числа a,b,c через пробел: ')
a,b,c=s.split(' ')
a=float(a)
b=float(b)
c=float(c)
print('Сумма наибольших 2 аргументов: {0}'.format(my_func(a,b,c)))