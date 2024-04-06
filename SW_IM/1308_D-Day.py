#-*- coding: utf-8 -*-
"""
2008 12 27
2009 1 22

(D-26)
"""
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

sy, sm, sd = map(int, input().split())     # 2008 12 27     2024 1 31   2024 11 30
ey, em, ed = map(int, input().split())     # 2009 1 22

cnt = 0

if sy == ey:
    if is_leap(sy):
        for m in range(sm, em+1):
            if m == sm and m == em:
                cnt += ed - sd
            elif m == sm and em > sm:
                cnt += calendar_leap[m] - sd
            if m > sm and m < em:
                cnt += calendar_leap[m]
            if m == em:
                cnt += ed
                
    elif not is_leap(sy):
        for m in range(sm, em+1):
            if m == sm and m == em:
                cnt += ed - sd
            elif m == sm and em > sm:
                cnt += calendar_normal[m] - sd
            if m > sm and m < em:
                cnt += calendar_normal[m]
            if m == em:
                cnt += ed

elif 0 < ey - sy < 1000:
    for yr in range(sy, ey+1):
        if yr == sy and is_leap(yr):
            for m in range(sm, 13):
                if m == sm:
                    cnt += calendar_leap[m] - sd
                else:
                    cnt += calendar_leap[m]
        elif yr == sy and not is_leap(yr):
            for m in range(sm, 13):
                if m == sm:
                    cnt += calendar_normal[m] - sd
                else:
                    cnt += calendar_normal[m]
                    
        if sy < yr < ey and is_leap(yr):
            cnt += sum(calendar_leap.values())
        elif sy < yr < ey and not is_leap(yr):
            cnt += sum(calendar_normal.values())
            
        if yr == ey and is_leap(yr):
            for m in range(1, em+1):
                if m != em:
                    cnt += calendar_leap[m]
                elif m == em:
                    cnt += ed
        elif yr == ey and not is_leap(yr):
            for m in range(1, em+1):
                if m != em:
                    cnt += calendar_normal[m]
                elif m == em:
                    cnt += ed   
                    
elif ey - sy == 1000:
    if em > sm:
        cnt == "gg"
    elif em == sm and ed >= sd:
        cnt == "gg"
    elif em == sm and ed < sd:
        for yr in range(sy, ey+1):
            if yr == sy and is_leap(yr):
                for m in range(sm, 13):
                    if m == sm:
                        cnt += calendar_leap[m] - sd
                    else:
                        cnt += calendar_leap[m]
            elif yr == sy and not is_leap(yr):
                for m in range(sm, 13):
                    if m == sm:
                        cnt += calendar_normal[m] - sd
                    else:
                        cnt += calendar_normal[m]
                        
            if sy < yr < ey and is_leap(yr):
                cnt += sum(calendar_leap.values())
            elif sy < yr < ey and not is_leap(yr):
                cnt += sum(calendar_normal.values())
                
            if yr == ey and is_leap(yr):
                for m in range(1, em+1):
                    if m != em:
                        cnt += calendar_leap[m]
                    elif m == em:
                        cnt += ed
            elif yr == ey and not is_leap(yr):
                for m in range(1, em+1):
                    if m != em:
                        cnt += calendar_normal[m]
                    elif m == em:
                        cnt += ed

elif ey - sy > 1000:
    cnt == "gg"  