# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:26:11 2020

@author: Lenovo
"""

def dvd(a,b):
    '''Деление числа a на b'''
    if b!=0:
        return a/b
    else:
        raise ValueError('Второй аргумент не должен равняться 0!')
    

a=float(input('Введите первое число: '))
b=float(input('Введите второе число: '))
print(dvd(a,b))