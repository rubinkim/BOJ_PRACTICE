#-*- coding: utf-8 -*-
"""
May 10, 1981 00:31

(35.348363774733635)
"""
date = input()
date = date.replace(',', ' ')
date = date.replace(':', ' ')
print(date)

month_dict = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
m, d, y, hh, mm = date.split()
m = 
print(f"m : {m}, d : {d}, y : {y}, hh : {hh}, mm : {mm}")


