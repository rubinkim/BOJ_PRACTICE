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

lst = []
while True:
    a = input()
    b = input()
    if a == '':
        break
    
    a = list(a)
    b = list(b)

    a = set(a)
    b = set(b)
    
    common = a.intersection(b)
    common = sorted(list(common))
    print("".join(common))
    
