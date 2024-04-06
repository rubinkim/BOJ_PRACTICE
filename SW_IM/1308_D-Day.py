#-*- coding: utf-8 -*-
"""
2008 12 27
2009 1 22

(D-26)
"""
def is_leap(yr):
    if yr % 4 == 0 and yr % 100 == 0 and yr % 400 == 0:
        return True
    
        