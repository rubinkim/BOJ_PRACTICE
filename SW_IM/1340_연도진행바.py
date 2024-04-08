#-*- coding: utf-8 -*-
"""
May 10, 1981 00:31

(35.348363774733635)
"""
date = input()
date = date.replace(',', ' ')
date = date.replace(':', ' ')
print(date)
m, d, y, hh, mm = date.split()
print(f"m : {m}, d : {d}, y : {y}, hh : {hh}, mm : {mm}")