#-*- coding: utf-8 -*-
"""
pretty
women
walking
down
the
street

(e
nw
et)
"""
while True:
    try:
        a = input()
        b = input()
        
        a = list(a)
        b = list(b)

        a = set(a)
        b = set(b)
        
        common = a.intersection(b)
        common = sorted(list(common))
        print("".join(common))
    except:
        break
    
