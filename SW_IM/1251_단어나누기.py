#-*- coding: utf-8 -*-
"""
mobitel         (bometil)
arrested        (aerrdets)
"""
word = input()
lst = []
for i, ch in enumerate(word):
    lst.append((i, ord(ch)))
print(lst)