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
    a = input()
    b = input()
    if a == '':
        exit(0)
    
    a = list(a)
    b = list(b)

    a = set(a)
    b = set(b)
    
    common = a.intersection(b)
    common = sorted(list(common))
    print("".join(common))
    
