#-*- coding: utf-8 -*-
"""
adaabc aababbc
(2)

hello xello
(1)

koder topcoder
(1)

abc topabcoder
(0)

giorgi igroig
(6)
"""

a, b = input().split()
print(f"a : {a},  b : {b}")

diff = len(b) - len(a)
print(f"diff : {diff}")

if diff == 0:
    cnt = 0
    for i in range(len(b)):
        if a[i] != b[i]:
            cnt += 
            
            
else:
    cnt = 51
    for i in range(diff+1):
        if i == 0:
            new_a = a + b[-(diff-i):]
        elif 0 < i < diff:
            new_a = b[:i] + a + b[-(diff-i):]
        elif i == diff:
            new_a = b[:i] + a
        print(f"i : {i},  new_a : {new_a},  b : {b}")
        
        sub_cnt = 0
        for j in range(len(b)):
            if new_a[j] != b[j]:
                sub_cnt += 1
        cnt = min(cnt, sub_cnt)
print(cnt) 
    
    