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