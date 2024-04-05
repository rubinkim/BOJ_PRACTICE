#-*- coding: utf-8 -*-
"""
mobitel         (bometil)
arrested        (aerrdets)
"""
word = input()
lst = []
for i, ch in enumerate(word):
    lst.append((i, ord(ch)))
    
#lst.sort(key=lambda x : (x[1], x[0]))    
print(lst)

min_idx = min([x[1] for x in lst])
print(min_idx)

min_idx_lst = []
for i, ord_ch in lst:
    if ord_ch == min_idx:
        min_idx_lst.append(i)
print(min_idx_lst)



    