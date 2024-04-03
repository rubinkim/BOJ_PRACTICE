#-*- coding: utf-8 -*-
"""
mobitel         (bometil)
"""
word = input()
min_ord = 1e5

for ch in word:
    min_ord = min(min_ord, ord(ch))
min_idx = word.index(ch(min_ch))
print(min_ord)
print(min_idx)

min_chr = chr(min_ord)
print(min_chr)