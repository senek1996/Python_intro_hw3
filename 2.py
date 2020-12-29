# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:50:09 2020

@author: Lenovo
"""

def userInfo(sname,fname,year,city,tel,email):
    '''
    Выводит информацию о пользователе одной строкой
    '''
    s='Фамилия: {0}; Имя: {1}; Год рождения: {2};'
    s=s+' Город: {3}; Телефон: {4}; E-mail: {5}\n'
    return s.format(sname,fname,year,city,tel,email)

s=input('Введите свою фамилию и имя через пробел: ')
sname, fname=s.split(' ')
s=input('Введите свой год рождения и город проживания через пробел: ')
year, city=s.split(' ')
year=int(year)
s=input('Введите свой телефон и e-mail через пробел: ')
tel, email=s.split(' ')

print(userInfo(sname,fname,year,city,tel,email))