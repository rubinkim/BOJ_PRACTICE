#-*- coding: utf-8 -*-
"""
May 10, 1980 00:31

(35.348363774733635)
"""
date = input()
date = date.replace(',', ' ')
date = date.replace(':', ' ')
print(date)

month_dict = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
m, d, y, hh, mm = date.split()
m = month_dict[m]
d, y, hh, mm = int(d), int(y), int(hh), int(mm)
print(f"m : {m}, d : {d}, y : {y}, hh : {hh}, mm : {mm}")

def is_leap(yr):
    if yr % 4 == 0 and yr % 100 == 0 and yr % 400 == 0:
        return True
    elif yr % 4 == 0 and yr % 100 == 0 and yr % 400 != 0:
        return False
    elif yr % 4 == 0 and yr % 100 != 0:
        return True
    elif yr % 4 != 0:
        return False
    
calendar_normal = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
calendar_leap = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}  

total_mins = 0
if is_leap(y):
    for m0 in range(1, 13):
        for d0 in range(1, calendar_leap[m0]):
            for h0 in range(25):
                for mm0 in range(61):
                    total_mins += 1
                    
elif is_leap(y):
    for m0 in range(1, 13):
        for d0 in range(1, calendar_leap[m0]):
            for h0 in range(25):
                for mm0 in range(61):
                    total_mins += 1
print(total_mins)           


