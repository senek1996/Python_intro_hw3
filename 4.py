# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:04:23 2020

@author: Lenovo
"""

def neg_pow(x,y):
    '''Возведение числа x в отрицательную целую степень y
       Используется формула a^(-n)=1/(a^n)'''
    if y>=0:
        raise ValueError('Неверное значение степени! Нужно целое отриц. число')
    
    y=abs(y)
    xx=1
    for i in range(y):
        xx=xx*x
    
    return 1/xx

s=input('Введите числа x,y через пробел: ')
x,y=s.split(' ')
x=float(x)
y=int(y)
print('{0}^({1})={2}'.format(x,y,neg_pow(x,y)))