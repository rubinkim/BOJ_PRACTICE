#-*- coding: utf-8 -*-
"""
May 10, 1981 00:31

(35.348363774733635)

January 01, 2008 00:00

(0.0)

December 31, 2007 23:59

(99.99980974124807)

July 02, 2008 00:00

(50.0)

January 31, 1900 00:47

(8.228120243531203)
"""
date = input()
date = date.replace(',', ' ')
date = date.replace(':', ' ')
#print(date)

month_dict = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
m, d, y, hh, mm = date.split()
m = month_dict[m]
d, y, hh, mm = int(d), int(y), int(hh), int(mm)
#print(f"m : {m}, d : {d}, y : {y}, hh : {hh}, mm : {mm}")

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
upto_mins = 0

# normal year : 525,600 mins
# leap year : 527,040 mins

if is_leap(y):
    for m0 in range(1, 13):
        for d0 in range(calendar_leap[m0]):
            for h0 in range(24):
                for mm0 in range(60):
                    total_mins += 1
                    
    for m0 in range(1,m+1):
        if m0 != m:
            for d0 in range(calendar_leap[m0]):
                for h0 in range(24):
                    for mm0 in range(60):
                        upto_mins += 1
        elif m0 == m:
            for d0 in range(d):
                if d0 != d-1:
                    for h0 in range(24):
                        for mm0 in range(60):
                            upto_mins += 1
                elif d0 == d-1:
                    for h0 in range(hh+1):
                        if h0 != hh:
                            for mm0 in range(60):
                                upto_mins += 1
                        elif h0 == hh:
                            upto_mins += mm                                  
                    
elif not is_leap(y):
    for m0 in range(1, 13):
        for d0 in range(calendar_normal[m0]):
            for h0 in range(24):
                for mm0 in range(60):
                    total_mins += 1
                    
    for m0 in range(1,m+1):
        if m0 != m:
            for d0 in range(calendar_normal[m0]):
                for h0 in range(24):
                    for mm0 in range(60):
                        upto_mins += 1
        elif m0 == m:
            for d0 in range(d):
                if d0 != d-1:
                    for h0 in range(24):
                        for mm0 in range(60):
                            upto_mins += 1
                elif d0 == d-1:
                    for h0 in range(hh+1):
                        if h0 != hh:
                            for mm0 in range(60):
                                upto_mins += 1
                        elif h0 == hh:
                            upto_mins += mm
#print(total_mins) 
#print(upto_mins)
print(upto_mins * 100 / total_mins)          


